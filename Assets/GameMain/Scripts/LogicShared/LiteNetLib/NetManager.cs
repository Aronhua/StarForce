﻿/*
* 文件名：NetManager
* 文件描述：
* 作者：aronliang
* 创建时间：2023/07/21 19:19:24
* 修改记录：
*/

using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using System.Threading;
using LogicShared.LiteNetLib.Layers;
using LogicShared.LiteNetLib.Utils;

namespace LogicShared.LiteNetLib
{
    public enum IPv6Mode
    {
        Disabled,
        SeparateSocket,
        DualMode
    }
    
    /// <summary>
    /// 包读取器
    /// </summary>
    public sealed class NetPacketReader : NetDataReader
    {
        private NetPacket _packet;
        private readonly NetManager _manager;
        private readonly NetEvent _evt;

        internal NetPacketReader(NetManager manager, NetEvent evt)
        {
            _manager = manager;
            _evt = evt;
        }

        internal void SetSource(NetPacket packet, int headerSize)
        {
            if (packet == null)
                return;
            _packet = packet;
            SetSource(packet.RawData, headerSize, packet.Size);
        }

        /// <summary>
        /// 内部回收_packet和_evt
        /// </summary>
        internal void RecycleInternal()
        {
            Clear();
            if (_packet != null)
                _manager.NetPacketPool.Recycle(_packet);
            _packet = null;
            _manager.RecycleEvent(_evt);
        }

        /// <summary>
        /// 回收_packet和_evt
        /// </summary>
        /// <exception cref="Exception"></exception>
        public void Recycle()
        {
            if(_manager.AutoRecycle)
                throw new Exception("Recycle called with AutoRecycle enabled");
            RecycleInternal();
        }
    }

    /// <summary>
    /// 网络事件：连接事件，断开连接事件，收到网络包消息事件等
    /// </summary>
    internal sealed class NetEvent
    {
        public NetEvent Next;

        public enum EType
        {
            Connect,                    //有新的peer连接成功
            Disconnect,                 //peer断开连接
            Receive,                    //peer收到消息（必须连接成功）
            ReceiveUnconnected,         //peer收到消息（无需连接成功）
            Error,                      //连接错误
            ConnectionLatencyUpdated,   //连接延迟
            Broadcast,                  //广播消息
            ConnectionRequest,          //peer发送连接请求
            MessageDelivered            //派发消息，通知其他系统
        }
        public EType Type;

        public NetPeer Peer;
        public IPEndPoint RemoteEndPoint;
        public object UserData;
        public int Latency;
        public SocketError ErrorCode;
        public DisconnectReason DisconnectReason;
        public ConnectionRequest ConnectionRequest;
        public DeliveryMethod DeliveryMethod;
        public readonly NetPacketReader DataReader;

        public NetEvent(NetManager manager)
        {
            DataReader = new NetPacketReader(manager, this);
        }
    }
    /// <summary>
    /// 管理发送和接收等事件
    /// </summary>
    public class NetManager : INetSocketListener, IEnumerable<NetPeer>
    {
        /// <summary>
        /// 重写EndPoint比较方法（等于或不等于）
        /// </summary>
        private class IPEndPointComparer : IEqualityComparer<IPEndPoint>
        {
            /// <summary>
            /// ip和port都相等才认为相等
            /// </summary>
            /// <param name="x"></param>
            /// <param name="y"></param>
            /// <returns></returns>
            public bool Equals(IPEndPoint x, IPEndPoint y)
            {
                return x.Address.Equals(y.Address) && x.Port == y.Port;
            }

            public int GetHashCode(IPEndPoint obj)
            {
                return obj.GetHashCode();
            }
        }

        /// <summary>
        /// Peer迭代器，通过Peer.NextPeer进行迭代
        /// </summary>
        public struct NetPeerEnumerator : IEnumerator<NetPeer>
        {
            private readonly NetPeer _initialPeer;
            private NetPeer _peer;

            public NetPeerEnumerator(NetPeer peer)
            {
                _initialPeer = peer;
                _peer = null;
            }

            public void Dispose()
            {

            }

            public bool MoveNext()
            {
                _peer = _peer == null ? _initialPeer : _peer.NextPeer;
                return _peer != null;
            }

            public void Reset()
            {
                throw new NotSupportedException();
            }

            public NetPeer Current
            {
                get { return _peer; }
            }

            object IEnumerator.Current
            {
                get { return _peer; }
            }
        }
        
        #if DEBUG
        private struct IncomingData
        {
            public byte[] Data;
            public IPEndPoint EndPoint;
            public DateTime TimeWhenGet;
        }
        private readonly List<IncomingData> _pingSimulationList = new List<IncomingData>(); 
        private readonly Random _randomGenerator = new Random();
        private const int MinLatencyThreshold = 5;      //最小ping
#endif

        private readonly NetSocket _socket;                 //收发socket
        private Thread _logicThread;                        //逻辑线程
        private readonly AutoResetEvent _updateTriggerEvent = new AutoResetEvent(true);

        private readonly Queue<NetEvent> _netEventsQueue;   //网络事件队列
        private NetEvent _netEventPoolHead;                 //网络事件对象池中第一个可用的对象
        private readonly INetEventListener _netEventListener;                       //网络事件监听器
        private readonly IDeliveryEventListener _deliveryEventListener;             //派发事件监听器
    
        private readonly Dictionary<IPEndPoint, NetPeer> _peersDict;                //所有Peer字典
        private readonly Dictionary<IPEndPoint, ConnectionRequest> _requestsDict;   //请求连接网络包字典
        private readonly ReaderWriterLockSlim _peersLock;   //peers读写锁
        private volatile NetPeer _headPeer;                 //已连接的peer中最后一个添加进来的peer
        private volatile int _connectedPeersCount;          //已连接成功的peer数量
        private readonly List<NetPeer> _connectedPeerListCache; //缓存已连接成功的peer列表
        private NetPeer[] _peersArray;                      //已连接的peer数组，数组索引是peer.Id
        private readonly PacketLayerBase _extraPacketLayer; //额外的packet层
        private int _lastPeerId;                            //上一个被使用的PeerId
        private readonly Queue<int> _peerIds;               //PeerId对象池
        private byte _channelsCount = 1;                    //频道数量

        internal readonly NetPacketPool NetPacketPool;      //网络包对象池
        
        #region config section
        
        /// <summary>
        /// Enable messages receiving without connection. (with SendUnconnectedMessage method)
        /// </summary>
        public bool UnconnectedMessagesEnabled = false; 

        /// <summary>
        /// Enable nat punch messages
        /// 启用NAT打洞
        /// </summary>
        public bool NatPunchEnabled = false;

        /// <summary>
        /// Library logic update and send period in milliseconds
        /// </summary>
        public int UpdateTime = 15;

        /// <summary>
        /// Interval for latency detection and checking connection in milliseconds
        /// </summary>
        public int PingInterval = 10000;

        /// <summary>
        /// If NetManager doesn't receive any packet from remote peer during this time then connection will be closed
        /// (including library internal keepalive packets)
        /// </summary>
        public int DisconnectTimeout = 50000;

        /// <summary>
        /// Simulate packet loss by dropping random amount of packets. (Works only in DEBUG mode)
        /// 模拟丢包
        /// </summary>
        public bool SimulatePacketLoss = false;

        /// <summary>
        /// Simulate latency by holding packets for random time. (Works only in DEBUG mode)
        /// 模拟延迟
        /// </summary>
        public bool SimulateLatency = false;

        /// <summary>
        /// Chance of packet loss when simulation enabled. value in percents (1 - 100).
        /// 模拟丢包概率（1-100）
        /// </summary>
        public int SimulationPacketLossChance = 10;

