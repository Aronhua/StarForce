// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_headframeconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_headframeconfig.proto</summary>
  public static partial class XlsBeansHeadframeconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_headframeconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansHeadframeconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch94bHNfYmVhbnNfaGVhZGZyYW1lY29uZmlnLnByb3RvEgpEMTEuUGJlYW5z",
            "Ir0BCg9IZWFkRnJhbWVDb25maWcSCgoCaWQYASABKA0SDgoGaXNTaG93GAIg",
            "ASgIEg4KBmljb25JRBgDIAEoDRIOCgZlZmZlY3QYBCABKAkSDAoEbmFtZRgF",
            "IAEoCRIPCgdxdWFsaXR5GAYgASgNEhUKDWRlc2NyaXB0aW9uSUQYByABKA0S",
            "EQoJaXNEZWZhdWx0GAggASgIEhIKCmxvY2tJdGVtSWQYCSABKA0SEQoJcm9i",
            "b3RVc2VkGAogASgNIkMKFUhlYWRGcmFtZUNvbmZpZ19BcnJheRIqCgVpdGVt",
            "cxgBIAMoCzIbLkQxMS5QYmVhbnMuSGVhZEZyYW1lQ29uZmlnYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.HeadFrameConfig), global::D11.Pbeans.HeadFrameConfig.Parser, new[]{ "Id", "IsShow", "IconID", "Effect", "Name", "Quality", "DescriptionID", "IsDefault", "LockItemId", "RobotUsed" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.HeadFrameConfig_Array), global::D11.Pbeans.HeadFrameConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class HeadFrameConfig : pb::IMessage<HeadFrameConfig> {
    private static readonly pb::MessageParser<HeadFrameConfig> _parser = new pb::MessageParser<HeadFrameConfig>(() => new HeadFrameConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<HeadFrameConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansHeadframeconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public HeadFrameConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public HeadFrameConfig(HeadFrameConfig other) : this() {
      id_ = other.id_;
      isShow_ = other.isShow_;
      iconID_ = other.iconID_;
      effect_ = other.effect_;
      name_ = other.name_;
      quality_ = other.quality_;
      descriptionID_ = other.descriptionID_;
      isDefault_ = other.isDefault_;
      lockItemId_ = other.lockItemId_;
      robotUsed_ = other.robotUsed_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public HeadFrameConfig Clone() {
      return new HeadFrameConfig(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private uint id_;
    /// <summary>
    /// 图片名（系统） 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "isShow" field.</summary>
    public const int IsShowFieldNumber = 2;
    private bool isShow_;
    /// <summary>
    /// 是否显示 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool IsShow {
      get { return isShow_; }
      set {
        isShow_ = value;
      }
    }

    /// <summary>Field number for the "iconID" field.</summary>
    public const int IconIDFieldNumber = 3;
    private uint iconID_;
    /// <summary>
    /// 资源id 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint IconID {
      get { return iconID_; }
      set {
        iconID_ = value;
      }
    }

    /// <summary>Field number for the "effect" field.</summary>
    public const int EffectFieldNumber = 4;
    private string effect_ = "";
    /// <summary>
    /// 特效路径 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Effect {
      get { return effect_; }
      set {
        effect_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 5;
    private string name_ = "";
    /// <summary>
    /// 物品名称 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "quality" field.</summary>
    public const int QualityFieldNumber = 6;
    private uint quality_;
    /// <summary>
    /// 品质 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Quality {
      get { return quality_; }
      set {
        quality_ = value;
      }
    }

    /// <summary>Field number for the "descriptionID" field.</summary>
    public const int DescriptionIDFieldNumber = 7;
    private uint descriptionID_;
    /// <summary>
    /// 描述 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint DescriptionID {
      get { return descriptionID_; }
      set {
        descriptionID_ = value;
      }
    }

    /// <summary>Field number for the "isDefault" field.</summary>
    public const int IsDefaultFieldNumber = 8;
    private bool isDefault_;
    /// <summary>
    /// 默认解锁 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool IsDefault {
      get { return isDefault_; }
      set {
        isDefault_ = value;
      }
    }

    /// <summary>Field number for the "lockItemId" field.</summary>
    public const int LockItemIdFieldNumber = 9;
    private uint lockItemId_;
    /// <summary>
    /// 解锁物品ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint LockItemId {
      get { return lockItemId_; }
      set {
        lockItemId_ = value;
      }
    }

    /// <summary>Field number for the "robotUsed" field.</summary>
    public const int RobotUsedFieldNumber = 10;
    private uint robotUsed_;
    /// <summary>
    /// 机器人是否可用,1:可用 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint RobotUsed {
      get { return robotUsed_; }
      set {
        robotUsed_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as HeadFrameConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(HeadFrameConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (IsShow != other.IsShow) return false;
      if (IconID != other.IconID) return false;
      if (Effect != other.Effect) return false;
      if (Name != other.Name) return false;
      if (Quality != other.Quality) return false;
      if (DescriptionID != other.DescriptionID) return false;
      if (IsDefault != other.IsDefault) return false;
      if (LockItemId != other.LockItemId) return false;
      if (RobotUsed != other.RobotUsed) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (IsShow != false) hash ^= IsShow.GetHashCode();
      if (IconID != 0) hash ^= IconID.GetHashCode();
      if (Effect.Length != 0) hash ^= Effect.GetHashCode();
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (Quality != 0) hash ^= Quality.GetHashCode();
      if (DescriptionID != 0) hash ^= DescriptionID.GetHashCode();
      if (IsDefault != false) hash ^= IsDefault.GetHashCode();
      if (LockItemId != 0) hash ^= LockItemId.GetHashCode();
      if (RobotUsed != 0) hash ^= RobotUsed.GetHashCode();
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
      if (IsShow != false) {
        output.WriteRawTag(16);
        output.WriteBool(IsShow);
      }
      if (IconID != 0) {
        output.WriteRawTag(24);
        output.WriteUInt32(IconID);
      }
      if (Effect.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Effect);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Name);
      }
      if (Quality != 0) {
        output.WriteRawTag(48);
        output.WriteUInt32(Quality);
      }
      if (DescriptionID != 0) {
        output.WriteRawTag(56);
        output.WriteUInt32(DescriptionID);
      }
      if (IsDefault != false) {
        output.WriteRawTag(64);
        output.WriteBool(IsDefault);
      }
      if (LockItemId != 0) {
        output.WriteRawTag(72);
        output.WriteUInt32(LockItemId);
      }
      if (RobotUsed != 0) {
        output.WriteRawTag(80);
        output.WriteUInt32(RobotUsed);
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
      if (IsShow != false) {
        size += 1 + 1;
      }
      if (IconID != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(IconID);
      }
      if (Effect.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Effect);
      }
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (Quality != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Quality);
      }
      if (DescriptionID != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(DescriptionID);
      }
      if (IsDefault != false) {
        size += 1 + 1;
      }
      if (LockItemId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(LockItemId);
      }
      if (RobotUsed != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(RobotUsed);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(HeadFrameConfig other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.IsShow != false) {
        IsShow = other.IsShow;
      }
      if (other.IconID != 0) {
        IconID = other.IconID;
      }
      if (other.Effect.Length != 0) {
        Effect = other.Effect;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      if (other.Quality != 0) {
        Quality = other.Quality;
      }
      if (other.DescriptionID != 0) {
        DescriptionID = other.DescriptionID;
      }
      if (other.IsDefault != false) {
        IsDefault = other.IsDefault;
      }
      if (other.LockItemId != 0) {
        LockItemId = other.LockItemId;
      }
      if (other.RobotUsed != 0) {
        RobotUsed = other.RobotUsed;
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
            IsShow = input.ReadBool();
            break;
          }
          case 24: {
            IconID = input.ReadUInt32();
            break;
          }
          case 34: {
            Effect = input.ReadString();
            break;
          }
          case 42: {
            Name = input.ReadString();
            break;
          }
          case 48: {
            Quality = input.ReadUInt32();
            break;
          }
          case 56: {
            DescriptionID = input.ReadUInt32();
            break;
          }
          case 64: {
            IsDefault = input.ReadBool();
            break;
          }
          case 72: {
            LockItemId = input.ReadUInt32();
            break;
          }
          case 80: {
            RobotUsed = input.ReadUInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class HeadFrameConfig_Array : pb::IMessage<HeadFrameConfig_Array> {
    private static readonly pb::MessageParser<HeadFrameConfig_Array> _parser = new pb::MessageParser<HeadFrameConfig_Array>(() => new HeadFrameConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<HeadFrameConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansHeadframeconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public HeadFrameConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public HeadFrameConfig_Array(HeadFrameConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public HeadFrameConfig_Array Clone() {
      return new HeadFrameConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.HeadFrameConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.HeadFrameConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.HeadFrameConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.HeadFrameConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.HeadFrameConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as HeadFrameConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(HeadFrameConfig_Array other) {
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
    public void MergeFrom(HeadFrameConfig_Array other) {
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