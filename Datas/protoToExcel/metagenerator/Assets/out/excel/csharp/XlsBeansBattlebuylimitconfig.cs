// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_battlebuylimitconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_battlebuylimitconfig.proto</summary>
  public static partial class XlsBeansBattlebuylimitconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_battlebuylimitconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansBattlebuylimitconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiR4bHNfYmVhbnNfYmF0dGxlYnV5bGltaXRjb25maWcucHJvdG8SCkQxMS5Q",
            "YmVhbnMinQIKFEJhdHRsZUJ1eUxpbWl0Q29uZmlnEgoKAmlkGAEgASgNEhEK",
            "CW1heE93bk51bRgCIAEoBRIRCgltYXhCdXlOdW0YAyABKAUSQwoMU3ViVHlw",
            "ZUxpbWl0GAQgAygLMi0uRDExLlBiZWFucy5CYXR0bGVCdXlMaW1pdENvbmZp",
            "Z19TdWJUeXBlTGltaXQSSwoQU2hhcmVLaW5kSWRMaW1pdBgFIAMoCzIxLkQx",
            "MS5QYmVhbnMuQmF0dGxlQnV5TGltaXRDb25maWdfU2hhcmVLaW5kSWRMaW1p",
            "dBJBCgtLaW5kSWRMaW1pdBgGIAMoCzIsLkQxMS5QYmVhbnMuQmF0dGxlQnV5",
            "TGltaXRDb25maWdfS2luZElkTGltaXQiWgohQmF0dGxlQnV5TGltaXRDb25m",
            "aWdfU3ViVHlwZUxpbWl0Eg8KB3N1YlR5cGUYASABKA0SEQoJbWF4T3duTnVt",
            "GAIgASgFEhEKCW1heEJ1eU51bRgDIAEoBSJKCiVCYXR0bGVCdXlMaW1pdENv",
            "bmZpZ19TaGFyZUtpbmRJZExpbWl0Eg4KBmtpbmRJZBgBIAEoCRIRCgltYXhP",
            "d25OdW0YAiABKAUiWAogQmF0dGxlQnV5TGltaXRDb25maWdfS2luZElkTGlt",
            "aXQSDgoGa2luZElkGAEgASgNEhEKCW1heE93bk51bRgCIAEoBRIRCgltYXhC",
            "dXlOdW0YAyABKAUiTQoaQmF0dGxlQnV5TGltaXRDb25maWdfQXJyYXkSLwoF",
            "aXRlbXMYASADKAsyIC5EMTEuUGJlYW5zLkJhdHRsZUJ1eUxpbWl0Q29uZmln",
            "YgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BattleBuyLimitConfig), global::D11.Pbeans.BattleBuyLimitConfig.Parser, new[]{ "Id", "MaxOwnNum", "MaxBuyNum", "SubTypeLimit", "ShareKindIdLimit", "KindIdLimit" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BattleBuyLimitConfig_SubTypeLimit), global::D11.Pbeans.BattleBuyLimitConfig_SubTypeLimit.Parser, new[]{ "SubType", "MaxOwnNum", "MaxBuyNum" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BattleBuyLimitConfig_ShareKindIdLimit), global::D11.Pbeans.BattleBuyLimitConfig_ShareKindIdLimit.Parser, new[]{ "KindId", "MaxOwnNum" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BattleBuyLimitConfig_KindIdLimit), global::D11.Pbeans.BattleBuyLimitConfig_KindIdLimit.Parser, new[]{ "KindId", "MaxOwnNum", "MaxBuyNum" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.BattleBuyLimitConfig_Array), global::D11.Pbeans.BattleBuyLimitConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class BattleBuyLimitConfig : pb::IMessage<BattleBuyLimitConfig> {
    private static readonly pb::MessageParser<BattleBuyLimitConfig> _parser = new pb::MessageParser<BattleBuyLimitConfig>(() => new BattleBuyLimitConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BattleBuyLimitConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBattlebuylimitconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig(BattleBuyLimitConfig other) : this() {
      id_ = other.id_;
      maxOwnNum_ = other.maxOwnNum_;
      maxBuyNum_ = other.maxBuyNum_;
      subTypeLimit_ = other.subTypeLimit_.Clone();
      shareKindIdLimit_ = other.shareKindIdLimit_.Clone();
      kindIdLimit_ = other.kindIdLimit_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig Clone() {
      return new BattleBuyLimitConfig(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private uint id_;
    /// <summary>
    /// 模式ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "maxOwnNum" field.</summary>
    public const int MaxOwnNumFieldNumber = 2;
    private int maxOwnNum_;
    /// <summary>
    /// 默认最大持有数:武器类型 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int MaxOwnNum {
      get { return maxOwnNum_; }
      set {
        maxOwnNum_ = value;
      }
    }

    /// <summary>Field number for the "maxBuyNum" field.</summary>
    public const int MaxBuyNumFieldNumber = 3;
    private int maxBuyNum_;
    /// <summary>
    /// 默认购买次数:武器类型 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int MaxBuyNum {
      get { return maxBuyNum_; }
      set {
        maxBuyNum_ = value;
      }
    }

    /// <summary>Field number for the "SubTypeLimit" field.</summary>
    public const int SubTypeLimitFieldNumber = 4;
    private static readonly pb::FieldCodec<global::D11.Pbeans.BattleBuyLimitConfig_SubTypeLimit> _repeated_subTypeLimit_codec
        = pb::FieldCodec.ForMessage(34, global::D11.Pbeans.BattleBuyLimitConfig_SubTypeLimit.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_SubTypeLimit> subTypeLimit_ = new pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_SubTypeLimit>();
    /// <summary>
    /// 武器主类型:subType1 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_SubTypeLimit> SubTypeLimit {
      get { return subTypeLimit_; }
    }

    /// <summary>Field number for the "ShareKindIdLimit" field.</summary>
    public const int ShareKindIdLimitFieldNumber = 5;
    private static readonly pb::FieldCodec<global::D11.Pbeans.BattleBuyLimitConfig_ShareKindIdLimit> _repeated_shareKindIdLimit_codec
        = pb::FieldCodec.ForMessage(42, global::D11.Pbeans.BattleBuyLimitConfig_ShareKindIdLimit.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_ShareKindIdLimit> shareKindIdLimit_ = new pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_ShareKindIdLimit>();
    /// <summary>
    /// 武器类型1 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_ShareKindIdLimit> ShareKindIdLimit {
      get { return shareKindIdLimit_; }
    }

    /// <summary>Field number for the "KindIdLimit" field.</summary>
    public const int KindIdLimitFieldNumber = 6;
    private static readonly pb::FieldCodec<global::D11.Pbeans.BattleBuyLimitConfig_KindIdLimit> _repeated_kindIdLimit_codec
        = pb::FieldCodec.ForMessage(50, global::D11.Pbeans.BattleBuyLimitConfig_KindIdLimit.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_KindIdLimit> kindIdLimit_ = new pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_KindIdLimit>();
    /// <summary>
    /// 燃烧弹 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig_KindIdLimit> KindIdLimit {
      get { return kindIdLimit_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BattleBuyLimitConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BattleBuyLimitConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (MaxOwnNum != other.MaxOwnNum) return false;
      if (MaxBuyNum != other.MaxBuyNum) return false;
      if(!subTypeLimit_.Equals(other.subTypeLimit_)) return false;
      if(!shareKindIdLimit_.Equals(other.shareKindIdLimit_)) return false;
      if(!kindIdLimit_.Equals(other.kindIdLimit_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (MaxOwnNum != 0) hash ^= MaxOwnNum.GetHashCode();
      if (MaxBuyNum != 0) hash ^= MaxBuyNum.GetHashCode();
      hash ^= subTypeLimit_.GetHashCode();
      hash ^= shareKindIdLimit_.GetHashCode();
      hash ^= kindIdLimit_.GetHashCode();
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
      if (MaxOwnNum != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(MaxOwnNum);
      }
      if (MaxBuyNum != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(MaxBuyNum);
      }
      subTypeLimit_.WriteTo(output, _repeated_subTypeLimit_codec);
      shareKindIdLimit_.WriteTo(output, _repeated_shareKindIdLimit_codec);
      kindIdLimit_.WriteTo(output, _repeated_kindIdLimit_codec);
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
      if (MaxOwnNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(MaxOwnNum);
      }
      if (MaxBuyNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(MaxBuyNum);
      }
      size += subTypeLimit_.CalculateSize(_repeated_subTypeLimit_codec);
      size += shareKindIdLimit_.CalculateSize(_repeated_shareKindIdLimit_codec);
      size += kindIdLimit_.CalculateSize(_repeated_kindIdLimit_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(BattleBuyLimitConfig other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.MaxOwnNum != 0) {
        MaxOwnNum = other.MaxOwnNum;
      }
      if (other.MaxBuyNum != 0) {
        MaxBuyNum = other.MaxBuyNum;
      }
      subTypeLimit_.Add(other.subTypeLimit_);
      shareKindIdLimit_.Add(other.shareKindIdLimit_);
      kindIdLimit_.Add(other.kindIdLimit_);
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
            MaxOwnNum = input.ReadInt32();
            break;
          }
          case 24: {
            MaxBuyNum = input.ReadInt32();
            break;
          }
          case 34: {
            subTypeLimit_.AddEntriesFrom(input, _repeated_subTypeLimit_codec);
            break;
          }
          case 42: {
            shareKindIdLimit_.AddEntriesFrom(input, _repeated_shareKindIdLimit_codec);
            break;
          }
          case 50: {
            kindIdLimit_.AddEntriesFrom(input, _repeated_kindIdLimit_codec);
            break;
          }
        }
      }
    }

  }

  public sealed partial class BattleBuyLimitConfig_SubTypeLimit : pb::IMessage<BattleBuyLimitConfig_SubTypeLimit> {
    private static readonly pb::MessageParser<BattleBuyLimitConfig_SubTypeLimit> _parser = new pb::MessageParser<BattleBuyLimitConfig_SubTypeLimit>(() => new BattleBuyLimitConfig_SubTypeLimit());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BattleBuyLimitConfig_SubTypeLimit> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBattlebuylimitconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_SubTypeLimit() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_SubTypeLimit(BattleBuyLimitConfig_SubTypeLimit other) : this() {
      subType_ = other.subType_;
      maxOwnNum_ = other.maxOwnNum_;
      maxBuyNum_ = other.maxBuyNum_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_SubTypeLimit Clone() {
      return new BattleBuyLimitConfig_SubTypeLimit(this);
    }

    /// <summary>Field number for the "subType" field.</summary>
    public const int SubTypeFieldNumber = 1;
    private uint subType_;
    /// <summary>
    /// 武器主类型:subType1 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint SubType {
      get { return subType_; }
      set {
        subType_ = value;
      }
    }

    /// <summary>Field number for the "maxOwnNum" field.</summary>
    public const int MaxOwnNumFieldNumber = 2;
    private int maxOwnNum_;
    /// <summary>
    /// 持有最大数 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int MaxOwnNum {
      get { return maxOwnNum_; }
      set {
        maxOwnNum_ = value;
      }
    }

    /// <summary>Field number for the "maxBuyNum" field.</summary>
    public const int MaxBuyNumFieldNumber = 3;
    private int maxBuyNum_;
    /// <summary>
    /// 购买次数 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int MaxBuyNum {
      get { return maxBuyNum_; }
      set {
        maxBuyNum_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BattleBuyLimitConfig_SubTypeLimit);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BattleBuyLimitConfig_SubTypeLimit other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (SubType != other.SubType) return false;
      if (MaxOwnNum != other.MaxOwnNum) return false;
      if (MaxBuyNum != other.MaxBuyNum) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (SubType != 0) hash ^= SubType.GetHashCode();
      if (MaxOwnNum != 0) hash ^= MaxOwnNum.GetHashCode();
      if (MaxBuyNum != 0) hash ^= MaxBuyNum.GetHashCode();
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
      if (SubType != 0) {
        output.WriteRawTag(8);
        output.WriteUInt32(SubType);
      }
      if (MaxOwnNum != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(MaxOwnNum);
      }
      if (MaxBuyNum != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(MaxBuyNum);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (SubType != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(SubType);
      }
      if (MaxOwnNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(MaxOwnNum);
      }
      if (MaxBuyNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(MaxBuyNum);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(BattleBuyLimitConfig_SubTypeLimit other) {
      if (other == null) {
        return;
      }
      if (other.SubType != 0) {
        SubType = other.SubType;
      }
      if (other.MaxOwnNum != 0) {
        MaxOwnNum = other.MaxOwnNum;
      }
      if (other.MaxBuyNum != 0) {
        MaxBuyNum = other.MaxBuyNum;
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
            SubType = input.ReadUInt32();
            break;
          }
          case 16: {
            MaxOwnNum = input.ReadInt32();
            break;
          }
          case 24: {
            MaxBuyNum = input.ReadInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class BattleBuyLimitConfig_ShareKindIdLimit : pb::IMessage<BattleBuyLimitConfig_ShareKindIdLimit> {
    private static readonly pb::MessageParser<BattleBuyLimitConfig_ShareKindIdLimit> _parser = new pb::MessageParser<BattleBuyLimitConfig_ShareKindIdLimit>(() => new BattleBuyLimitConfig_ShareKindIdLimit());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BattleBuyLimitConfig_ShareKindIdLimit> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBattlebuylimitconfigReflection.Descriptor.MessageTypes[2]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_ShareKindIdLimit() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_ShareKindIdLimit(BattleBuyLimitConfig_ShareKindIdLimit other) : this() {
      kindId_ = other.kindId_;
      maxOwnNum_ = other.maxOwnNum_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_ShareKindIdLimit Clone() {
      return new BattleBuyLimitConfig_ShareKindIdLimit(this);
    }

    /// <summary>Field number for the "kindId" field.</summary>
    public const int KindIdFieldNumber = 1;
    private string kindId_ = "";
    /// <summary>
    /// 武器类型1 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string KindId {
      get { return kindId_; }
      set {
        kindId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "maxOwnNum" field.</summary>
    public const int MaxOwnNumFieldNumber = 2;
    private int maxOwnNum_;
    /// <summary>
    /// 合计持有数 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int MaxOwnNum {
      get { return maxOwnNum_; }
      set {
        maxOwnNum_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BattleBuyLimitConfig_ShareKindIdLimit);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BattleBuyLimitConfig_ShareKindIdLimit other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (KindId != other.KindId) return false;
      if (MaxOwnNum != other.MaxOwnNum) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (KindId.Length != 0) hash ^= KindId.GetHashCode();
      if (MaxOwnNum != 0) hash ^= MaxOwnNum.GetHashCode();
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
      if (KindId.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(KindId);
      }
      if (MaxOwnNum != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(MaxOwnNum);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (KindId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(KindId);
      }
      if (MaxOwnNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(MaxOwnNum);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(BattleBuyLimitConfig_ShareKindIdLimit other) {
      if (other == null) {
        return;
      }
      if (other.KindId.Length != 0) {
        KindId = other.KindId;
      }
      if (other.MaxOwnNum != 0) {
        MaxOwnNum = other.MaxOwnNum;
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
          case 10: {
            KindId = input.ReadString();
            break;
          }
          case 16: {
            MaxOwnNum = input.ReadInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class BattleBuyLimitConfig_KindIdLimit : pb::IMessage<BattleBuyLimitConfig_KindIdLimit> {
    private static readonly pb::MessageParser<BattleBuyLimitConfig_KindIdLimit> _parser = new pb::MessageParser<BattleBuyLimitConfig_KindIdLimit>(() => new BattleBuyLimitConfig_KindIdLimit());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BattleBuyLimitConfig_KindIdLimit> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBattlebuylimitconfigReflection.Descriptor.MessageTypes[3]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_KindIdLimit() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_KindIdLimit(BattleBuyLimitConfig_KindIdLimit other) : this() {
      kindId_ = other.kindId_;
      maxOwnNum_ = other.maxOwnNum_;
      maxBuyNum_ = other.maxBuyNum_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_KindIdLimit Clone() {
      return new BattleBuyLimitConfig_KindIdLimit(this);
    }

    /// <summary>Field number for the "kindId" field.</summary>
    public const int KindIdFieldNumber = 1;
    private uint kindId_;
    /// <summary>
    /// 燃烧弹 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint KindId {
      get { return kindId_; }
      set {
        kindId_ = value;
      }
    }

    /// <summary>Field number for the "maxOwnNum" field.</summary>
    public const int MaxOwnNumFieldNumber = 2;
    private int maxOwnNum_;
    /// <summary>
    /// 持有最大数 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int MaxOwnNum {
      get { return maxOwnNum_; }
      set {
        maxOwnNum_ = value;
      }
    }

    /// <summary>Field number for the "maxBuyNum" field.</summary>
    public const int MaxBuyNumFieldNumber = 3;
    private int maxBuyNum_;
    /// <summary>
    /// 购买次数 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int MaxBuyNum {
      get { return maxBuyNum_; }
      set {
        maxBuyNum_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BattleBuyLimitConfig_KindIdLimit);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BattleBuyLimitConfig_KindIdLimit other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (KindId != other.KindId) return false;
      if (MaxOwnNum != other.MaxOwnNum) return false;
      if (MaxBuyNum != other.MaxBuyNum) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (KindId != 0) hash ^= KindId.GetHashCode();
      if (MaxOwnNum != 0) hash ^= MaxOwnNum.GetHashCode();
      if (MaxBuyNum != 0) hash ^= MaxBuyNum.GetHashCode();
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
      if (KindId != 0) {
        output.WriteRawTag(8);
        output.WriteUInt32(KindId);
      }
      if (MaxOwnNum != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(MaxOwnNum);
      }
      if (MaxBuyNum != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(MaxBuyNum);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (KindId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(KindId);
      }
      if (MaxOwnNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(MaxOwnNum);
      }
      if (MaxBuyNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(MaxBuyNum);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(BattleBuyLimitConfig_KindIdLimit other) {
      if (other == null) {
        return;
      }
      if (other.KindId != 0) {
        KindId = other.KindId;
      }
      if (other.MaxOwnNum != 0) {
        MaxOwnNum = other.MaxOwnNum;
      }
      if (other.MaxBuyNum != 0) {
        MaxBuyNum = other.MaxBuyNum;
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
            KindId = input.ReadUInt32();
            break;
          }
          case 16: {
            MaxOwnNum = input.ReadInt32();
            break;
          }
          case 24: {
            MaxBuyNum = input.ReadInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class BattleBuyLimitConfig_Array : pb::IMessage<BattleBuyLimitConfig_Array> {
    private static readonly pb::MessageParser<BattleBuyLimitConfig_Array> _parser = new pb::MessageParser<BattleBuyLimitConfig_Array>(() => new BattleBuyLimitConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BattleBuyLimitConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansBattlebuylimitconfigReflection.Descriptor.MessageTypes[4]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_Array(BattleBuyLimitConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BattleBuyLimitConfig_Array Clone() {
      return new BattleBuyLimitConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.BattleBuyLimitConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.BattleBuyLimitConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.BattleBuyLimitConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BattleBuyLimitConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BattleBuyLimitConfig_Array other) {
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
    public void MergeFrom(BattleBuyLimitConfig_Array other) {
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