        /// <summary>
        /// Minimum simulated latency
        /// 最小模拟延迟
        /// </summary>
        public int SimulationMinLatency = 30;

        /// <summary>
        /// Maximum simulated latency
        /// 最大模拟延迟
        /// </summary>
        public int SimulationMaxLatency = 100;

        /// <summary>
        /// Events automatically will be called without PollEvents method from another thread
        /// </summary>
        public bool UnsyncedEvents = false;

        /// <summary>
        /// If true - receive event will be called from "receive" thread immediately otherwise on PollEvents call
        /// </summary>
        public bool UnsyncedReceiveEvent = false;

        /// <summary>
        /// If true - delivery event will be called from "receive" thread immediately otherwise on PollEvents call
        /// </summary>
        public bool UnsyncedDeliveryEvent = false;

        /// <summary>
        /// Allows receive broadcast packets
        /// </summary>
        public bool BroadcastReceiveEnabled = false;

        /// <summary>
        /// Delay between initial connection attempts
        /// </summary>
        public int ReconnectDelay = 500;

        /// <summary>
        /// Maximum connection attempts before client stops and call disconnect event.
        /// </summary>
        public int MaxConnectAttempts = 10;

        /// <summary>
        /// Enables socket option "ReuseAddress" for specific purposes
        /// </summary>
        public bool ReuseAddress = false;

        /// <summary>
        /// Statistics of all connections
        /// </summary>
        public readonly NetStatistics Statistics;

        /// <summary>
        /// Toggles the collection of network statistics for the instance and all known peers
        /// </summary>
        public bool EnableStatistics = false;

        /// <summary>
        /// NatPunchModule for NAT hole punching operations
        /// </summary>
        public readonly NatPunchModule NatPunchModule;

        /// <summary>
        /// Returns true if socket listening and update thread is running
        /// </summary>
        public bool IsRunning { get { return _socket.IsRunning; } }

        /// <summary>
        /// Local EndPoint (host and port)
        /// </summary>
        public int LocalPort { get { return _socket.LocalPort; } }

        /// <summary>
        /// Automatically recycle NetPacketReader after OnReceive event
        /// </summary>
        public bool AutoRecycle;

        /// <summary>
        /// IPv6 support
        /// </summary>
        public IPv6Mode IPv6Enabled = IPv6Mode.SeparateSocket;

        /// <summary>
        /// First peer. Useful for Client mode
        /// </summary>
        public NetPeer FirstPeer
        {
            get { return _headPeer; }
        }

        /// <summary>
        /// QoS channel count per message type (value must be between 1 and 64 channels)
        /// </summary>
        public byte ChannelsCount
        {
            get { return _channelsCount; }
            set
            {
                if (value < 1 || value > 64)
                    throw new ArgumentException("Channels count must be between 1 and 64");
                _channelsCount = value;
            }
        }

        /// <summary>
        /// Returns connected peers list (with internal cached list)
        /// </summary>
        public List<NetPeer> ConnectedPeerList
        {
            get
            {
                GetPeersNonAlloc(_connectedPeerListCache, ConnectionState.Connected);
                return _connectedPeerListCache;
            }
        }

        /// <summary>
        /// Gets peer by peer id
        /// </summary>
        /// <param name="id">id of peer</param>
        /// <returns>Peer if peer with id exist, otherwise null</returns>
        public NetPeer GetPeerById(int id)
        {
            return _peersArray[id];
        }

        /// <summary>
        /// Returns connected peers count
        /// </summary>
        public int ConnectedPeersCount { get { return _connectedPeersCount; } }
        
        /// <summary>
        /// 其他layer的额外packet数量
        /// </summary>
        public int ExtraPacketSizeForLayer
        {
            get { return _extraPacketLayer != null ? _extraPacketLayer.ExtraPacketSizeForLayer : 0; }
        }

        #endregion
        
        /// <summary>
        /// NetManager constructor
        /// </summary>
        /// <param name="listener">Network events listener (also can implement IDeliveryEventListener)</param>
        /// <param name="extraPacketLayer">Extra processing of packages, like CRC checksum or encryption. All connected NetManagers must have same layer.</param>
        public NetManager(INetEventListener listener, PacketLayerBase extraPacketLayer = null)
        {
            _socket = new NetSocket(this);
            _netEventListener = listener;
            _deliveryEventListener = listener as IDeliveryEventListener;
            _netEventsQueue = new Queue<NetEvent>();
            NetPacketPool = new NetPacketPool();
            NatPunchModule = new NatPunchModule(_socket);
            Statistics = new NetStatistics();
            _connectedPeerListCache = new List<NetPeer>();
            _peersDict = new Dictionary<IPEndPoint, NetPeer>(new IPEndPointComparer());
            _requestsDict = new Dictionary<IPEndPoint, ConnectionRequest>(new IPEndPointComparer());
            _peersLock = new ReaderWriterLockSlim(LockRecursionPolicy.NoRecursion);
            _peerIds = new Queue<int>();
            _peersArray = new NetPeer[32];
            _extraPacketLayer = extraPacketLayer;
        }
        
        #region Start and Stop Logic
        
        /// <summary>
        /// Start logic thread and listening on available port
        /// </summary>
        public bool Start()
        {
            return Start(0);
        }

        /// <summary>
        /// Start logic thread and listening on selected port
        /// </summary>
        /// <param name="addressIPv4">bind to specific ipv4 address</param>
        /// <param name="addressIPv6">bind to specific ipv6 address</param>
        /// <param name="port">port to listen</param>
        public bool Start(IPAddress addressIPv4, IPAddress addressIPv6, int port)
        {
            if (!_socket.Bind(addressIPv4, addressIPv6, port, ReuseAddress, IPv6Enabled))
                return false;
            _logicThread = new Thread(UpdateLogic) { Name = "LogicThread", IsBackground = true };
            _logicThread.Start();
            return true;
        }

        /// <summary>
        /// Start logic thread and listening on selected port
        /// </summary>
        /// <param name="addressIPv4">bind to specific ipv4 address</param>
        /// <param name="addressIPv6">bind to specific ipv6 address</param>
        /// <param name="port">port to listen</param>
        public bool Start(string addressIPv4, string addressIPv6, int port)
        {
            IPAddress ipv4 = NetUtils.ResolveAddress(addressIPv4);
            IPAddress ipv6 = NetUtils.ResolveAddress(addressIPv6);
            return Start(ipv4, ipv6, port);
        }

        /// <summary>
        /// Start logic thread and listening on selected port
        /// </summary>
        /// <param name="port">port to listen</param>
        public bool Start(int port)
        {
            return Start(IPAddress.Any, IPAddress.IPv6Any, port);
        }

        /// <summary>
        /// Force closes connection and stop all threads.
        /// </summary>
        public void Stop()
        {
            Stop(true);
        }

        /// <summary>
        /// Force closes connection and stop all threads.
        /// </summary>
        /// <param name="sendDisconnectMessages">Send disconnect messages</param>
        public void Stop(bool sendDisconnectMessages)
        {
            if (!_socket.IsRunning)
                return;
            Logger.Debug("[NM] Stop");

            //Send last disconnect
            for(var netPeer = _headPeer; netPeer != null; netPeer = netPeer.NextPeer)
                netPeer.Shutdown(null, 0, 0, !sendDisconnectMessages);

            //Stop
            _socket.Close(false);
            _updateTriggerEvent.Set();
            _logicThread.Join();
            _logicThread = null;

            //clear peers
            _peersLock.EnterWriteLock();
            _headPeer = null;
            _peersDict.Clear();
            _peersArray = new NetPeer[32];
            _peersLock.ExitWriteLock();
            lock(_peerIds)
                _peerIds.Clear();
#if DEBUG
            lock (_pingSimulationList)
                _pingSimulationList.Clear();
#endif
            _connectedPeersCount = 0;
            lock(_netEventsQueue)
                _netEventsQueue.Clear();
        }
        
