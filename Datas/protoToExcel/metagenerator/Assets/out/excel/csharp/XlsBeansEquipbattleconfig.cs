// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_equipbattleconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_equipbattleconfig.proto</summary>
  public static partial class XlsBeansEquipbattleconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_equipbattleconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansEquipbattleconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiF4bHNfYmVhbnNfZXF1aXBiYXR0bGVjb25maWcucHJvdG8SCkQxMS5QYmVh",
            "bnMijgEKEUVxdWlwQmF0dGxlQ29uZmlnEgoKAmlkGAEgASgNEgwKBG5hbWUY",
            "AiABKAkSEQoJRXF1aXBUeXBlGAMgASgNEgwKBGljb24YBCABKA0SGAoQd2Vh",
            "cG9uQ29uZmlnTmFtZRgFIAEoCRIQCghEZXNjcmliZRgGIAEoCRISCgphdHRy",
            "aWJ1dGVzGAcgAygNIkcKF0VxdWlwQmF0dGxlQ29uZmlnX0FycmF5EiwKBWl0",
            "ZW1zGAEgAygLMh0uRDExLlBiZWFucy5FcXVpcEJhdHRsZUNvbmZpZ2IGcHJv",
            "dG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.EquipBattleConfig), global::D11.Pbeans.EquipBattleConfig.Parser, new[]{ "Id", "Name", "EquipType", "Icon", "WeaponConfigName", "Describe", "Attributes" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.EquipBattleConfig_Array), global::D11.Pbeans.EquipBattleConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class EquipBattleConfig : pb::IMessage<EquipBattleConfig> {
    private static readonly pb::MessageParser<EquipBattleConfig> _parser = new pb::MessageParser<EquipBattleConfig>(() => new EquipBattleConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<EquipBattleConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansEquipbattleconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBattleConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBattleConfig(EquipBattleConfig other) : this() {
      id_ = other.id_;
      name_ = other.name_;
      equipType_ = other.equipType_;
      icon_ = other.icon_;
      weaponConfigName_ = other.weaponConfigName_;
      describe_ = other.describe_;
      attributes_ = other.attributes_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBattleConfig Clone() {
      return new EquipBattleConfig(this);
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

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 2;
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

    /// <summary>Field number for the "EquipType" field.</summary>
    public const int EquipTypeFieldNumber = 3;
    private uint equipType_;
    /// <summary>
    /// 装备类型 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint EquipType {
      get { return equipType_; }
      set {
        equipType_ = value;
      }
    }

    /// <summary>Field number for the "icon" field.</summary>
    public const int IconFieldNumber = 4;
    private uint icon_;
    /// <summary>
    /// HUD图标 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Icon {
      get { return icon_; }
      set {
        icon_ = value;
      }
    }

    /// <summary>Field number for the "weaponConfigName" field.</summary>
    public const int WeaponConfigNameFieldNumber = 5;
    private string weaponConfigName_ = "";
    /// <summary>
    /// AttributeConfig 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string WeaponConfigName {
      get { return weaponConfigName_; }
      set {
        weaponConfigName_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "Describe" field.</summary>
    public const int DescribeFieldNumber = 6;
    private string describe_ = "";
    /// <summary>
    ///  
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Describe {
      get { return describe_; }
      set {
        describe_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "attributes" field.</summary>
    public const int AttributesFieldNumber = 7;
    private static readonly pb::FieldCodec<uint> _repeated_attributes_codec
        = pb::FieldCodec.ForUInt32(58);
    private readonly pbc::RepeatedField<uint> attributes_ = new pbc::RepeatedField<uint>();
    /// <summary>
    /// 推荐&amp;特点列表 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<uint> Attributes {
      get { return attributes_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as EquipBattleConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(EquipBattleConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (Name != other.Name) return false;
      if (EquipType != other.EquipType) return false;
      if (Icon != other.Icon) return false;
      if (WeaponConfigName != other.WeaponConfigName) return false;
      if (Describe != other.Describe) return false;
      if(!attributes_.Equals(other.attributes_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (EquipType != 0) hash ^= EquipType.GetHashCode();
      if (Icon != 0) hash ^= Icon.GetHashCode();
      if (WeaponConfigName.Length != 0) hash ^= WeaponConfigName.GetHashCode();
      if (Describe.Length != 0) hash ^= Describe.GetHashCode();
      hash ^= attributes_.GetHashCode();
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
      if (Name.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Name);
      }
      if (EquipType != 0) {
        output.WriteRawTag(24);
        output.WriteUInt32(EquipType);
      }
      if (Icon != 0) {
        output.WriteRawTag(32);
        output.WriteUInt32(Icon);
      }
      if (WeaponConfigName.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(WeaponConfigName);
      }
      if (Describe.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Describe);
      }
      attributes_.WriteTo(output, _repeated_attributes_codec);
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
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (EquipType != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(EquipType);
      }
      if (Icon != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Icon);
      }
      if (WeaponConfigName.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(WeaponConfigName);
      }
      if (Describe.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Describe);
      }
      size += attributes_.CalculateSize(_repeated_attributes_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(EquipBattleConfig other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      if (other.EquipType != 0) {
        EquipType = other.EquipType;
      }
      if (other.Icon != 0) {
        Icon = other.Icon;
      }
      if (other.WeaponConfigName.Length != 0) {
        WeaponConfigName = other.WeaponConfigName;
      }
      if (other.Describe.Length != 0) {
        Describe = other.Describe;
      }
      attributes_.Add(other.attributes_);
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
          case 18: {
            Name = input.ReadString();
            break;
          }
          case 24: {
            EquipType = input.ReadUInt32();
            break;
          }
          case 32: {
            Icon = input.ReadUInt32();
            break;
          }
          case 42: {
            WeaponConfigName = input.ReadString();
            break;
          }
          case 50: {
            Describe = input.ReadString();
            break;
          }
          case 58:
          case 56: {
            attributes_.AddEntriesFrom(input, _repeated_attributes_codec);
            break;
          }
        }
      }
    }

  }

  public sealed partial class EquipBattleConfig_Array : pb::IMessage<EquipBattleConfig_Array> {
    private static readonly pb::MessageParser<EquipBattleConfig_Array> _parser = new pb::MessageParser<EquipBattleConfig_Array>(() => new EquipBattleConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<EquipBattleConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansEquipbattleconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBattleConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBattleConfig_Array(EquipBattleConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public EquipBattleConfig_Array Clone() {
      return new EquipBattleConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.EquipBattleConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.EquipBattleConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.EquipBattleConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.EquipBattleConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.EquipBattleConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as EquipBattleConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(EquipBattleConfig_Array other) {
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
    public void MergeFrom(EquipBattleConfig_Array other) {
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