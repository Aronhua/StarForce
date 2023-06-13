// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_britemslotconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_britemslotconfig.proto</summary>
  public static partial class XlsBeansBritemslotconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_britemslotconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansBritemslotconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiB4bHNfYmVhbnNfYnJpdGVtc2xvdGNvbmZpZy5wcm90bxIKRDExLlBiZWFu",
            "cyKiAQoQQlJJdGVtU2xvdENvbmZpZxIKCgJpZBgBIAEoDRIQCghtYXhMaW1p",
            "dBgCIAEoDRISCgpjYW5SZXBsYWNlGAMgASgIEhYKDmNhblJlcGxhY2VEcm9w",
            "GAQgASgIEg8KB2NhbkRyb3AYBSABKAgSFgoOc2xvdFRhY3RpY2FsSWQYBiAB",
            "KA0SGwoTZW1wdHlTbG90VGFjdGljYWxJZBgHIAEoDSJFChZCUkl0ZW1TbG90",
            "Q29uZmlnX0FycmF5EisKBWl0ZW1zGAEgAygLMhwuRDExLlBiZWFucy5CUkl0",
            "ZW1TbG90Q29uZmlnYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BRItemSlotConfig), global::D11.Pbeans.BRItemSlotConfig.Parser, new[]{ "Id", "MaxLimit", "CanReplace", "CanReplaceDrop", "CanDrop", "SlotTacticalId", "EmptySlotTacticalId" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BRItemSlotConfig_Array), global::D11.Pbeans.BRItemSlotConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class BRItemSlotConfig : pb::IMessage<BRItemSlotConfig> {
    private static readonly pb::MessageParser<BRItemSlotConfig> _parser = new pb::MessageParser<BRItemSlotConfig>(() => new BRItemSlotConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BRItemSlotConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBritemslotconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRItemSlotConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRItemSlotConfig(BRItemSlotConfig other) : this() {
      id_ = other.id_;
      maxLimit_ = other.maxLimit_;
      canReplace_ = other.canReplace_;
      canReplaceDrop_ = other.canReplaceDrop_;
      canDrop_ = other.canDrop_;
      slotTacticalId_ = other.slotTacticalId_;
      emptySlotTacticalId_ = other.emptySlotTacticalId_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRItemSlotConfig Clone() {
      return new BRItemSlotConfig(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private uint id_;
    /// <summary>
    /// 槽位ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "maxLimit" field.</summary>
    public const int MaxLimitFieldNumber = 2;
    private uint maxLimit_;
    /// <summary>
    /// 携带上限数 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint MaxLimit {
      get { return maxLimit_; }
      set {
        maxLimit_ = value;
      }
    }

    /// <summary>Field number for the "canReplace" field.</summary>
    public const int CanReplaceFieldNumber = 3;
    private bool canReplace_;
    /// <summary>
    /// 是否可替换 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool CanReplace {
      get { return canReplace_; }
      set {
        canReplace_ = value;
      }
    }

    /// <summary>Field number for the "canReplaceDrop" field.</summary>
    public const int CanReplaceDropFieldNumber = 4;
    private bool canReplaceDrop_;
    /// <summary>
    /// 替换时是否掉落 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool CanReplaceDrop {
      get { return canReplaceDrop_; }
      set {
        canReplaceDrop_ = value;
      }
    }

    /// <summary>Field number for the "canDrop" field.</summary>
    public const int CanDropFieldNumber = 5;
    private bool canDrop_;
    /// <summary>
    /// 是否可丢弃 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool CanDrop {
      get { return canDrop_; }
      set {
        canDrop_ = value;
      }
    }

    /// <summary>Field number for the "slotTacticalId" field.</summary>
    public const int SlotTacticalIdFieldNumber = 6;
    private uint slotTacticalId_;
    /// <summary>
    /// 长按非空槽位战术提示 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint SlotTacticalId {
      get { return slotTacticalId_; }
      set {
        slotTacticalId_ = value;
      }
    }

    /// <summary>Field number for the "emptySlotTacticalId" field.</summary>
    public const int EmptySlotTacticalIdFieldNumber = 7;
    private uint emptySlotTacticalId_;
    /// <summary>
    /// 长按空槽位战术提示 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint EmptySlotTacticalId {
      get { return emptySlotTacticalId_; }
      set {
        emptySlotTacticalId_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BRItemSlotConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BRItemSlotConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (MaxLimit != other.MaxLimit) return false;
      if (CanReplace != other.CanReplace) return false;
      if (CanReplaceDrop != other.CanReplaceDrop) return false;
      if (CanDrop != other.CanDrop) return false;
      if (SlotTacticalId != other.SlotTacticalId) return false;
      if (EmptySlotTacticalId != other.EmptySlotTacticalId) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (MaxLimit != 0) hash ^= MaxLimit.GetHashCode();
      if (CanReplace != false) hash ^= CanReplace.GetHashCode();
      if (CanReplaceDrop != false) hash ^= CanReplaceDrop.GetHashCode();
      if (CanDrop != false) hash ^= CanDrop.GetHashCode();
      if (SlotTacticalId != 0) hash ^= SlotTacticalId.GetHashCode();
      if (EmptySlotTacticalId != 0) hash ^= EmptySlotTacticalId.GetHashCode();
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
      if (MaxLimit != 0) {
        output.WriteRawTag(16);
        output.WriteUInt32(MaxLimit);
      }
      if (CanReplace != false) {
        output.WriteRawTag(24);
        output.WriteBool(CanReplace);
      }
      if (CanReplaceDrop != false) {
        output.WriteRawTag(32);
        output.WriteBool(CanReplaceDrop);
      }
      if (CanDrop != false) {
        output.WriteRawTag(40);
        output.WriteBool(CanDrop);
      }
      if (SlotTacticalId != 0) {
        output.WriteRawTag(48);
        output.WriteUInt32(SlotTacticalId);
      }
      if (EmptySlotTacticalId != 0) {
        output.WriteRawTag(56);
        output.WriteUInt32(EmptySlotTacticalId);
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
      if (MaxLimit != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(MaxLimit);
      }
      if (CanReplace != false) {
        size += 1 + 1;
      }
      if (CanReplaceDrop != false) {
        size += 1 + 1;
      }
      if (CanDrop != false) {
        size += 1 + 1;
      }
      if (SlotTacticalId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(SlotTacticalId);
      }
      if (EmptySlotTacticalId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(EmptySlotTacticalId);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(BRItemSlotConfig other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.MaxLimit != 0) {
        MaxLimit = other.MaxLimit;
      }
      if (other.CanReplace != false) {
        CanReplace = other.CanReplace;
      }
      if (other.CanReplaceDrop != false) {
        CanReplaceDrop = other.CanReplaceDrop;
      }
      if (other.CanDrop != false) {
        CanDrop = other.CanDrop;
      }
      if (other.SlotTacticalId != 0) {
        SlotTacticalId = other.SlotTacticalId;
      }
      if (other.EmptySlotTacticalId != 0) {
        EmptySlotTacticalId = other.EmptySlotTacticalId;
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
            MaxLimit = input.ReadUInt32();
            break;
          }
          case 24: {
            CanReplace = input.ReadBool();
            break;
          }
          case 32: {
            CanReplaceDrop = input.ReadBool();
            break;
          }
          case 40: {
            CanDrop = input.ReadBool();
            break;
          }
          case 48: {
            SlotTacticalId = input.ReadUInt32();
            break;
          }
          case 56: {
            EmptySlotTacticalId = input.ReadUInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class BRItemSlotConfig_Array : pb::IMessage<BRItemSlotConfig_Array> {
    private static readonly pb::MessageParser<BRItemSlotConfig_Array> _parser = new pb::MessageParser<BRItemSlotConfig_Array>(() => new BRItemSlotConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BRItemSlotConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBritemslotconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRItemSlotConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRItemSlotConfig_Array(BRItemSlotConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRItemSlotConfig_Array Clone() {
      return new BRItemSlotConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.BRItemSlotConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.BRItemSlotConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.BRItemSlotConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.BRItemSlotConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.BRItemSlotConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BRItemSlotConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BRItemSlotConfig_Array other) {
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
    public void MergeFrom(BRItemSlotConfig_Array other) {
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