        #endregion
        
        #region Add or Remove Peer Method
        
        /// <summary>
        /// 添加一个新的Peer
        /// </summary>
        /// <param name="peer"></param>
        private void AddPeer(NetPeer peer)
        {
            _peersLock.EnterWriteLock();
            if (_headPeer != null)
            {
                peer.NextPeer = _headPeer;
                _headPeer.PrevPeer = peer;
            }
            //headPeer = 最后添加的peer
            _headPeer = peer;
            _peersDict.Add(peer.EndPoint, peer);
            if (peer.Id >= _peersArray.Length)
            {
                int newSize = _peersArray.Length * 2;
                while (peer.Id >= newSize)
                    newSize *= 2;
                Array.Resize(ref _peersArray, newSize);
            }
            _peersArray[peer.Id] = peer;
            _peersLock.ExitWriteLock();
        }

        private void RemovePeer(NetPeer peer)
        {
            _peersLock.EnterWriteLock();
            RemovePeerInternal(peer);
            _peersLock.ExitWriteLock();
        }
        
        private void RemovePeerInternal(NetPeer peer)
        {
            if (!_peersDict.Remove(peer.EndPoint))
                return;
            if (peer == _headPeer)
                _headPeer = peer.NextPeer;

            //从双链表中移除一个元素
            if (peer.PrevPeer != null)
                peer.PrevPeer.NextPeer = peer.NextPeer;
            if (peer.NextPeer != null)
                peer.NextPeer.PrevPeer = peer.PrevPeer;
            peer.PrevPeer = null;

            _peersArray[peer.Id] = null;
            lock (_peerIds)
                _peerIds.Enqueue(peer.Id);
        }

        #endregion
        
        #region Net Event Method
        
        internal void ConnectionLatencyUpdated(NetPeer fromPeer, int latency)
        {
            CreateEvent(NetEvent.EType.ConnectionLatencyUpdated, fromPeer, latency: latency);
        }

        internal void MessageDelivered(NetPeer fromPeer, object userData)
        {
            if(_deliveryEventListener != null)
                CreateEvent(NetEvent.EType.MessageDelivered, fromPeer, userData: userData);
        }
        
         /// <summary>
        /// 创建网络事件
        /// </summary>
        /// <param name="type"></param>
        /// <param name="peer"></param>
        /// <param name="remoteEndPoint"></param>
        /// <param name="errorCode"></param>
        /// <param name="latency"></param>
        /// <param name="disconnectReason"></param>
        /// <param name="connectionRequest"></param>
        /// <param name="deliveryMethod"></param>
        /// <param name="readerSource"></param>
        /// <param name="userData"></param>
        private void CreateEvent(
            NetEvent.EType type,
            NetPeer peer = null,
            IPEndPoint remoteEndPoint = null,
            SocketError errorCode = 0,
            int latency = 0,
            DisconnectReason disconnectReason = DisconnectReason.ConnectionFailed,
            ConnectionRequest connectionRequest = null,
            DeliveryMethod deliveryMethod = DeliveryMethod.Unreliable,
            NetPacket readerSource = null,
            object userData = null)
        {
            NetEvent evt;
            bool unsyncEvent = UnsyncedEvents;
            
            if (type == NetEvent.EType.Connect)
                Interlocked.Increment(ref _connectedPeersCount);
            else if (type == NetEvent.EType.MessageDelivered)
                unsyncEvent = UnsyncedDeliveryEvent;

            do
            {
                evt = _netEventPoolHead;
                if (evt == null)
                {
                    evt = new NetEvent(this);
                    break;
                }
            } while (evt != Interlocked.CompareExchange(ref _netEventPoolHead, evt.Next, evt));

            evt.Type = type;
            evt.DataReader.SetSource(readerSource, readerSource == null ? 0 : readerSource.GetHeaderSize());
            evt.Peer = peer;
            evt.RemoteEndPoint = remoteEndPoint;
            evt.Latency = latency;
            evt.ErrorCode = errorCode;
            evt.DisconnectReason = disconnectReason;
            evt.ConnectionRequest = connectionRequest;
            evt.DeliveryMethod = deliveryMethod;
            evt.UserData = userData;

            //不需要PoolEvent
            if (unsyncEvent)
            {
                ProcessEvent(evt);
            }
            else
            {
                lock (_netEventsQueue)
                    _netEventsQueue.Enqueue(evt);
            }
        }

        /// <summary>
        /// 处理网络事件
        /// </summary>
        /// <param name="evt"></param>
        private void ProcessEvent(NetEvent evt)
        {
            //Logger.Debug("[NM] Processing event: " + evt.Type);
            bool emptyData = evt.DataReader.IsNull;
            switch (evt.Type)
            {
                case NetEvent.EType.Connect:
                    _netEventListener.OnPeerConnected(evt.Peer);
                    break;
                case NetEvent.EType.Disconnect:
                    var info = new DisconnectInfo
                    {
                        Reason = evt.DisconnectReason,
                        AdditionalData = evt.DataReader,
                        SocketErrorCode = evt.ErrorCode
                    };
                    _netEventListener.OnPeerDisconnected(evt.Peer, info);
                    break;
                case NetEvent.EType.Receive:
                    _netEventListener.OnNetworkReceive(evt.Peer, evt.DataReader, evt.DeliveryMethod);
                    break;
                case NetEvent.EType.ReceiveUnconnected:
                    _netEventListener.OnNetworkReceiveUnconnected(evt.RemoteEndPoint, evt.DataReader, UnconnectedMessageType.BasicMessage);
                    break;
                case NetEvent.EType.Broadcast:
                    _netEventListener.OnNetworkReceiveUnconnected(evt.RemoteEndPoint, evt.DataReader, UnconnectedMessageType.Broadcast);
                    break;
                case NetEvent.EType.Error:
                    _netEventListener.OnNetworkError(evt.RemoteEndPoint, evt.ErrorCode);
                    break;
                case NetEvent.EType.ConnectionLatencyUpdated:
                    _netEventListener.OnNetworkLatencyUpdate(evt.Peer, evt.Latency);
                    break;
                case NetEvent.EType.ConnectionRequest:
                    _netEventListener.OnConnectionRequest(evt.ConnectionRequest);
                    break;
                case NetEvent.EType.MessageDelivered:
                    _deliveryEventListener.OnMessageDelivered(evt.Peer, evt.UserData);
                    break;
            }
            //Recycle if not message
            if (emptyData)
                RecycleEvent(evt);
            else if (AutoRecycle)
                evt.DataReader.RecycleInternal();
        }

        /// <summary>
        /// 回收网络事件
        /// </summary>
        /// <param name="evt"></param>
        internal void RecycleEvent(NetEvent evt)
        {
            evt.Peer = null;
            evt.ErrorCode = 0;
            evt.RemoteEndPoint = null;
            evt.ConnectionRequest = null;
            do
            {
                evt.Next = _netEventPoolHead;
            } while (evt.Next != Interlocked.CompareExchange(ref _netEventPoolHead, evt, evt.Next));
        }
        #endregion
        
        #region Send Methods
        
        /// <summary>
        /// Send data to all connected peers (channel = 0)
        /// </summary>
        /// <param name="writer">DataWriter with data</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        public void SendToAll(NetDataWriter writer, DeliveryMethod options)
        {
            SendToAll(writer.Data, 0, writer.Length, options);
        }

