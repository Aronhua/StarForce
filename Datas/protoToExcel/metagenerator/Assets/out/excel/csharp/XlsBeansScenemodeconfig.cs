// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_scenemodeconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_scenemodeconfig.proto</summary>
  public static partial class XlsBeansScenemodeconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_scenemodeconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansScenemodeconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch94bHNfYmVhbnNfc2NlbmVtb2RlY29uZmlnLnByb3RvEgpEMTEuUGJlYW5z",
            "IloKD1NjZW5lTW9kZUNvbmZpZxIKCgJpZBgBIAEoDRIMCgRpZE1TGAIgASgN",
            "EgwKBGRlc2MYAyABKAkSDgoGaWRNb2RlGAQgASgNEg8KB2lkU2NlbmUYBSAB",
            "KA0iQwoVU2NlbmVNb2RlQ29uZmlnX0FycmF5EioKBWl0ZW1zGAEgAygLMhsu",
            "RDExLlBiZWFucy5TY2VuZU1vZGVDb25maWdiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.SceneModeConfig), global::D11.Pbeans.SceneModeConfig.Parser, new[]{ "Id", "IdMS", "Desc", "IdMode", "IdScene" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.SceneModeConfig_Array), global::D11.Pbeans.SceneModeConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class SceneModeConfig : pb::IMessage<SceneModeConfig> {
    private static readonly pb::MessageParser<SceneModeConfig> _parser = new pb::MessageParser<SceneModeConfig>(() => new SceneModeConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<SceneModeConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansScenemodeconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SceneModeConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SceneModeConfig(SceneModeConfig other) : this() {
      id_ = other.id_;
      idMS_ = other.idMS_;
      desc_ = other.desc_;
      idMode_ = other.idMode_;
      idScene_ = other.idScene_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SceneModeConfig Clone() {
      return new SceneModeConfig(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private uint id_;
    /// <summary>
    /// 地图显示ID（局外） 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "idMS" field.</summary>
    public const int IdMSFieldNumber = 2;
    private uint idMS_;
    /// <summary>
    /// 地图玩法ID（局内） 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint IdMS {
      get { return idMS_; }
      set {
        idMS_ = value;
      }
    }

    /// <summary>Field number for the "desc" field.</summary>
    public const int DescFieldNumber = 3;
    private string desc_ = "";
    /// <summary>
    /// 备注 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Desc {
      get { return desc_; }
      set {
        desc_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "idMode" field.</summary>
    public const int IdModeFieldNumber = 4;
    private uint idMode_;
    /// <summary>
    /// 模式玩法ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint IdMode {
      get { return idMode_; }
      set {
        idMode_ = value;
      }
    }

    /// <summary>Field number for the "idScene" field.</summary>
    public const int IdSceneFieldNumber = 5;
    private uint idScene_;
    /// <summary>
    /// 场景ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint IdScene {
      get { return idScene_; }
      set {
        idScene_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as SceneModeConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(SceneModeConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (IdMS != other.IdMS) return false;
      if (Desc != other.Desc) return false;
      if (IdMode != other.IdMode) return false;
      if (IdScene != other.IdScene) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (IdMS != 0) hash ^= IdMS.GetHashCode();
      if (Desc.Length != 0) hash ^= Desc.GetHashCode();
      if (IdMode != 0) hash ^= IdMode.GetHashCode();
      if (IdScene != 0) hash ^= IdScene.GetHashCode();
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
      if (IdMS != 0) {
        output.WriteRawTag(16);
        output.WriteUInt32(IdMS);
      }
      if (Desc.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(Desc);
      }
      if (IdMode != 0) {
        output.WriteRawTag(32);
        output.WriteUInt32(IdMode);
      }
      if (IdScene != 0) {
        output.WriteRawTag(40);
        output.WriteUInt32(IdScene);
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
      if (IdMS != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(IdMS);
      }
      if (Desc.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Desc);
      }
      if (IdMode != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(IdMode);
      }
      if (IdScene != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(IdScene);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(SceneModeConfig other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.IdMS != 0) {
        IdMS = other.IdMS;
      }
      if (other.Desc.Length != 0) {
        Desc = other.Desc;
      }
      if (other.IdMode != 0) {
        IdMode = other.IdMode;
      }
      if (other.IdScene != 0) {
        IdScene = other.IdScene;
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
            IdMS = input.ReadUInt32();
            break;
          }
          case 26: {
            Desc = input.ReadString();
            break;
          }
          case 32: {
            IdMode = input.ReadUInt32();
            break;
          }
          case 40: {
            IdScene = input.ReadUInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class SceneModeConfig_Array : pb::IMessage<SceneModeConfig_Array> {
    private static readonly pb::MessageParser<SceneModeConfig_Array> _parser = new pb::MessageParser<SceneModeConfig_Array>(() => new SceneModeConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<SceneModeConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansScenemodeconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SceneModeConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SceneModeConfig_Array(SceneModeConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SceneModeConfig_Array Clone() {
      return new SceneModeConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.SceneModeConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.SceneModeConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.SceneModeConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.SceneModeConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.SceneModeConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as SceneModeConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(SceneModeConfig_Array other) {
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
    public void MergeFrom(SceneModeConfig_Array other) {
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