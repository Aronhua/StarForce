// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_roguelikeleveltalentconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_roguelikeleveltalentconfig.proto</summary>
  public static partial class XlsBeansRoguelikeleveltalentconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_roguelikeleveltalentconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansRoguelikeleveltalentconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Cip4bHNfYmVhbnNfcm9ndWVsaWtlbGV2ZWx0YWxlbnRjb25maWcucHJvdG8S",
            "CkQxMS5QYmVhbnMiigIKGlJvZ3VlTGlrZUxldmVsVGFsZW50Q29uZmlnEgoK",
            "AmlkGAEgASgNEg8KB2F0TGV2ZWwYAiABKA0SEQoJZ2FtZUxldmVsGAMgASgN",
            "EhIKCmZpcnN0R3JvdXAYBCABKAgSEgoKcGFja2V0TmFtZRgFIAEoCRIPCgdx",
            "dWFsaXR5GAYgASgNEhAKCFRhbGVudElkGAcgASgNEhQKDFRhbGVudFdlaWdo",
            "dBgIIAEoDRIQCgh3ZWFwb25JZBgJIAEoDRIUCgxxdWFsaXR5TGV2ZWwYCiAB",
            "KA0SEwoLd2VhcG9uTGV2ZWwYCyABKA0SDwoHbWVkc051bRgMIAEoDRINCgVt",
            "b25leRgNIAEoDSJZCiBSb2d1ZUxpa2VMZXZlbFRhbGVudENvbmZpZ19BcnJh",
            "eRI1CgVpdGVtcxgBIAMoCzImLkQxMS5QYmVhbnMuUm9ndWVMaWtlTGV2ZWxU",
            "YWxlbnRDb25maWdiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.RogueLikeLevelTalentConfig), global::D11.Pbeans.RogueLikeLevelTalentConfig.Parser, new[]{ "Id", "AtLevel", "GameLevel", "FirstGroup", "PacketName", "Quality", "TalentId", "TalentWeight", "WeaponId", "QualityLevel", "WeaponLevel", "MedsNum", "Money" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.RogueLikeLevelTalentConfig_Array), global::D11.Pbeans.RogueLikeLevelTalentConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class RogueLikeLevelTalentConfig : pb::IMessage<RogueLikeLevelTalentConfig> {
    private static readonly pb::MessageParser<RogueLikeLevelTalentConfig> _parser = new pb::MessageParser<RogueLikeLevelTalentConfig>(() => new RogueLikeLevelTalentConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<RogueLikeLevelTalentConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansRoguelikeleveltalentconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RogueLikeLevelTalentConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RogueLikeLevelTalentConfig(RogueLikeLevelTalentConfig other) : this() {
      id_ = other.id_;
      atLevel_ = other.atLevel_;
      gameLevel_ = other.gameLevel_;
      firstGroup_ = other.firstGroup_;
      packetName_ = other.packetName_;
      quality_ = other.quality_;
      talentId_ = other.talentId_;
      talentWeight_ = other.talentWeight_;
      weaponId_ = other.weaponId_;
      qualityLevel_ = other.qualityLevel_;
      weaponLevel_ = other.weaponLevel_;
      medsNum_ = other.medsNum_;
      money_ = other.money_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RogueLikeLevelTalentConfig Clone() {
      return new RogueLikeLevelTalentConfig(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private uint id_;
    /// <summary>
    /// 包id 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "atLevel" field.</summary>
    public const int AtLevelFieldNumber = 2;
    private uint atLevel_;
    /// <summary>
    /// 关卡 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint AtLevel {
      get { return atLevel_; }
      set {
        atLevel_ = value;
      }
    }

    /// <summary>Field number for the "gameLevel" field.</summary>
    public const int GameLevelFieldNumber = 3;
    private uint gameLevel_;
    /// <summary>
    /// 难度 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint GameLevel {
      get { return gameLevel_; }
      set {
        gameLevel_ = value;
      }
    }

    /// <summary>Field number for the "firstGroup" field.</summary>
    public const int FirstGroupFieldNumber = 4;
    private bool firstGroup_;
    /// <summary>
    /// 第一组 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool FirstGroup {
      get { return firstGroup_; }
      set {
        firstGroup_ = value;
      }
    }

    /// <summary>Field number for the "packetName" field.</summary>
    public const int PacketNameFieldNumber = 5;
    private string packetName_ = "";
    /// <summary>
    /// 包名 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string PacketName {
      get { return packetName_; }
      set {
        packetName_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
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

    /// <summary>Field number for the "TalentId" field.</summary>
    public const int TalentIdFieldNumber = 7;
    private uint talentId_;
    /// <summary>
    /// 天赋ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint TalentId {
      get { return talentId_; }
      set {
        talentId_ = value;
      }
    }

    /// <summary>Field number for the "TalentWeight" field.</summary>
    public const int TalentWeightFieldNumber = 8;
    private uint talentWeight_;
    /// <summary>
    /// 天赋权重 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint TalentWeight {
      get { return talentWeight_; }
      set {
        talentWeight_ = value;
      }
    }

    /// <summary>Field number for the "weaponId" field.</summary>
    public const int WeaponIdFieldNumber = 9;
    private uint weaponId_;
    /// <summary>
    /// 武器种类 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint WeaponId {
      get { return weaponId_; }
      set {
        weaponId_ = value;
      }
    }

    /// <summary>Field number for the "qualityLevel" field.</summary>
    public const int QualityLevelFieldNumber = 10;
    private uint qualityLevel_;
    /// <summary>
    /// 品质等级 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint QualityLevel {
      get { return qualityLevel_; }
      set {
        qualityLevel_ = value;
      }
    }

    /// <summary>Field number for the "weaponLevel" field.</summary>
    public const int WeaponLevelFieldNumber = 11;
    private uint weaponLevel_;
    /// <summary>
    /// 武器等级 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint WeaponLevel {
      get { return weaponLevel_; }
      set {
        weaponLevel_ = value;
      }
    }

    /// <summary>Field number for the "medsNum" field.</summary>
    public const int MedsNumFieldNumber = 12;
    private uint medsNum_;
    /// <summary>
    /// 医疗针数量 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint MedsNum {
      get { return medsNum_; }
      set {
        medsNum_ = value;
      }
    }

    /// <summary>Field number for the "money" field.</summary>
    public const int MoneyFieldNumber = 13;
    private uint money_;
    /// <summary>
    /// 金钱数量 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Money {
      get { return money_; }
      set {
        money_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as RogueLikeLevelTalentConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(RogueLikeLevelTalentConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (AtLevel != other.AtLevel) return false;
      if (GameLevel != other.GameLevel) return false;
      if (FirstGroup != other.FirstGroup) return false;
      if (PacketName != other.PacketName) return false;
      if (Quality != other.Quality) return false;
      if (TalentId != other.TalentId) return false;
      if (TalentWeight != other.TalentWeight) return false;
      if (WeaponId != other.WeaponId) return false;
      if (QualityLevel != other.QualityLevel) return false;
      if (WeaponLevel != other.WeaponLevel) return false;
      if (MedsNum != other.MedsNum) return false;
      if (Money != other.Money) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (AtLevel != 0) hash ^= AtLevel.GetHashCode();
      if (GameLevel != 0) hash ^= GameLevel.GetHashCode();
      if (FirstGroup != false) hash ^= FirstGroup.GetHashCode();
      if (PacketName.Length != 0) hash ^= PacketName.GetHashCode();
      if (Quality != 0) hash ^= Quality.GetHashCode();
      if (TalentId != 0) hash ^= TalentId.GetHashCode();
      if (TalentWeight != 0) hash ^= TalentWeight.GetHashCode();
      if (WeaponId != 0) hash ^= WeaponId.GetHashCode();
      if (QualityLevel != 0) hash ^= QualityLevel.GetHashCode();
      if (WeaponLevel != 0) hash ^= WeaponLevel.GetHashCode();
      if (MedsNum != 0) hash ^= MedsNum.GetHashCode();
      if (Money != 0) hash ^= Money.GetHashCode();
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
      if (AtLevel != 0) {
        output.WriteRawTag(16);
        output.WriteUInt32(AtLevel);
      }
      if (GameLevel != 0) {
        output.WriteRawTag(24);
        output.WriteUInt32(GameLevel);
      }
      if (FirstGroup != false) {
        output.WriteRawTag(32);
        output.WriteBool(FirstGroup);
      }
      if (PacketName.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(PacketName);
      }
      if (Quality != 0) {
        output.WriteRawTag(48);
        output.WriteUInt32(Quality);
      }
      if (TalentId != 0) {
        output.WriteRawTag(56);
        output.WriteUInt32(TalentId);
      }
      if (TalentWeight != 0) {
        output.WriteRawTag(64);
        output.WriteUInt32(TalentWeight);
      }
      if (WeaponId != 0) {
        output.WriteRawTag(72);
        output.WriteUInt32(WeaponId);
      }
      if (QualityLevel != 0) {
        output.WriteRawTag(80);
        output.WriteUInt32(QualityLevel);
      }
      if (WeaponLevel != 0) {
        output.WriteRawTag(88);
        output.WriteUInt32(WeaponLevel);
      }
      if (MedsNum != 0) {
        output.WriteRawTag(96);
        output.WriteUInt32(MedsNum);
      }
      if (Money != 0) {
        output.WriteRawTag(104);
        output.WriteUInt32(Money);
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
      if (AtLevel != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(AtLevel);
      }
      if (GameLevel != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(GameLevel);
      }
      if (FirstGroup != false) {
        size += 1 + 1;
      }
      if (PacketName.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(PacketName);
      }
      if (Quality != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Quality);
      }
      if (TalentId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(TalentId);
      }
      if (TalentWeight != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(TalentWeight);
      }
      if (WeaponId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(WeaponId);
      }
      if (QualityLevel != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(QualityLevel);
      }
      if (WeaponLevel != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(WeaponLevel);
      }
      if (MedsNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(MedsNum);
      }
      if (Money != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Money);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(RogueLikeLevelTalentConfig other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.AtLevel != 0) {
        AtLevel = other.AtLevel;
      }
      if (other.GameLevel != 0) {
        GameLevel = other.GameLevel;
      }
      if (other.FirstGroup != false) {
        FirstGroup = other.FirstGroup;
      }
      if (other.PacketName.Length != 0) {
        PacketName = other.PacketName;
      }
      if (other.Quality != 0) {
        Quality = other.Quality;
      }
      if (other.TalentId != 0) {
        TalentId = other.TalentId;
      }
      if (other.TalentWeight != 0) {
        TalentWeight = other.TalentWeight;
      }
      if (other.WeaponId != 0) {
        WeaponId = other.WeaponId;
      }
      if (other.QualityLevel != 0) {
        QualityLevel = other.QualityLevel;
      }
      if (other.WeaponLevel != 0) {
        WeaponLevel = other.WeaponLevel;
      }
      if (other.MedsNum != 0) {
        MedsNum = other.MedsNum;
      }
      if (other.Money != 0) {
        Money = other.Money;
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
            AtLevel = input.ReadUInt32();
            break;
          }
          case 24: {
            GameLevel = input.ReadUInt32();
            break;
          }
          case 32: {
            FirstGroup = input.ReadBool();
            break;
          }
          case 42: {
            PacketName = input.ReadString();
            break;
          }
          case 48: {
            Quality = input.ReadUInt32();
            break;
          }
          case 56: {
            TalentId = input.ReadUInt32();
            break;
          }
          case 64: {
            TalentWeight = input.ReadUInt32();
            break;
          }
          case 72: {
            WeaponId = input.ReadUInt32();
            break;
          }
          case 80: {
            QualityLevel = input.ReadUInt32();
            break;
          }
          case 88: {
            WeaponLevel = input.ReadUInt32();
            break;
          }
          case 96: {
            MedsNum = input.ReadUInt32();
            break;
          }
          case 104: {
            Money = input.ReadUInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class RogueLikeLevelTalentConfig_Array : pb::IMessage<RogueLikeLevelTalentConfig_Array> {
    private static readonly pb::MessageParser<RogueLikeLevelTalentConfig_Array> _parser = new pb::MessageParser<RogueLikeLevelTalentConfig_Array>(() => new RogueLikeLevelTalentConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<RogueLikeLevelTalentConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansRoguelikeleveltalentconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RogueLikeLevelTalentConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RogueLikeLevelTalentConfig_Array(RogueLikeLevelTalentConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public RogueLikeLevelTalentConfig_Array Clone() {
      return new RogueLikeLevelTalentConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.RogueLikeLevelTalentConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.RogueLikeLevelTalentConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.RogueLikeLevelTalentConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.RogueLikeLevelTalentConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.RogueLikeLevelTalentConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as RogueLikeLevelTalentConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(RogueLikeLevelTalentConfig_Array other) {
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
    public void MergeFrom(RogueLikeLevelTalentConfig_Array other) {
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