        /// <summary>
        /// Send data to all connected peers (channel = 0)
        /// </summary>
        /// <param name="data">Data</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        public void SendToAll(byte[] data, DeliveryMethod options)
        {
            SendToAll(data, 0, data.Length, options);
        }

        /// <summary>
        /// Send data to all connected peers (channel = 0)
        /// </summary>
        /// <param name="data">Data</param>
        /// <param name="start">Start of data</param>
        /// <param name="length">Length of data</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        public void SendToAll(byte[] data, int start, int length, DeliveryMethod options)
        {
            SendToAll(data, start, length, 0, options);
        }

        /// <summary>
        /// Send data to all connected peers
        /// </summary>
        /// <param name="writer">DataWriter with data</param>
        /// <param name="channelNumber">Number of channel (from 0 to channelsCount - 1)</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        public void SendToAll(NetDataWriter writer, byte channelNumber, DeliveryMethod options)
        {
            SendToAll(writer.Data, 0, writer.Length, channelNumber, options);
        }

        /// <summary>
        /// Send data to all connected peers
        /// </summary>
        /// <param name="data">Data</param>
        /// <param name="channelNumber">Number of channel (from 0 to channelsCount - 1)</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        public void SendToAll(byte[] data, byte channelNumber, DeliveryMethod options)
        {
            SendToAll(data, 0, data.Length, channelNumber, options);
        }

        /// <summary>
        /// Send data to all connected peers
        /// </summary>
        /// <param name="data">Data</param>
        /// <param name="start">Start of data</param>
        /// <param name="length">Length of data</param>
        /// <param name="channelNumber">Number of channel (from 0 to channelsCount - 1)</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        public void SendToAll(byte[] data, int start, int length, byte channelNumber, DeliveryMethod options)
        {
            try
            {
                _peersLock.EnterReadLock();
                for (var netPeer = _headPeer; netPeer != null; netPeer = netPeer.NextPeer)
                    netPeer.Send(data, start, length, channelNumber, options);
            }
            finally
            {
                _peersLock.ExitReadLock();
            }
        }

        /// <summary>
        /// Send data to all connected peers (channel = 0)
        /// </summary>
        /// <param name="writer">DataWriter with data</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        /// <param name="excludePeer">Excluded peer</param>
        public void SendToAll(NetDataWriter writer, DeliveryMethod options, NetPeer excludePeer)
        {
            SendToAll(writer.Data, 0, writer.Length, 0, options, excludePeer);
        }

        /// <summary>
        /// Send data to all connected peers (channel = 0)
        /// </summary>
        /// <param name="data">Data</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        /// <param name="excludePeer">Excluded peer</param>
        public void SendToAll(byte[] data, DeliveryMethod options, NetPeer excludePeer)
        {
            SendToAll(data, 0, data.Length, 0, options, excludePeer);
        }

        /// <summary>
        /// Send data to all connected peers (channel = 0)
        /// </summary>
        /// <param name="data">Data</param>
        /// <param name="start">Start of data</param>
        /// <param name="length">Length of data</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        /// <param name="excludePeer">Excluded peer</param>
        public void SendToAll(byte[] data, int start, int length, DeliveryMethod options, NetPeer excludePeer)
        {
            SendToAll(data, start, length, 0, options, excludePeer);
        }

        /// <summary>
        /// Send data to all connected peers
        /// </summary>
        /// <param name="writer">DataWriter with data</param>
        /// <param name="channelNumber">Number of channel (from 0 to channelsCount - 1)</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        /// <param name="excludePeer">Excluded peer</param>
        public void SendToAll(NetDataWriter writer, byte channelNumber, DeliveryMethod options, NetPeer excludePeer)
        {
            SendToAll(writer.Data, 0, writer.Length, channelNumber, options, excludePeer);
        }

        /// <summary>
        /// Send data to all connected peers
        /// </summary>
        /// <param name="data">Data</param>
        /// <param name="channelNumber">Number of channel (from 0 to channelsCount - 1)</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        /// <param name="excludePeer">Excluded peer</param>
        public void SendToAll(byte[] data, byte channelNumber, DeliveryMethod options, NetPeer excludePeer)
        {
            SendToAll(data, 0, data.Length, channelNumber, options, excludePeer);
        }


        /// <summary>
        /// Send data to all connected peers
        /// </summary>
        /// <param name="data">Data</param>
        /// <param name="start">Start of data</param>
        /// <param name="length">Length of data</param>
        /// <param name="channelNumber">Number of channel (from 0 to channelsCount - 1)</param>
        /// <param name="options">Send options (reliable, unreliable, etc.)</param>
        /// <param name="excludePeer">Excluded peer</param>
        public void SendToAll(byte[] data, int start, int length, byte channelNumber, DeliveryMethod options, NetPeer excludePeer)
        {
            try
            {
                _peersLock.EnterReadLock();
                for (var netPeer = _headPeer; netPeer != null; netPeer = netPeer.NextPeer)
                {
                    if (netPeer != excludePeer)
                        netPeer.Send(data, start, length, channelNumber, options);
                }
            }
            finally
            {
                _peersLock.ExitReadLock();
            }
        }
        
        /// <summary>
        /// Send message without connection
        /// </summary>
        /// <param name="message">Raw data</param>
        /// <param name="remoteEndPoint">Packet destination</param>
        /// <returns>Operation result</returns>
        public bool SendUnconnectedMessage(byte[] message, IPEndPoint remoteEndPoint)
        {
            return SendUnconnectedMessage(message, 0, message.Length, remoteEndPoint);
        }

        /// <summary>
        /// Send message without connection
        /// </summary>
        /// <param name="writer">Data serializer</param>
        /// <param name="remoteEndPoint">Packet destination</param>
        /// <returns>Operation result</returns>
        public bool SendUnconnectedMessage(NetDataWriter writer, IPEndPoint remoteEndPoint)
        {
            return SendUnconnectedMessage(writer.Data, 0, writer.Length, remoteEndPoint);
        }

        /// <summary>
        /// Send message without connection
        /// </summary>
        /// <param name="message">Raw data</param>
        /// <param name="start">data start</param>
        /// <param name="length">data length</param>
        /// <param name="remoteEndPoint">Packet destination</param>
        /// <returns>Operation result</returns>
        public bool SendUnconnectedMessage(byte[] message, int start, int length, IPEndPoint remoteEndPoint)
        {
            //No need for CRC here, SendRaw does that
            NetPacket packet = NetPacketPool.GetWithData(PacketProperty.UnconnectedMessage, message, start, length);
            return SendRawAndRecycle(packet, remoteEndPoint) > 0;
        }

        internal int SendRawAndRecycle(NetPacket packet, IPEndPoint remoteEndPoint)
        {
            var result = SendRaw(packet.RawData, 0, packet.Size, remoteEndPoint);
            NetPacketPool.Recycle(packet);
            return result;
        }

        internal int SendRaw(NetPacket packet, IPEndPoint remoteEndPoint)
        {
            return SendRaw(packet.RawData, 0, packet.Size, remoteEndPoint);
        }

