// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_tacticalvoice.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_tacticalvoice.proto</summary>
  public static partial class XlsBeansTacticalvoiceReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_tacticalvoice.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansTacticalvoiceReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch14bHNfYmVhbnNfdGFjdGljYWx2b2ljZS5wcm90bxIKRDExLlBiZWFucyLI",
            "AQoNVGFjdGljYWxWb2ljZRIKCgJpZBgBIAEoDRIYChB0YWN0aWNhbEFjdGlv",
            "bklkGAIgASgNEhIKCnRhcmdldFR5cGUYAyABKA0SEwoLVGl0bGVFbmFibGUY",
            "BCABKA0SGgoSSXNOb3RUYWN0aWNhbFRpdGxlGAUgASgNEhAKCGVudHJhbmNl",
            "GAYgASgJEg4KBmljb25JRBgHIAEoDRISCgpoYWxsSWNvbklEGAggASgNEhYK",
            "DklzTmVkZEFyZWFOYW1lGAkgASgIIj8KE1RhY3RpY2FsVm9pY2VfQXJyYXkS",
            "KAoFaXRlbXMYASADKAsyGS5EMTEuUGJlYW5zLlRhY3RpY2FsVm9pY2ViBnBy",
            "b3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.TacticalVoice), global::D11.Pbeans.TacticalVoice.Parser, new[]{ "Id", "TacticalActionId", "TargetType", "TitleEnable", "IsNotTacticalTitle", "Entrance", "IconID", "HallIconID", "IsNeddAreaName" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.TacticalVoice_Array), global::D11.Pbeans.TacticalVoice_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class TacticalVoice : pb::IMessage<TacticalVoice> {
    private static readonly pb::MessageParser<TacticalVoice> _parser = new pb::MessageParser<TacticalVoice>(() => new TacticalVoice());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<TacticalVoice> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansTacticalvoiceReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TacticalVoice() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TacticalVoice(TacticalVoice other) : this() {
      id_ = other.id_;
      tacticalActionId_ = other.tacticalActionId_;
      targetType_ = other.targetType_;
      titleEnable_ = other.titleEnable_;
      isNotTacticalTitle_ = other.isNotTacticalTitle_;
      entrance_ = other.entrance_;
      iconID_ = other.iconID_;
      hallIconID_ = other.hallIconID_;
      isNeddAreaName_ = other.isNeddAreaName_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TacticalVoice Clone() {
      return new TacticalVoice(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private uint id_;
    /// <summary>
    /// 检查用 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "tacticalActionId" field.</summary>
    public const int TacticalActionIdFieldNumber = 2;
    private uint tacticalActionId_;
    /// <summary>
    /// 战术动作类型（非0 ID读voxData表）获取语音和文本 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint TacticalActionId {
      get { return tacticalActionId_; }
      set {
        tacticalActionId_ = value;
      }
    }

    /// <summary>Field number for the "targetType" field.</summary>
    public const int TargetTypeFieldNumber = 3;
    private uint targetType_;
    /// <summary>
    /// 指示点类型 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint TargetType {
      get { return targetType_; }
      set {
        targetType_ = value;
      }
    }

    /// <summary>Field number for the "TitleEnable" field.</summary>
    public const int TitleEnableFieldNumber = 4;
    private uint titleEnable_;
    /// <summary>
    /// 是否UI显示 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint TitleEnable {
      get { return titleEnable_; }
      set {
        titleEnable_ = value;
      }
    }

    /// <summary>Field number for the "IsNotTacticalTitle" field.</summary>
    public const int IsNotTacticalTitleFieldNumber = 5;
    private uint isNotTacticalTitle_;
    /// <summary>
    /// 不是战术标记 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint IsNotTacticalTitle {
      get { return isNotTacticalTitle_; }
      set {
        isNotTacticalTitle_ = value;
      }
    }

    /// <summary>Field number for the "entrance" field.</summary>
    public const int EntranceFieldNumber = 6;
    private string entrance_ = "";
    /// <summary>
    /// 轮盘入口名称 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Entrance {
      get { return entrance_; }
      set {
        entrance_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "iconID" field.</summary>
    public const int IconIDFieldNumber = 7;
    private uint iconID_;
    /// <summary>
    /// GUI资源id 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint IconID {
      get { return iconID_; }
      set {
        iconID_ = value;
      }
    }

    /// <summary>Field number for the "hallIconID" field.</summary>
    public const int HallIconIDFieldNumber = 8;
    private uint hallIconID_;
    /// <summary>
    /// 局外GUI资源Id 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint HallIconID {
      get { return hallIconID_; }
      set {
        hallIconID_ = value;
      }
    }

    /// <summary>Field number for the "IsNeddAreaName" field.</summary>
    public const int IsNeddAreaNameFieldNumber = 9;
    private bool isNeddAreaName_;
    /// <summary>
    /// 是否需要携带地名 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool IsNeddAreaName {
      get { return isNeddAreaName_; }
      set {
        isNeddAreaName_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as TacticalVoice);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(TacticalVoice other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (TacticalActionId != other.TacticalActionId) return false;
      if (TargetType != other.TargetType) return false;
      if (TitleEnable != other.TitleEnable) return false;
      if (IsNotTacticalTitle != other.IsNotTacticalTitle) return false;
      if (Entrance != other.Entrance) return false;
      if (IconID != other.IconID) return false;
      if (HallIconID != other.HallIconID) return false;
      if (IsNeddAreaName != other.IsNeddAreaName) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (TacticalActionId != 0) hash ^= TacticalActionId.GetHashCode();
      if (TargetType != 0) hash ^= TargetType.GetHashCode();
      if (TitleEnable != 0) hash ^= TitleEnable.GetHashCode();
      if (IsNotTacticalTitle != 0) hash ^= IsNotTacticalTitle.GetHashCode();
      if (Entrance.Length != 0) hash ^= Entrance.GetHashCode();
      if (IconID != 0) hash ^= IconID.GetHashCode();
      if (HallIconID != 0) hash ^= HallIconID.GetHashCode();
      if (IsNeddAreaName != false) hash ^= IsNeddAreaName.GetHashCode();
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
      if (TacticalActionId != 0) {
        output.WriteRawTag(16);
        output.WriteUInt32(TacticalActionId);
      }
      if (TargetType != 0) {
        output.WriteRawTag(24);
        output.WriteUInt32(TargetType);
      }
      if (TitleEnable != 0) {
        output.WriteRawTag(32);
        output.WriteUInt32(TitleEnable);
      }
      if (IsNotTacticalTitle != 0) {
        output.WriteRawTag(40);
        output.WriteUInt32(IsNotTacticalTitle);
      }
      if (Entrance.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Entrance);
      }
      if (IconID != 0) {
        output.WriteRawTag(56);
        output.WriteUInt32(IconID);
      }
      if (HallIconID != 0) {
        output.WriteRawTag(64);
        output.WriteUInt32(HallIconID);
      }
      if (IsNeddAreaName != false) {
        output.WriteRawTag(72);
        output.WriteBool(IsNeddAreaName);
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
      if (TacticalActionId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(TacticalActionId);
      }
      if (TargetType != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(TargetType);
      }
      if (TitleEnable != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(TitleEnable);
      }
      if (IsNotTacticalTitle != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(IsNotTacticalTitle);
      }
      if (Entrance.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Entrance);
      }
      if (IconID != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(IconID);
      }
      if (HallIconID != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(HallIconID);
      }
      if (IsNeddAreaName != false) {
        size += 1 + 1;
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(TacticalVoice other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.TacticalActionId != 0) {
        TacticalActionId = other.TacticalActionId;
      }
      if (other.TargetType != 0) {
        TargetType = other.TargetType;
      }
      if (other.TitleEnable != 0) {
        TitleEnable = other.TitleEnable;
      }
      if (other.IsNotTacticalTitle != 0) {
        IsNotTacticalTitle = other.IsNotTacticalTitle;
      }
      if (other.Entrance.Length != 0) {
        Entrance = other.Entrance;
      }
      if (other.IconID != 0) {
        IconID = other.IconID;
      }
      if (other.HallIconID != 0) {
        HallIconID = other.HallIconID;
      }
      if (other.IsNeddAreaName != false) {
        IsNeddAreaName = other.IsNeddAreaName;
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
            TacticalActionId = input.ReadUInt32();
            break;
          }
          case 24: {
            TargetType = input.ReadUInt32();
            break;
          }
          case 32: {
            TitleEnable = input.ReadUInt32();
            break;
          }
          case 40: {
            IsNotTacticalTitle = input.ReadUInt32();
            break;
          }
          case 50: {
            Entrance = input.ReadString();
            break;
          }
          case 56: {
            IconID = input.ReadUInt32();
            break;
          }
          case 64: {
            HallIconID = input.ReadUInt32();
            break;
          }
          case 72: {
            IsNeddAreaName = input.ReadBool();
            break;
          }
        }
      }
    }

  }

  public sealed partial class TacticalVoice_Array : pb::IMessage<TacticalVoice_Array> {
    private static readonly pb::MessageParser<TacticalVoice_Array> _parser = new pb::MessageParser<TacticalVoice_Array>(() => new TacticalVoice_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<TacticalVoice_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansTacticalvoiceReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TacticalVoice_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TacticalVoice_Array(TacticalVoice_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public TacticalVoice_Array Clone() {
      return new TacticalVoice_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.TacticalVoice> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.TacticalVoice.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.TacticalVoice> items_ = new pbc::RepeatedField<global::D11.Pbeans.TacticalVoice>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.TacticalVoice> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as TacticalVoice_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(TacticalVoice_Array other) {
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
    public void MergeFrom(TacticalVoice_Array other) {
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