// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_brshoplotteryconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_brshoplotteryconfig.proto</summary>
  public static partial class XlsBeansBrshoplotteryconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_brshoplotteryconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansBrshoplotteryconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiN4bHNfYmVhbnNfYnJzaG9wbG90dGVyeWNvbmZpZy5wcm90bxIKRDExLlBi",
            "ZWFucyJIChNCUlNob3BMb3R0ZXJ5Q29uZmlnEhMKC2l0ZW1Hcm91cElkGAEg",
            "ASgNEg4KBml0ZW1JZBgCIAEoDRIMCgRyYXRlGAMgAygNIksKGUJSU2hvcExv",
            "dHRlcnlDb25maWdfQXJyYXkSLgoFaXRlbXMYASADKAsyHy5EMTEuUGJlYW5z",
            "LkJSU2hvcExvdHRlcnlDb25maWdiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BRShopLotteryConfig), global::D11.Pbeans.BRShopLotteryConfig.Parser, new[]{ "ItemGroupId", "ItemId", "Rate" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BRShopLotteryConfig_Array), global::D11.Pbeans.BRShopLotteryConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class BRShopLotteryConfig : pb::IMessage<BRShopLotteryConfig> {
    private static readonly pb::MessageParser<BRShopLotteryConfig> _parser = new pb::MessageParser<BRShopLotteryConfig>(() => new BRShopLotteryConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BRShopLotteryConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBrshoplotteryconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRShopLotteryConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRShopLotteryConfig(BRShopLotteryConfig other) : this() {
      itemGroupId_ = other.itemGroupId_;
      itemId_ = other.itemId_;
      rate_ = other.rate_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRShopLotteryConfig Clone() {
      return new BRShopLotteryConfig(this);
    }

    /// <summary>Field number for the "itemGroupId" field.</summary>
    public const int ItemGroupIdFieldNumber = 1;
    private uint itemGroupId_;
    /// <summary>
    /// 商店道具组ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint ItemGroupId {
      get { return itemGroupId_; }
      set {
        itemGroupId_ = value;
      }
    }

    /// <summary>Field number for the "itemId" field.</summary>
    public const int ItemIdFieldNumber = 2;
    private uint itemId_;
    /// <summary>
    /// 道具ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint ItemId {
      get { return itemId_; }
      set {
        itemId_ = value;
      }
    }

    /// <summary>Field number for the "rate" field.</summary>
    public const int RateFieldNumber = 3;
    private static readonly pb::FieldCodec<uint> _repeated_rate_codec
        = pb::FieldCodec.ForUInt32(26);
    private readonly pbc::RepeatedField<uint> rate_ = new pbc::RepeatedField<uint>();
    /// <summary>
    /// 阶段1权重 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<uint> Rate {
      get { return rate_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BRShopLotteryConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BRShopLotteryConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (ItemGroupId != other.ItemGroupId) return false;
      if (ItemId != other.ItemId) return false;
      if(!rate_.Equals(other.rate_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (ItemGroupId != 0) hash ^= ItemGroupId.GetHashCode();
      if (ItemId != 0) hash ^= ItemId.GetHashCode();
      hash ^= rate_.GetHashCode();
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
      if (ItemGroupId != 0) {
        output.WriteRawTag(8);
        output.WriteUInt32(ItemGroupId);
      }
      if (ItemId != 0) {
        output.WriteRawTag(16);
        output.WriteUInt32(ItemId);
      }
      rate_.WriteTo(output, _repeated_rate_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (ItemGroupId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(ItemGroupId);
      }
      if (ItemId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(ItemId);
      }
      size += rate_.CalculateSize(_repeated_rate_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(BRShopLotteryConfig other) {
      if (other == null) {
        return;
      }
      if (other.ItemGroupId != 0) {
        ItemGroupId = other.ItemGroupId;
      }
      if (other.ItemId != 0) {
        ItemId = other.ItemId;
      }
      rate_.Add(other.rate_);
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
            ItemGroupId = input.ReadUInt32();
            break;
          }
          case 16: {
            ItemId = input.ReadUInt32();
            break;
          }
          case 26:
          case 24: {
            rate_.AddEntriesFrom(input, _repeated_rate_codec);
            break;
          }
        }
      }
    }

  }

  public sealed partial class BRShopLotteryConfig_Array : pb::IMessage<BRShopLotteryConfig_Array> {
    private static readonly pb::MessageParser<BRShopLotteryConfig_Array> _parser = new pb::MessageParser<BRShopLotteryConfig_Array>(() => new BRShopLotteryConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BRShopLotteryConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBrshoplotteryconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRShopLotteryConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRShopLotteryConfig_Array(BRShopLotteryConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BRShopLotteryConfig_Array Clone() {
      return new BRShopLotteryConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.BRShopLotteryConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.BRShopLotteryConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.BRShopLotteryConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.BRShopLotteryConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.BRShopLotteryConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BRShopLotteryConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BRShopLotteryConfig_Array other) {
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
    public void MergeFrom(BRShopLotteryConfig_Array other) {
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