        /// <summary>
        /// 发送byte数组形式的消息
        /// </summary>
        /// <param name="message"></param>
        /// <param name="start"></param>
        /// <param name="length"></param>
        /// <param name="remoteEndPoint"></param>
        /// <returns></returns>
        internal int SendRaw(byte[] message, int start, int length, IPEndPoint remoteEndPoint)
        {
            if (!_socket.IsRunning)
                return 0;

            SocketError errorCode = 0;
            int result;
            if (_extraPacketLayer != null)  //添加CRC校验等数据之后再发送
            {
                var expandedPacket = NetPacketPool.GetPacket(length + _extraPacketLayer.ExtraPacketSizeForLayer);
                Buffer.BlockCopy(message, start, expandedPacket.RawData, 0, length);
                int newStart = 0;
                _extraPacketLayer.ProcessOutBoundPacket(remoteEndPoint, ref expandedPacket.RawData, ref newStart, ref length);
                result = _socket.SendTo(expandedPacket.RawData, newStart, length, remoteEndPoint, ref errorCode);
                NetPacketPool.Recycle(expandedPacket);
            }
            else
            {
                //否则直接发送
                result = _socket.SendTo(message, start, length, remoteEndPoint, ref errorCode);
            }

            //因为是同步发送，因此到这里就已经知道发送的结果了
            NetPeer fromPeer;
            switch (errorCode)
            {
                case SocketError.MessageSize:                       //返回消息长度
                    Logger.Debug($"[SRD] 10040, data length: {length}");
                    return -1;
                case SocketError.HostUnreachable:
                    if (TryGetPeer(remoteEndPoint, out fromPeer))   //不能达到远端主服务器
                        DisconnectPeerForce(fromPeer, DisconnectReason.HostUnreachable, errorCode, null);
                    CreateEvent(NetEvent.EType.Error, remoteEndPoint: remoteEndPoint, errorCode: errorCode);
                    return -1;
                case SocketError.NetworkUnreachable:                //网络不通
                    if (TryGetPeer(remoteEndPoint, out fromPeer))
                        DisconnectPeerForce(fromPeer, DisconnectReason.NetworkUnreachable, errorCode, null);
                    CreateEvent(NetEvent.EType.Error, remoteEndPoint: remoteEndPoint, errorCode: errorCode);
                    return -1;
            }
            if (result <= 0)
                return 0;

            if (EnableStatistics)
            {
                Statistics.IncrementPacketsSent();
                Statistics.AddBytesSent(length);
            }

            return result;
        }
        
        public bool SendBroadcast(NetDataWriter writer, int port)
        {
            return SendBroadcast(writer.Data, 0, writer.Length, port);
        }

        public bool SendBroadcast(byte[] data, int port)
        {
            return SendBroadcast(data, 0, data.Length, port);
        }

        public bool SendBroadcast(byte[] data, int start, int length, int port)
        {
            NetPacket packet;
            if (_extraPacketLayer != null)
            {
                var headerSize = NetPacket.GetHeaderSize(PacketProperty.Broadcast);
                packet = NetPacketPool.GetPacket(headerSize + length + _extraPacketLayer.ExtraPacketSizeForLayer);
                packet.Property = PacketProperty.Broadcast;
                Buffer.BlockCopy(data, start, packet.RawData, headerSize, length);
                var checksumComputeStart = 0;
                int preCrcLength = length + headerSize;
                _extraPacketLayer.ProcessOutBoundPacket(null, ref packet.RawData, ref checksumComputeStart, ref preCrcLength);
            }
            else
            {
                packet = NetPacketPool.GetWithData(PacketProperty.Broadcast, data, start, length);
            }

            bool result = _socket.SendBroadcast(packet.RawData, 0, packet.Size, port);
            NetPacketPool.Recycle(packet);
            return result;
        }
        
        #endregion
        
        #region Update Method
        /// <summary>
        /// Triggers update and send logic immediately (works asynchronously)
        /// </summary>
        public void TriggerUpdate()
        {
            _updateTriggerEvent.Set();
        }

        /// <summary>
        /// Receive all pending events. Call this in game update code
        /// </summary>
        public void PollEvents()
        {
            if (UnsyncedEvents)
                return;
            int eventsCount;
            lock (_netEventsQueue)
                eventsCount = _netEventsQueue.Count;
            for(int i = 0; i < eventsCount; i++)
            {
                NetEvent evt;
                lock (_netEventsQueue)
                    evt = _netEventsQueue.Dequeue();
                ProcessEvent(evt);
            }
        }
        
  /// <summary>
        /// 在_logicThread线程中更新网络逻辑
        /// </summary>
        private void UpdateLogic()
        {
            var peersToRemove = new List<NetPeer>();    //待移除的peer列表
            var stopwatch = new Stopwatch();
            stopwatch.Start();

            while (_socket.IsRunning)
            {
#if DEBUG   //模拟丢包和延迟
                if (SimulateLatency)
                {
                    var time = DateTime.UtcNow;
                    lock (_pingSimulationList)
                    {
                        for (int i = 0; i < _pingSimulationList.Count; i++)
                        {
                            var incomingData = _pingSimulationList[i];
                            if (incomingData.TimeWhenGet <= time)
                            {
                                DataReceived(incomingData.Data, incomingData.Data.Length, incomingData.EndPoint);
                                _pingSimulationList.RemoveAt(i);
                                i--;
                            }
                        }
                    }
                }
#endif

                int elapsed = (int)stopwatch.ElapsedMilliseconds;
                elapsed = elapsed <= 0 ? 1 : elapsed;
                stopwatch.Reset();
                stopwatch.Start();

                //遍历所有连接的peer
                for (var netPeer = _headPeer; netPeer != null; netPeer = netPeer.NextPeer)
                {
                    if (netPeer.ConnectionState == ConnectionState.Disconnected && netPeer.TimeSinceLastPacket > DisconnectTimeout)
                    {
                        peersToRemove.Add(netPeer); 
                    }
                    else
                    {
                        netPeer.Update(elapsed);
                    }
                }
                if (peersToRemove.Count > 0)
                {
                    _peersLock.EnterWriteLock();
                    for (int i = 0; i < peersToRemove.Count; i++)
                        RemovePeerInternal(peersToRemove[i]);
                    _peersLock.ExitWriteLock();
                    peersToRemove.Clear();
                }

                int sleepTime = UpdateTime - (int)stopwatch.ElapsedMilliseconds;
                if (sleepTime > 0)
                    _updateTriggerEvent.WaitOne(sleepTime); //线程等待sleepTime
            }
            stopwatch.Stop();
        }
      

        #endregion
        
        #region Handle Message Method

          
        /// <summary>
        /// 收到socket接收到的原始数据
        /// </summary>
        /// <param name="data"></param>
        /// <param name="length"></param>
        /// <param name="errorCode"></param>
        /// <param name="remoteEndPoint"></param>
        void INetSocketListener.OnMessageReceived(byte[] data, int length, SocketError errorCode, IPEndPoint remoteEndPoint)
        {
            //出错了，创建报错事件
            if (errorCode != 0)
            {
                CreateEvent(NetEvent.EType.Error, errorCode: errorCode);
                Logger.Error($"[NM] Receive error: {errorCode}");
                return;
            }
#if DEBUG   //模拟丢包和延迟
            if (SimulatePacketLoss && _randomGenerator.NextDouble() * 100 < SimulationPacketLossChance)
            {
                //drop packet
                return;
            }
            if (SimulateLatency)
            {
                int latency = _randomGenerator.Next(SimulationMinLatency, SimulationMaxLatency);
                if (latency > MinLatencyThreshold)
                {
                    byte[] holdedData = new byte[length];
                    Buffer.BlockCopy(data, 0, holdedData, 0, length);

                    lock (_pingSimulationList)
                    {
                        _pingSimulationList.Add(new IncomingData
                        {
                            Data = holdedData,
                            EndPoint = remoteEndPoint,
                            TimeWhenGet = DateTime.UtcNow.AddMilliseconds(latency)
                        });
                    }
                    //hold packet
                    return;
                }
            }
#endif
            try
            {
                //ProcessEvents
                DataReceived(data, length, remoteEndPoint);
            }
            catch(Exception e)
            {
                //protects socket receive thread
                Logger.Error("[NM] SocketReceiveThread error: " + e );
            }
        }

