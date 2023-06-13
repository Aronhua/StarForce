// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: BossMonsterData_HeavyPunch.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pjson {

  /// <summary>Holder for reflection information generated from BossMonsterData_HeavyPunch.proto</summary>
  public static partial class BossMonsterDataHeavyPunchReflection {

    #region Descriptor
    /// <summary>File descriptor for BossMonsterData_HeavyPunch.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static BossMonsterDataHeavyPunchReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiBCb3NzTW9uc3RlckRhdGFfSGVhdnlQdW5jaC5wcm90bxIJRDExLlBqc29u",
            "IqUCChpCb3NzTW9uc3RlckRhdGFfSGVhdnlQdW5jaBImCh5EaXN0YW5jZU1p",
            "bkxpbWl0Rm9yQ29tZm9ydFpvbWUYASABKAUSJgoeRGlzdGFuY2VNYXhMaW1p",
            "dEZvckNvbWZvcnRab21lGAIgASgFEiQKHFVzZVNraWxsVGltZXNGb3JTd2l0",
            "Y2hUYXJnZXQYAyABKAUSHgoWQm9ybkF0dGFja0Nvb2xEb3duVGltZRgEIAEo",
            "AhITCgtTa2lsbElkTGlzdBgFIAEoCRIYChBDb250aW51ZU1vdmVUaW1lGAYg",
            "ASgCEhAKCElkbGVUaW1lGAcgASgCEhkKEVNraWxsQ29vbERvd25UaW1lGAgg",
            "ASgCEhUKDUFuaW1hdGlvblRpbWUYCSABKAJiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pjson.BossMonsterData_HeavyPunch), global::D11.Pjson.BossMonsterData_HeavyPunch.Parser, new[]{ "DistanceMinLimitForComfortZome", "DistanceMaxLimitForComfortZome", "UseSkillTimesForSwitchTarget", "BornAttackCoolDownTime", "SkillIdList", "ContinueMoveTime", "IdleTime", "SkillCoolDownTime", "AnimationTime" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class BossMonsterData_HeavyPunch : pb::IMessage<BossMonsterData_HeavyPunch> {
    private static readonly pb::MessageParser<BossMonsterData_HeavyPunch> _parser = new pb::MessageParser<BossMonsterData_HeavyPunch>(() => new BossMonsterData_HeavyPunch());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<BossMonsterData_HeavyPunch> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pjson.BossMonsterDataHeavyPunchReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BossMonsterData_HeavyPunch() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BossMonsterData_HeavyPunch(BossMonsterData_HeavyPunch other) : this() {
      distanceMinLimitForComfortZome_ = other.distanceMinLimitForComfortZome_;
      distanceMaxLimitForComfortZome_ = other.distanceMaxLimitForComfortZome_;
      useSkillTimesForSwitchTarget_ = other.useSkillTimesForSwitchTarget_;
      bornAttackCoolDownTime_ = other.bornAttackCoolDownTime_;
      skillIdList_ = other.skillIdList_;
      continueMoveTime_ = other.continueMoveTime_;
      idleTime_ = other.idleTime_;
      skillCoolDownTime_ = other.skillCoolDownTime_;
      animationTime_ = other.animationTime_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public BossMonsterData_HeavyPunch Clone() {
      return new BossMonsterData_HeavyPunch(this);
    }

    /// <summary>Field number for the "DistanceMinLimitForComfortZome" field.</summary>
    public const int DistanceMinLimitForComfortZomeFieldNumber = 1;
    private int distanceMinLimitForComfortZome_;
    /// <summary>
    ///	舒适区最小距离限制
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int DistanceMinLimitForComfortZome {
      get { return distanceMinLimitForComfortZome_; }
      set {
        distanceMinLimitForComfortZome_ = value;
      }
    }

    /// <summary>Field number for the "DistanceMaxLimitForComfortZome" field.</summary>
    public const int DistanceMaxLimitForComfortZomeFieldNumber = 2;
    private int distanceMaxLimitForComfortZome_;
    /// <summary>
    ///  舒适区最大距离限制
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int DistanceMaxLimitForComfortZome {
      get { return distanceMaxLimitForComfortZome_; }
      set {
        distanceMaxLimitForComfortZome_ = value;
      }
    }

    /// <summary>Field number for the "UseSkillTimesForSwitchTarget" field.</summary>
    public const int UseSkillTimesForSwitchTargetFieldNumber = 3;
    private int useSkillTimesForSwitchTarget_;
    /// <summary>
    ///	使用X次技能后切换目标
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int UseSkillTimesForSwitchTarget {
      get { return useSkillTimesForSwitchTarget_; }
      set {
        useSkillTimesForSwitchTarget_ = value;
      }
    }

    /// <summary>Field number for the "BornAttackCoolDownTime" field.</summary>
    public const int BornAttackCoolDownTimeFieldNumber = 4;
    private float bornAttackCoolDownTime_;
    /// <summary>
    ///	出生后冷却时间
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public float BornAttackCoolDownTime {
      get { return bornAttackCoolDownTime_; }
      set {
        bornAttackCoolDownTime_ = value;
      }
    }

    /// <summary>Field number for the "SkillIdList" field.</summary>
    public const int SkillIdListFieldNumber = 5;
    private string skillIdList_ = "";
    /// <summary>
    ///	技能列表
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string SkillIdList {
      get { return skillIdList_; }
      set {
        skillIdList_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "ContinueMoveTime" field.</summary>
    public const int ContinueMoveTimeFieldNumber = 6;
    private float continueMoveTime_;
    /// <summary>
    /// 	移动时间
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public float ContinueMoveTime {
      get { return continueMoveTime_; }
      set {
        continueMoveTime_ = value;
      }
    }

    /// <summary>Field number for the "IdleTime" field.</summary>
    public const int IdleTimeFieldNumber = 7;
    private float idleTime_;
    /// <summary>
    ///	休息时间
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public float IdleTime {
      get { return idleTime_; }
      set {
        idleTime_ = value;
      }
    }

    /// <summary>Field number for the "SkillCoolDownTime" field.</summary>
    public const int SkillCoolDownTimeFieldNumber = 8;
    private float skillCoolDownTime_;
    /// <summary>
    ///	技能CD
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public float SkillCoolDownTime {
      get { return skillCoolDownTime_; }
      set {
        skillCoolDownTime_ = value;
      }
    }

    /// <summary>Field number for the "AnimationTime" field.</summary>
    public const int AnimationTimeFieldNumber = 9;
    private float animationTime_;
    /// <summary>
    ///	出场动画时长
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public float AnimationTime {
      get { return animationTime_; }
      set {
        animationTime_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as BossMonsterData_HeavyPunch);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(BossMonsterData_HeavyPunch other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (DistanceMinLimitForComfortZome != other.DistanceMinLimitForComfortZome) return false;
      if (DistanceMaxLimitForComfortZome != other.DistanceMaxLimitForComfortZome) return false;
      if (UseSkillTimesForSwitchTarget != other.UseSkillTimesForSwitchTarget) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(BornAttackCoolDownTime, other.BornAttackCoolDownTime)) return false;
      if (SkillIdList != other.SkillIdList) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(ContinueMoveTime, other.ContinueMoveTime)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(IdleTime, other.IdleTime)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(SkillCoolDownTime, other.SkillCoolDownTime)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(AnimationTime, other.AnimationTime)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (DistanceMinLimitForComfortZome != 0) hash ^= DistanceMinLimitForComfortZome.GetHashCode();
      if (DistanceMaxLimitForComfortZome != 0) hash ^= DistanceMaxLimitForComfortZome.GetHashCode();
      if (UseSkillTimesForSwitchTarget != 0) hash ^= UseSkillTimesForSwitchTarget.GetHashCode();
      if (BornAttackCoolDownTime != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(BornAttackCoolDownTime);
      if (SkillIdList.Length != 0) hash ^= SkillIdList.GetHashCode();
      if (ContinueMoveTime != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(ContinueMoveTime);
      if (IdleTime != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(IdleTime);
      if (SkillCoolDownTime != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(SkillCoolDownTime);
      if (AnimationTime != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(AnimationTime);
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
      if (DistanceMinLimitForComfortZome != 0) {
        output.WriteRawTag(8);
        output.WriteInt32(DistanceMinLimitForComfortZome);
      }
      if (DistanceMaxLimitForComfortZome != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(DistanceMaxLimitForComfortZome);
      }
      if (UseSkillTimesForSwitchTarget != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(UseSkillTimesForSwitchTarget);
      }
      if (BornAttackCoolDownTime != 0F) {
        output.WriteRawTag(37);
        output.WriteFloat(BornAttackCoolDownTime);
      }
      if (SkillIdList.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(SkillIdList);
      }
      if (ContinueMoveTime != 0F) {
        output.WriteRawTag(53);
        output.WriteFloat(ContinueMoveTime);
      }
      if (IdleTime != 0F) {
        output.WriteRawTag(61);
        output.WriteFloat(IdleTime);
      }
      if (SkillCoolDownTime != 0F) {
        output.WriteRawTag(69);
        output.WriteFloat(SkillCoolDownTime);
      }
      if (AnimationTime != 0F) {
        output.WriteRawTag(77);
        output.WriteFloat(AnimationTime);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (DistanceMinLimitForComfortZome != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(DistanceMinLimitForComfortZome);
      }
      if (DistanceMaxLimitForComfortZome != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(DistanceMaxLimitForComfortZome);
      }
      if (UseSkillTimesForSwitchTarget != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(UseSkillTimesForSwitchTarget);
      }
      if (BornAttackCoolDownTime != 0F) {
        size += 1 + 4;
      }
      if (SkillIdList.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(SkillIdList);
      }
      if (ContinueMoveTime != 0F) {
        size += 1 + 4;
      }
      if (IdleTime != 0F) {
        size += 1 + 4;
      }
      if (SkillCoolDownTime != 0F) {
        size += 1 + 4;
      }
      if (AnimationTime != 0F) {
        size += 1 + 4;
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(BossMonsterData_HeavyPunch other) {
      if (other == null) {
        return;
      }
      if (other.DistanceMinLimitForComfortZome != 0) {
        DistanceMinLimitForComfortZome = other.DistanceMinLimitForComfortZome;
      }
      if (other.DistanceMaxLimitForComfortZome != 0) {
        DistanceMaxLimitForComfortZome = other.DistanceMaxLimitForComfortZome;
      }
      if (other.UseSkillTimesForSwitchTarget != 0) {
        UseSkillTimesForSwitchTarget = other.UseSkillTimesForSwitchTarget;
      }
      if (other.BornAttackCoolDownTime != 0F) {
        BornAttackCoolDownTime = other.BornAttackCoolDownTime;
      }
      if (other.SkillIdList.Length != 0) {
        SkillIdList = other.SkillIdList;
      }
      if (other.ContinueMoveTime != 0F) {
        ContinueMoveTime = other.ContinueMoveTime;
      }
      if (other.IdleTime != 0F) {
        IdleTime = other.IdleTime;
      }
      if (other.SkillCoolDownTime != 0F) {
        SkillCoolDownTime = other.SkillCoolDownTime;
      }
      if (other.AnimationTime != 0F) {
        AnimationTime = other.AnimationTime;
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
            DistanceMinLimitForComfortZome = input.ReadInt32();
            break;
          }
          case 16: {
            DistanceMaxLimitForComfortZome = input.ReadInt32();
            break;
          }
          case 24: {
            UseSkillTimesForSwitchTarget = input.ReadInt32();
            break;
          }
          case 37: {
            BornAttackCoolDownTime = input.ReadFloat();
            break;
          }
          case 42: {
            SkillIdList = input.ReadString();
            break;
          }
          case 53: {
            ContinueMoveTime = input.ReadFloat();
            break;
          }
          case 61: {
            IdleTime = input.ReadFloat();
            break;
          }
          case 69: {
            SkillCoolDownTime = input.ReadFloat();
            break;
          }
          case 77: {
            AnimationTime = input.ReadFloat();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code