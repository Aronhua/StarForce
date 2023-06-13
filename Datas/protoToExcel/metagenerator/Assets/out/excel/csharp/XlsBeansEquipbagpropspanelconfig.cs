// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_equipbagpropspanelconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_equipbagpropspanelconfig.proto</summary>
  public static partial class XlsBeansEquipbagpropspanelconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_equipbagpropspanelconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansEquipbagpropspanelconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Cih4bHNfYmVhbnNfZXF1aXBiYWdwcm9wc3BhbmVsY29uZmlnLnByb3RvEgpE",
            "MTEuUGJlYW5zIlYKGEVxdWlwQmFnUHJvcHNQYW5lbENvbmZpZxIKCgJpZBgB",
            "IAEoDRIOCgZzbG90SUQYAiABKA0SDgoGaXNMb2NrGAMgASgNEg4KBmljb25J",
            "RBgEIAEoDSJVCh5FcXVpcEJhZ1Byb3BzUGFuZWxDb25maWdfQXJyYXkSMwoF",
            "aXRlbXMYASADKAsyJC5EMTEuUGJlYW5zLkVxdWlwQmFnUHJvcHNQYW5lbENv",
            "bmZpZ2IGcHJvdG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.EquipBagPropsPanelConfig), global::D11.Pbeans.EquipBagPropsPanelConfig.Parser, new[]{ "Id", "SlotID", "IsLock", "IconID" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.EquipBagPropsPanelConfig_Array), global::D11.Pbeans.EquipBagPropsPanelConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class EquipBagPropsPanelConfig : pb::IMessage<EquipBagPropsPanelConfig> {
    private static readonly pb::MessageParser<EquipBagPropsPanelConfig> _parser = new pb::MessageParser<EquipBagPropsPanelConfig>(() => new EquipBagPropsPanelConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<EquipBagPropsPanelConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansEquipbagpropspanelconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBagPropsPanelConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBagPropsPanelConfig(EquipBagPropsPanelConfig other) : this() {
      id_ = other.id_;
      slotID_ = other.slotID_;
      isLock_ = other.isLock_;
      iconID_ = other.iconID_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBagPropsPanelConfig Clone() {
      return new EquipBagPropsPanelConfig(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private uint id_;
    /// <summary>
    /// 编号 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "slotID" field.</summary>
    public const int SlotIDFieldNumber = 2;
    private uint slotID_;
    /// <summary>
    /// 槽位ID（与EquipBagSlotConfig中ID对应） 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint SlotID {
      get { return slotID_; }
      set {
        slotID_ = value;
      }
    }

    /// <summary>Field number for the "isLock" field.</summary>
    public const int IsLockFieldNumber = 3;
    private uint isLock_;
    /// <summary>
    /// 是否锁定 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint IsLock {
      get { return isLock_; }
      set {
        isLock_ = value;
      }
    }

    /// <summary>Field number for the "iconID" field.</summary>
    public const int IconIDFieldNumber = 4;
    private uint iconID_;
    /// <summary>
    /// 锁定时显示的图标ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint IconID {
      get { return iconID_; }
      set {
        iconID_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as EquipBagPropsPanelConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(EquipBagPropsPanelConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (SlotID != other.SlotID) return false;
      if (IsLock != other.IsLock) return false;
      if (IconID != other.IconID) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (SlotID != 0) hash ^= SlotID.GetHashCode();
      if (IsLock != 0) hash ^= IsLock.GetHashCode();
      if (IconID != 0) hash ^= IconID.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (Id != 0) {
        output.WriteRawTag(8);
        output.WriteUInt32(Id);
      }
      if (SlotID != 0) {
        output.WriteRawTag(16);
        output.WriteUInt32(SlotID);
      }
      if (IsLock != 0) {
        output.WriteRawTag(24);
        output.WriteUInt32(IsLock);
      }
      if (IconID != 0) {
        output.WriteRawTag(32);
        output.WriteUInt32(IconID);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Id != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Id);
      }
      if (SlotID != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(SlotID);
      }
      if (IsLock != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(IsLock);
      }
      if (IconID != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(IconID);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(EquipBagPropsPanelConfig other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.SlotID != 0) {
        SlotID = other.SlotID;
      }
      if (other.IsLock != 0) {
        IsLock = other.IsLock;
      }
      if (other.IconID != 0) {
        IconID = other.IconID;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 8: {
            Id = input.ReadUInt32();
            break;
          }
          case 16: {
            SlotID = input.ReadUInt32();
            break;
          }
          case 24: {
            IsLock = input.ReadUInt32();
            break;
          }
          case 32: {
            IconID = input.ReadUInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class EquipBagPropsPanelConfig_Array : pb::IMessage<EquipBagPropsPanelConfig_Array> {
    private static readonly pb::MessageParser<EquipBagPropsPanelConfig_Array> _parser = new pb::MessageParser<EquipBagPropsPanelConfig_Array>(() => new EquipBagPropsPanelConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<EquipBagPropsPanelConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansEquipbagpropspanelconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBagPropsPanelConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBagPropsPanelConfig_Array(EquipBagPropsPanelConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBagPropsPanelConfig_Array Clone() {
      return new EquipBagPropsPanelConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.EquipBagPropsPanelConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.EquipBagPropsPanelConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.EquipBagPropsPanelConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.EquipBagPropsPanelConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.EquipBagPropsPanelConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as EquipBagPropsPanelConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(EquipBagPropsPanelConfig_Array other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if(!items_.Equals(other.items_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      hash ^= items_.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      items_.WriteTo(output, _repeated_items_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      size += items_.CalculateSize(_repeated_items_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(EquipBagPropsPanelConfig_Array other) {
      if (other == null) {
        return;
      }
      items_.Add(other.items_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            items_.AddEntriesFrom(input, _repeated_items_codec);
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code