        /// <summary>
        /// 处理客户端连接请求
        /// </summary>
        /// <param name="request"></param>
        /// <param name="rejectData"></param>
        /// <param name="start"></param>
        /// <param name="length"></param>
        /// <returns></returns>
        internal NetPeer OnConnectionSolved(ConnectionRequest request, byte[] rejectData, int start, int length)
        {
            NetPeer netPeer = null;

            if (request.Result == ConnectionRequestResult.RejectForce)
            {
                Logger.Debug( "[NM] Peer connect reject force.");
                if (rejectData != null && length > 0)
                {
                    var shutdownPacket = NetPacketPool.GetWithProperty(PacketProperty.Disconnect, length);
                    shutdownPacket.ConnectionNumber = request.ConnectionNumber;
                    FastBitConverter.GetBytes(shutdownPacket.RawData, 1, request.ConnectionTime);
                    if (shutdownPacket.Size >= NetConstants.PossibleMtu[0])
                        Logger.Error("[Peer] Disconnect additional data size more than MTU!");
                    else
                        Buffer.BlockCopy(rejectData, start, shutdownPacket.RawData, 9, length);
                    SendRawAndRecycle(shutdownPacket, request.RemoteEndPoint);
                }
            }
            else
            {
                _peersLock.EnterUpgradeableReadLock();
                if (_peersDict.TryGetValue(request.RemoteEndPoint, out netPeer))
                {
                    //already have peer
                    _peersLock.ExitUpgradeableReadLock();
                }
                else if (request.Result == ConnectionRequestResult.Reject)
                {
                    netPeer = new NetPeer(this, request.RemoteEndPoint, GetNextPeerId());
                    netPeer.Reject(request.ConnectionTime, request.ConnectionNumber, rejectData, start, length);
                    AddPeer(netPeer);
                    _peersLock.ExitUpgradeableReadLock();
                    Logger.Debug("[NM] Peer connect reject.");
                }
                else //Accept
                {
                    netPeer = new NetPeer(this, request.RemoteEndPoint, GetNextPeerId(), request.ConnectionTime, request.ConnectionNumber);
                    AddPeer(netPeer);
                    _peersLock.ExitUpgradeableReadLock();
                    CreateEvent(NetEvent.EType.Connect, netPeer);
                    Logger.Debug(string.Format("[NM] Received peer connection Id: {0}, EP: {1}",
                        netPeer.ConnectTime, netPeer.EndPoint));
                }
            }

            lock(_requestsDict)
                _requestsDict.Remove(request.RemoteEndPoint);

            return netPeer;
        }

        private int GetNextPeerId()
        {
            lock (_peerIds)
            {
                var peerId = _peerIds.Count == 0 ? _lastPeerId++ : _peerIds.Dequeue();
                Logger.Warning("new PeerId:" + peerId);
                return peerId;
            }
        }

        /// <summary>
        /// 处理网络连接请求包
        /// </summary>
        /// <param name="remoteEndPoint"></param>
        /// <param name="netPeer"></param>
        /// <param name="connRequest"></param>
        private void ProcessConnectRequest(
            IPEndPoint remoteEndPoint, 
            NetPeer netPeer, 
            NetConnectRequestPacket connRequest)
        {
            byte connectionNumber = connRequest.ConnectionNumber;
            ConnectionRequest req;

            //if we have peer
            if (netPeer != null)
            {
                var processResult = netPeer.ProcessConnectRequest(connRequest);
                Logger.Debug(string.Format("ConnectRequest LastId: {0}, NewId: {1}, EP: {2}, Result: {3}",
                    netPeer.ConnectTime,
                    connRequest.ConnectionTime,
                    remoteEndPoint,
                    processResult));

                switch (processResult)
                {
                    case ConnectRequestResult.Reconnection:
                        DisconnectPeerForce(netPeer, DisconnectReason.Reconnect, 0, null);
                        RemovePeer(netPeer);
                        //go to new connection
                        break;
                    case ConnectRequestResult.NewConnection:
                        RemovePeer(netPeer);
                        //go to new connection
                        break;
                    case ConnectRequestResult.P2PLose:
                        DisconnectPeerForce(netPeer, DisconnectReason.PeerToPeerConnection, 0, null);
                        RemovePeer(netPeer);
                        //go to new connection
                        break;
                    default:
                        //no operations needed
                        return;
                }
                //ConnectRequestResult.NewConnection
                //Set next connection number
                if(processResult != ConnectRequestResult.P2PLose)
                    connectionNumber = (byte)((netPeer.ConnectionNum + 1) % NetConstants.MaxConnectionNumber);
                //To reconnect peer
            }
            else
            {
                Logger.Debug(string.Format("ConnectRequest Id: {0}, EP: {1}",
                    connRequest.ConnectionTime, remoteEndPoint));
            }

            lock (_requestsDict)
            {
                if (_requestsDict.TryGetValue(remoteEndPoint, out req))
                {
                    req.UpdateRequest(connRequest);
                    return;
                }
                req = new ConnectionRequest(
                    connRequest.ConnectionTime,
                    connectionNumber,
                    connRequest.Data,
                    remoteEndPoint,
                    this);
                _requestsDict.Add(remoteEndPoint, req);
            }
            Logger.Debug("[NM] Creating request event: " + connRequest.ConnectionTime);
            CreateEvent(NetEvent.EType.ConnectionRequest, connectionRequest: req);
        }

