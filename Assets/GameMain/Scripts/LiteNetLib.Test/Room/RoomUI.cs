/*
  作者：LTH
  文件描述：
  文件名：RoomUI
  创建时间：2023/08/06 10:08:SS
*/

using System;
using GameMain;
using Protos;
using UnityEngine;
using UnityEngine.UI;

public class RoomUI:MonoBehaviour
{
    public GameObject BeforeGo, AfterGo;

    public Button OpenRoomBtn, JoinRoomBtn;
    public Button StartBattleBtn, ShowAllRoomBtn;
   
    public InputField JoinRoomIdText;
    public Text AllRoomIdText,RoomPlayerIdText;


    //当前加入的房间ID
    public int m_CurJoinRoomId;
    private void Start()
    {
        OpenRoomBtn.onClick.AddListener(OnOpenRoom);
        JoinRoomBtn.onClick.AddListener(OnJoinRoom);
        
        StartBattleBtn.onClick.AddListener(OnStartBattle);
        ShowAllRoomBtn.onClick.AddListener(OnShowAllRoom);
        
        OutsideNetManager.Register<OpenRoomRes>(OnOpenRoomRes);
        OutsideNetManager.Register<JoinRoomRes>(OnJoinRoomRes);
    }

    private void OnOpenRoom()
    {
        //发送开房间请求
        OpenRoomReq openRoomReq = new OpenRoomReq();
        openRoomReq.PlayerId = PlayerInfoManager.Instance.PlayerInfo.PlayerId;
        OutsideNetManager.SendPacket(openRoomReq);
    }

    private void OnJoinRoom()
    {
        //加入房间请求
        JoinRoomReq joinRoomReq = new JoinRoomReq();
        joinRoomReq.PlayerId = PlayerInfoManager.Instance.PlayerInfo.PlayerId;
        joinRoomReq.RoomId = Convert.ToInt32(JoinRoomIdText.text);
        OutsideNetManager.SendPacket(joinRoomReq);
    }

    private void OnStartBattle()
    {
        
    }
    
    private void OnShowAllRoom()
    {
        BeforeGo.SetActive(true);
        AfterGo.SetActive(false);
    }
    
    //
    private void OnOpenRoomRes(OpenRoomRes openRoomRes)
    {
        Debug.Log("开房间请求回包：" + openRoomRes.Result + " RoomId:" + openRoomRes.RoomId);
        if (openRoomRes.Result)
        {
            //房主自动设置房间id
            JoinRoomIdText.text = openRoomRes.RoomId.ToString();
        }
    }

    private void OnJoinRoomRes(JoinRoomRes joinRoomRes)
    {
        Debug.Log("加入房间请求回包：" + joinRoomRes.Result + " RoomId:" + joinRoomRes.RoomId);
        if (joinRoomRes.Result)  //加入房间成功，只显示当前房间信息
        {
            BeforeGo.SetActive(false);
            AfterGo.SetActive(true);
            m_CurJoinRoomId = joinRoomRes.RoomId;
        }
    }
}