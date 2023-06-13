// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_deathmatchrandweapon.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_deathmatchrandweapon.proto</summary>
  public static partial class XlsBeansDeathmatchrandweaponReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_deathmatchrandweapon.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansDeathmatchrandweaponReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiR4bHNfYmVhbnNfZGVhdGhtYXRjaHJhbmR3ZWFwb24ucHJvdG8SCkQxMS5Q",
            "YmVhbnMibAoURGVhdGhNYXRjaFJhbmRXZWFwb24SDgoGbW9kZUlkGAEgASgN",
            "EhAKCHdlYXBvbmlkGAIgASgNEhEKCXJhbmtCZWdpbhgDIAEoBRIPCgdyYW5r",
            "RW5kGAQgASgFEg4KBndlaWdodBgFIAEoDSJNChpEZWF0aE1hdGNoUmFuZFdl",
            "YXBvbl9BcnJheRIvCgVpdGVtcxgBIAMoCzIgLkQxMS5QYmVhbnMuRGVhdGhN",
            "YXRjaFJhbmRXZWFwb25iBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.DeathMatchRandWeapon), global::D11.Pbeans.DeathMatchRandWeapon.Parser, new[]{ "ModeId", "Weaponid", "RankBegin", "RankEnd", "Weight" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.DeathMatchRandWeapon_Array), global::D11.Pbeans.DeathMatchRandWeapon_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class DeathMatchRandWeapon : pb::IMessage<DeathMatchRandWeapon> {
    private static readonly pb::MessageParser<DeathMatchRandWeapon> _parser = new pb::MessageParser<DeathMatchRandWeapon>(() => new DeathMatchRandWeapon());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<DeathMatchRandWeapon> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansDeathmatchrandweaponReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public DeathMatchRandWeapon() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public DeathMatchRandWeapon(DeathMatchRandWeapon other) : this() {
      modeId_ = other.modeId_;
      weaponid_ = other.weaponid_;
      rankBegin_ = other.rankBegin_;
      rankEnd_ = other.rankEnd_;
      weight_ = other.weight_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public DeathMatchRandWeapon Clone() {
      return new DeathMatchRandWeapon(this);
    }

    /// <summary>Field number for the "modeId" field.</summary>
    public const int ModeIdFieldNumber = 1;
    private uint modeId_;
    /// <summary>
    /// 模式id 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint ModeId {
      get { return modeId_; }
      set {
        modeId_ = value;
      }
    }

    /// <summary>Field number for the "weaponid" field.</summary>
    public const int WeaponidFieldNumber = 2;
    private uint weaponid_;
    /// <summary>
    /// 武器id 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Weaponid {
      get { return weaponid_; }
      set {
        weaponid_ = value;
      }
    }

    /// <summary>Field number for the "rankBegin" field.</summary>
    public const int RankBeginFieldNumber = 3;
    private int rankBegin_;
    /// <summary>
    /// 排行区间下 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int RankBegin {
      get { return rankBegin_; }
      set {
        rankBegin_ = value;
      }
    }

    /// <summary>Field number for the "rankEnd" field.</summary>
    public const int RankEndFieldNumber = 4;
    private int rankEnd_;
    /// <summary>
    /// 排行区间上 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int RankEnd {
      get { return rankEnd_; }
      set {
        rankEnd_ = value;
      }
    }

    /// <summary>Field number for the "weight" field.</summary>
    public const int WeightFieldNumber = 5;
    private uint weight_;
    /// <summary>
    /// 权重 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Weight {
      get { return weight_; }
      set {
        weight_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as DeathMatchRandWeapon);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(DeathMatchRandWeapon other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (ModeId != other.ModeId) return false;
      if (Weaponid != other.Weaponid) return false;
      if (RankBegin != other.RankBegin) return false;
      if (RankEnd != other.RankEnd) return false;
      if (Weight != other.Weight) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (ModeId != 0) hash ^= ModeId.GetHashCode();
      if (Weaponid != 0) hash ^= Weaponid.GetHashCode();
      if (RankBegin != 0) hash ^= RankBegin.GetHashCode();
      if (RankEnd != 0) hash ^= RankEnd.GetHashCode();
      if (Weight != 0) hash ^= Weight.GetHashCode();
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
      if (ModeId != 0) {
        output.WriteRawTag(8);
        output.WriteUInt32(ModeId);
      }
      if (Weaponid != 0) {
        output.WriteRawTag(16);
        output.WriteUInt32(Weaponid);
      }
      if (RankBegin != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(RankBegin);
      }
      if (RankEnd != 0) {
        output.WriteRawTag(32);
        output.WriteInt32(RankEnd);
      }
      if (Weight != 0) {
        output.WriteRawTag(40);
        output.WriteUInt32(Weight);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (ModeId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(ModeId);
      }
      if (Weaponid != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Weaponid);
      }
      if (RankBegin != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(RankBegin);
      }
      if (RankEnd != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(RankEnd);
      }
      if (Weight != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Weight);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(DeathMatchRandWeapon other) {
      if (other == null) {
        return;
      }
      if (other.ModeId != 0) {
        ModeId = other.ModeId;
      }
      if (other.Weaponid != 0) {
        Weaponid = other.Weaponid;
      }
      if (other.RankBegin != 0) {
        RankBegin = other.RankBegin;
      }
      if (other.RankEnd != 0) {
        RankEnd = other.RankEnd;
      }
      if (other.Weight != 0) {
        Weight = other.Weight;
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
            ModeId = input.ReadUInt32();
            break;
          }
          case 16: {
            Weaponid = input.ReadUInt32();
            break;
          }
          case 24: {
            RankBegin = input.ReadInt32();
            break;
          }
          case 32: {
            RankEnd = input.ReadInt32();
            break;
          }
          case 40: {
            Weight = input.ReadUInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class DeathMatchRandWeapon_Array : pb::IMessage<DeathMatchRandWeapon_Array> {
    private static readonly pb::MessageParser<DeathMatchRandWeapon_Array> _parser = new pb::MessageParser<DeathMatchRandWeapon_Array>(() => new DeathMatchRandWeapon_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<DeathMatchRandWeapon_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansDeathmatchrandweaponReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public DeathMatchRandWeapon_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public DeathMatchRandWeapon_Array(DeathMatchRandWeapon_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public DeathMatchRandWeapon_Array Clone() {
      return new DeathMatchRandWeapon_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.DeathMatchRandWeapon> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.DeathMatchRandWeapon.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.DeathMatchRandWeapon> items_ = new pbc::RepeatedField<global::D11.Pbeans.DeathMatchRandWeapon>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.DeathMatchRandWeapon> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as DeathMatchRandWeapon_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(DeathMatchRandWeapon_Array other) {
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
    public void MergeFrom(DeathMatchRandWeapon_Array other) {
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