        /// <summary>
        /// 处理收到的网络二进制数据
        /// </summary>
        /// <param name="reusableBuffer"></param>
        /// <param name="count"></param>
        /// <param name="remoteEndPoint"></param>
        private void DataReceived(byte[] reusableBuffer, int count, IPEndPoint remoteEndPoint)
        {
            if (EnableStatistics)
            {
                Statistics.IncrementPacketsReceived();
                Statistics.AddBytesReceived(count);
            }

            int start = 0;
            if (_extraPacketLayer != null)  //先处理CRC检验等layer
            {
                _extraPacketLayer.ProcessInboundPacket(remoteEndPoint, ref reusableBuffer, ref start, ref count);
                if (count == 0)
                    return;
            }

            //empty packet
            if (reusableBuffer[start] == (byte) PacketProperty.Empty)
                return;

            //Try read packet
            NetPacket packet = NetPacketPool.GetPacket(count);
            if (!packet.FromBytes(reusableBuffer, start, count))
            {
                NetPacketPool.Recycle(packet);
                Logger.Error("[NM] DataReceived: bad!");
                return;
            }

            //1.check special packets
            switch (packet.Property)
            {
                //special case connect request
                case PacketProperty.ConnectRequest:
                    if (NetConnectRequestPacket.GetProtocolId(packet) != NetConstants.ProtocolId)
                    {
                        SendRawAndRecycle(NetPacketPool.GetWithProperty(PacketProperty.InvalidProtocol), remoteEndPoint);
                        return;
                    }
                    break;
                //unconnected messages
                case PacketProperty.Broadcast:
                    if (!BroadcastReceiveEnabled)
                        return;
                    CreateEvent(NetEvent.EType.Broadcast, remoteEndPoint: remoteEndPoint, readerSource: packet);
                    return;
                case PacketProperty.UnconnectedMessage:
                    if (!UnconnectedMessagesEnabled)
                        return;
                    CreateEvent(NetEvent.EType.ReceiveUnconnected, remoteEndPoint: remoteEndPoint, readerSource: packet);
                    return;
                case PacketProperty.NatMessage:
                    if (NatPunchEnabled)
                        NatPunchModule.ProcessMessage(remoteEndPoint, packet);
                    return;
            }

            //2.Check normal packets
            NetPeer netPeer;
            _peersLock.EnterReadLock();
            bool peerFound = _peersDict.TryGetValue(remoteEndPoint, out netPeer);
            _peersLock.ExitReadLock();
            
            switch (packet.Property)
            {
                case PacketProperty.ConnectRequest:
                    var connRequest = NetConnectRequestPacket.FromData(packet);
                    if (connRequest != null)
                        ProcessConnectRequest(remoteEndPoint, netPeer, connRequest);
                    break;
                case PacketProperty.PeerNotFound:
                    if (peerFound)
                    {
                        if (netPeer.ConnectionState != ConnectionState.Connected)
                            return;
                        if (packet.Size == 1) 
                        {
                            //first reply
                            var p = NetPacketPool.GetWithProperty(PacketProperty.PeerNotFound, 9);
                            p.RawData[1] = 0;
                            FastBitConverter.GetBytes(p.RawData, 2, netPeer.ConnectTime);
                            SendRawAndRecycle(p, remoteEndPoint);
                            Logger.Error($"PeerNotFound sending connectTime: {netPeer.ConnectTime}");
                        }
                        else if (packet.Size == 10 && packet.RawData[1] == 1 && BitConverter.ToInt64(packet.RawData, 2) == netPeer.ConnectTime) 
                        {
                            //second reply
                            Logger.Error($"PeerNotFound received our connectTime: {netPeer.ConnectTime}");
                            DisconnectPeerForce(netPeer, DisconnectReason.RemoteConnectionClose, 0, null);
                        }
                    }
                    else if (packet.Size == 10 && packet.RawData[1] == 0)
                    {
                        //send reply back
                        packet.RawData[1] = 1;
                        SendRawAndRecycle(packet, remoteEndPoint);
                    }
                    break;
                case PacketProperty.InvalidProtocol:
                    if (peerFound && netPeer.ConnectionState == ConnectionState.Outgoing)
                        DisconnectPeerForce(netPeer, DisconnectReason.InvalidProtocol, 0, null);
                    break;
                case PacketProperty.Disconnect:
                    if (peerFound)
                    {
                        var disconnectResult = netPeer.ProcessDisconnect(packet);
                        if (disconnectResult == DisconnectResult.None)
                        {
                            NetPacketPool.Recycle(packet);
                            return;
                        }
                        DisconnectPeerForce(
                            netPeer, 
                            disconnectResult == DisconnectResult.Disconnect
                            ? DisconnectReason.RemoteConnectionClose
                            : DisconnectReason.ConnectionRejected,
                            0, packet);
                    }
                    else
                    {
                        NetPacketPool.Recycle(packet);
                    }
                    //Send shutdown
                    SendRawAndRecycle(NetPacketPool.GetWithProperty(PacketProperty.ShutdownOk), remoteEndPoint);
                    break;
                case PacketProperty.ConnectAccept:  //同意连接请求
                    if (!peerFound)
                        return;
                    var connAccept = NetConnectAcceptPacket.FromData(packet);
                    if (connAccept != null && netPeer.ProcessConnectAccept(connAccept))
                        CreateEvent(NetEvent.EType.Connect, netPeer);
                    break;
                default:
                    if(peerFound)
                        netPeer.ProcessPacket(packet);
                    else
                        SendRawAndRecycle(NetPacketPool.GetWithProperty(PacketProperty.PeerNotFound), remoteEndPoint);
                    break;
            }
        }

        /// <summary>
        /// 创建收到网络包事件
        /// </summary>
        /// <param name="packet">收到的网络包</param>
        /// <param name="method"></param>
        /// <param name="headerSize"></param>
        /// <param name="fromPeer">网络包从这个peer收到的</param>
        internal void CreateReceiveEvent(NetPacket packet, DeliveryMethod method, int headerSize, NetPeer fromPeer)
        {
            NetEvent evt;
            do
            {
                evt = _netEventPoolHead;
                if (evt == null)
                {
                    evt = new NetEvent(this);
                    break;
                }
            } while (evt != Interlocked.CompareExchange(ref _netEventPoolHead, evt.Next, evt));
            evt.Type = NetEvent.EType.Receive;
            evt.DataReader.SetSource(packet, headerSize);
            evt.Peer = fromPeer;
            evt.DeliveryMethod = method;
            if (UnsyncedEvents || UnsyncedReceiveEvent)
            {
                ProcessEvent(evt);
            }
            else
            {
                lock (_netEventsQueue)
                    _netEventsQueue.Enqueue(evt);
            }
        }

        #endregion

        #region Get Peer Method
        
        private bool TryGetPeer(IPEndPoint endPoint, out NetPeer peer)
        {
            _peersLock.EnterReadLock();
            bool result = _peersDict.TryGetValue(endPoint, out peer);
            _peersLock.ExitReadLock();
            return result;
        }

        /// <summary>
        /// Return peers count with connection state
        /// </summary>
        /// <param name="peerState">peer connection state (you can use as bit flags)</param>
        /// <returns>peers count</returns>
        public int GetPeersCount(ConnectionState peerState)
        {
            int count = 0;
            _peersLock.EnterReadLock();
            for (var netPeer = _headPeer; netPeer != null; netPeer = netPeer.NextPeer)
            {
                if ((netPeer.ConnectionState & peerState) != 0)
                    count++;
            }
            _peersLock.ExitReadLock();
            return count;
        }

        /// <summary>
        /// Get copy of peers (without allocations)
        /// </summary>
        /// <param name="peers">List that will contain result</param>
        /// <param name="peerState">State of peers</param>
        public void GetPeersNonAlloc(List<NetPeer> peers, ConnectionState peerState)
        {
            peers.Clear();
            _peersLock.EnterReadLock();
            for (var netPeer = _headPeer; netPeer != null; netPeer = netPeer.NextPeer)
            {
                if ((netPeer.ConnectionState & peerState) != 0)
                    peers.Add(netPeer);
            }
            _peersLock.ExitReadLock();
        }
        
        #endregion

        #region Connet Method
        
        /// <summary>
        /// Connect to remote host
        /// </summary>
        /// <param name="address">Server IP or hostname</param>
        /// <param name="port">Server Port</param>
        /// <param name="key">Connection key</param>
        /// <returns>New NetPeer if new connection, Old NetPeer if already connected, null peer if there is ConnectionRequest awaiting</returns>
        /// <exception cref="InvalidOperationException">Manager is not running. Call <see cref="Start()"/></exception>
        public NetPeer Connect(string address, int port, string key)
        {
            return Connect(address, port, NetDataWriter.FromString(key));
        }

        /// <summary>
        /// Connect to remote host
        /// </summary>
        /// <param name="address">Server IP or hostname</param>
        /// <param name="port">Server Port</param>
        /// <param name="connectionData">Additional data for remote peer</param>
        /// <returns>New NetPeer if new connection, Old NetPeer if already connected, null peer if there is ConnectionRequest awaiting</returns>
        /// <exception cref="InvalidOperationException">Manager is not running. Call <see cref="Start()"/></exception>
        public NetPeer Connect(string address, int port, NetDataWriter connectionData)
        {
            IPEndPoint ep;
            try
            {
                ep = NetUtils.MakeEndPoint(address, port);
            }
            catch
            {
                CreateEvent(NetEvent.EType.Disconnect, disconnectReason: DisconnectReason.UnknownHost);
                return null;
            }
            return Connect(ep, connectionData);
        }

        /// <summary>
        /// Connect to remote host
        /// </summary>
        /// <param name="target">Server end point (ip and port)</param>
        /// <param name="key">Connection key</param>
        /// <returns>New NetPeer if new connection, Old NetPeer if already connected, null peer if there is ConnectionRequest awaiting</returns>
        /// <exception cref="InvalidOperationException">Manager is not running. Call <see cref="Start()"/></exception>
        public NetPeer Connect(IPEndPoint target, string key)
        {
            return Connect(target, NetDataWriter.FromString(key));
        }

        /// <summary>
        /// Connect to remote host
        /// </summary>
        /// <param name="target">Server end point (ip and port)</param>
        /// <param name="connectionData">Additional data for remote peer</param>
        /// <returns>New NetPeer if new connection, Old NetPeer if already connected, null peer if there is ConnectionRequest awaiting</returns>
        /// <exception cref="InvalidOperationException">Manager is not running. Call <see cref="Start()"/></exception>
        public NetPeer Connect(IPEndPoint target, NetDataWriter connectionData)
        {
            if (!_socket.IsRunning)
                throw new InvalidOperationException("Client is not running");

            NetPeer peer;
            byte connectionNumber = 0;

            lock(_requestsDict)
            {
                if (_requestsDict.ContainsKey(target))
                    return null;
            }

            _peersLock.EnterUpgradeableReadLock();
            if (_peersDict.TryGetValue(target, out peer))
            {
                switch (peer.ConnectionState)
                {
                    //just return already connected peer
                    case ConnectionState.Connected:
                    case ConnectionState.Outgoing:
                        _peersLock.ExitUpgradeableReadLock();
                        return peer;
                }
                //else reconnect
                connectionNumber = (byte)((peer.ConnectionNum + 1) % NetConstants.MaxConnectionNumber);
                RemovePeer(peer);
            }

            //Create reliable connection
            //And send connection request
            peer = new NetPeer(this, target, GetNextPeerId(), connectionNumber, connectionData);
            AddPeer(peer);
            _peersLock.ExitUpgradeableReadLock();

            return peer;
        }
        
        #endregion
        
        #region Disconnect Method

        
        /// <summary>
        /// Disconnect all peers without any additional data
        /// </summary>
        public void DisconnectAll()
        {
            DisconnectAll(null, 0, 0);
        }

        /// <summary>
        /// Disconnect all peers with shutdown message
        /// </summary>
        /// <param name="data">Data to send (must be less or equal MTU)</param>
        /// <param name="start">Data start</param>
        /// <param name="count">Data count</param>
        public void DisconnectAll(byte[] data, int start, int count)
        {
            //Send disconnect packets
            _peersLock.EnterReadLock();
            for (var netPeer = _headPeer; netPeer != null; netPeer = netPeer.NextPeer)
            {
                DisconnectPeer(
                    netPeer, 
                    DisconnectReason.DisconnectPeerCalled, 
                    0, 
                    false,
                    data, 
                    start, 
                    count,
                    null);
            }
            _peersLock.ExitReadLock();
        }

        /// <summary>
        /// Immediately disconnect peer from server without additional data
        /// </summary>
        /// <param name="peer">peer to disconnect</param>
        public void DisconnectPeerForce(NetPeer peer)
        {
            DisconnectPeerForce(peer, DisconnectReason.DisconnectPeerCalled, 0, null);
        }

        /// <summary>
        /// Disconnect peer from server
        /// </summary>
        /// <param name="peer">peer to disconnect</param>
        public void DisconnectPeer(NetPeer peer)
        {
            DisconnectPeer(peer, null, 0, 0);
        }

        /// <summary>
        /// Disconnect peer from server and send additional data (Size must be less or equal MTU - 8)
        /// </summary>
        /// <param name="peer">peer to disconnect</param>
        /// <param name="data">additional data</param>
        public void DisconnectPeer(NetPeer peer, byte[] data)
        {
            DisconnectPeer(peer, data, 0, data.Length);
        }

        /// <summary>
        /// Disconnect peer from server and send additional data (Size must be less or equal MTU - 8)
        /// </summary>
        /// <param name="peer">peer to disconnect</param>
        /// <param name="writer">additional data</param>
        public void DisconnectPeer(NetPeer peer, NetDataWriter writer)
        {
            DisconnectPeer(peer, writer.Data, 0, writer.Length);
        }

        /// <summary>
        /// Disconnect peer from server and send additional data (Size must be less or equal MTU - 8)
        /// </summary>
        /// <param name="peer">peer to disconnect</param>
        /// <param name="data">additional data</param>
        /// <param name="start">data start</param>
        /// <param name="count">data length</param>
        public void DisconnectPeer(NetPeer peer, byte[] data, int start, int count)
        {
            DisconnectPeer(
                peer, 
                DisconnectReason.DisconnectPeerCalled, 
                0, 
                false,
                data, 
                start, 
                count,
                null);
        }

         /// <summary>
        /// 强制断开连接
        /// </summary>
        /// <param name="peer"></param>
        /// <param name="reason"></param>
        /// <param name="socketErrorCode"></param>
        /// <param name="eventData"></param>
        internal void DisconnectPeerForce(NetPeer peer,
            DisconnectReason reason,
            SocketError socketErrorCode,
            NetPacket eventData)
        {
            DisconnectPeer(peer, reason, socketErrorCode, true, null, 0, 0, eventData);
        }

        /// <summary>
        /// 强制断开连接
        /// </summary>
        /// <param name="peer"></param>
        /// <param name="reason"></param>
        /// <param name="socketErrorCode"></param>
        /// <param name="force"></param>
        /// <param name="data"></param>
        /// <param name="start"></param>
        /// <param name="count"></param>
        /// <param name="eventData"></param>
        private void DisconnectPeer(
            NetPeer peer, 
            DisconnectReason reason,
            SocketError socketErrorCode, 
            bool force,
            byte[] data,
            int start,
            int count,
            NetPacket eventData)
        {
            var shutdownResult = peer.Shutdown(data, start, count, force);
            if (shutdownResult == ShutdownResult.None)
                return;
            if(shutdownResult == ShutdownResult.WasConnected)
                Interlocked.Decrement(ref _connectedPeersCount);
            
            
            //内存屏障
            //为什么要在这里设置内存屏障？
            //因为现代CPU为了提高性能而采取乱序执行，而内存屏障可以阻止指令重排，也就是说内存屏障之前的指令和之后的指令不会由于指令优化等原因而导致乱序。
            //这样就可以保证内存屏障之前的写入操作都已写入内存，内存屏障之后的读取操作读取到的都是之前写入的结果。因此，对于敏感的程序块，写操作之后，读操作之前
            //可以插入内存屏障，保证读取的数据就是写入的数据
            //参考：https://www.cnblogs.com/cdaniu/p/15733422.html
            //因为CreateEvent()需要读取_connectedPeersCount的值，所以需要在写入之后，读取之前插入内存屏障
            Thread.MemoryBarrier();
            
            
            CreateEvent(
                NetEvent.EType.Disconnect,
                peer,
                errorCode: socketErrorCode,
                disconnectReason: reason,
                readerSource: eventData);
        }

        #endregion

        #region 迭代器
        
        public NetPeerEnumerator GetEnumerator()
        {
            return new NetPeerEnumerator(_headPeer);
        }

        IEnumerator<NetPeer> IEnumerable<NetPeer>.GetEnumerator()
        {
            return new NetPeerEnumerator(_headPeer);
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return new NetPeerEnumerator(_headPeer);
        }
        
         #endregion
    }
}