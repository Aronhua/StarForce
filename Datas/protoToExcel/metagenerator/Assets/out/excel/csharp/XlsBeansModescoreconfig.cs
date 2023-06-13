// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_modescoreconfig.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_modescoreconfig.proto</summary>
  public static partial class XlsBeansModescoreconfigReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_modescoreconfig.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansModescoreconfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch94bHNfYmVhbnNfbW9kZXNjb3JlY29uZmlnLnByb3RvEgpEMTEuUGJlYW5z",
            "IpgDCg9Nb2RlU2NvcmVDb25maWcSCgoCaWQYASABKA0SEQoJa2lsbFNjb3Jl",
            "GAIgASgFEhMKC2Fzc2lzdFNjb3JlGAMgASgFEhQKDHN1aWNpZGVTY29yZRgE",
            "IAEoBRIVCg1raWxsTWF0ZVNjb3JlGAUgASgFEhIKCnNldEM0U2NvcmUYBiAB",
            "KAUSEwoLdGVhckM0U2NvcmUYByABKAUSHAoUdGVhckM0V2l0aEVuZW15U2Nv",
            "cmUYCCABKAUSFgoOZXhwbG9kZUM0U2NvcmUYCSABKAUSFQoNcm91bmRXaW5T",
            "Y29yZRgKIAEoBRIUCgxiaWdIZWFkU2NvcmUYCyABKAUSEwoLb2NjdXB5U2Nv",
            "cmUYDCABKAUSHQoVYmV0cmFpZWRSb3VuZFdpblNjb3JlGA0gASgFEhoKEmpv",
            "a2VyTW9kZUtpbGxTY29yZRgOIAEoBRIUCgxyZXZlbmdlU2NvcmUYDyABKAUS",
            "GAoQa2lsbFRvcFJhbmtTY29yZRgQIAEoBRIYChB0b3BSYW5rS2lsbFNjb3Jl",
            "GBEgASgFIkMKFU1vZGVTY29yZUNvbmZpZ19BcnJheRIqCgVpdGVtcxgBIAMo",
            "CzIbLkQxMS5QYmVhbnMuTW9kZVNjb3JlQ29uZmlnYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.ModeScoreConfig), global::D11.Pbeans.ModeScoreConfig.Parser, new[]{ "Id", "KillScore", "AssistScore", "SuicideScore", "KillMateScore", "SetC4Score", "TearC4Score", "TearC4WithEnemyScore", "ExplodeC4Score", "RoundWinScore", "BigHeadScore", "OccupyScore", "BetraiedRoundWinScore", "JokerModeKillScore", "RevengeScore", "KillTopRankScore", "TopRankKillScore" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.ModeScoreConfig_Array), global::D11.Pbeans.ModeScoreConfig_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class ModeScoreConfig : pb::IMessage<ModeScoreConfig> {
    private static readonly pb::MessageParser<ModeScoreConfig> _parser = new pb::MessageParser<ModeScoreConfig>(() => new ModeScoreConfig());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<ModeScoreConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansModescoreconfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ModeScoreConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ModeScoreConfig(ModeScoreConfig other) : this() {
      id_ = other.id_;
      killScore_ = other.killScore_;
      assistScore_ = other.assistScore_;
      suicideScore_ = other.suicideScore_;
      killMateScore_ = other.killMateScore_;
      setC4Score_ = other.setC4Score_;
      tearC4Score_ = other.tearC4Score_;
      tearC4WithEnemyScore_ = other.tearC4WithEnemyScore_;
      explodeC4Score_ = other.explodeC4Score_;
      roundWinScore_ = other.roundWinScore_;
      bigHeadScore_ = other.bigHeadScore_;
      occupyScore_ = other.occupyScore_;
      betraiedRoundWinScore_ = other.betraiedRoundWinScore_;
      jokerModeKillScore_ = other.jokerModeKillScore_;
      revengeScore_ = other.revengeScore_;
      killTopRankScore_ = other.killTopRankScore_;
      topRankKillScore_ = other.topRankKillScore_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ModeScoreConfig Clone() {
      return new ModeScoreConfig(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private uint id_;
    /// <summary>
    /// 模式 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "killScore" field.</summary>
    public const int KillScoreFieldNumber = 2;
    private int killScore_;
    /// <summary>
    /// 杀人得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int KillScore {
      get { return killScore_; }
      set {
        killScore_ = value;
      }
    }

    /// <summary>Field number for the "assistScore" field.</summary>
    public const int AssistScoreFieldNumber = 3;
    private int assistScore_;
    /// <summary>
    /// 助攻得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int AssistScore {
      get { return assistScore_; }
      set {
        assistScore_ = value;
      }
    }

    /// <summary>Field number for the "suicideScore" field.</summary>
    public const int SuicideScoreFieldNumber = 4;
    private int suicideScore_;
    /// <summary>
    /// 自杀得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int SuicideScore {
      get { return suicideScore_; }
      set {
        suicideScore_ = value;
      }
    }

    /// <summary>Field number for the "killMateScore" field.</summary>
    public const int KillMateScoreFieldNumber = 5;
    private int killMateScore_;
    /// <summary>
    /// 杀队友得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int KillMateScore {
      get { return killMateScore_; }
      set {
        killMateScore_ = value;
      }
    }

    /// <summary>Field number for the "setC4Score" field.</summary>
    public const int SetC4ScoreFieldNumber = 6;
    private int setC4Score_;
    /// <summary>
    /// 下包得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int SetC4Score {
      get { return setC4Score_; }
      set {
        setC4Score_ = value;
      }
    }

    /// <summary>Field number for the "tearC4Score" field.</summary>
    public const int TearC4ScoreFieldNumber = 7;
    private int tearC4Score_;
    /// <summary>
    /// 拆包得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int TearC4Score {
      get { return tearC4Score_; }
      set {
        tearC4Score_ = value;
      }
    }

    /// <summary>Field number for the "tearC4WithEnemyScore" field.</summary>
    public const int TearC4WithEnemyScoreFieldNumber = 8;
    private int tearC4WithEnemyScore_;
    /// <summary>
    /// 拆包有敌额外加分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int TearC4WithEnemyScore {
      get { return tearC4WithEnemyScore_; }
      set {
        tearC4WithEnemyScore_ = value;
      }
    }

    /// <summary>Field number for the "explodeC4Score" field.</summary>
    public const int ExplodeC4ScoreFieldNumber = 9;
    private int explodeC4Score_;
    /// <summary>
    /// C4爆炸得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int ExplodeC4Score {
      get { return explodeC4Score_; }
      set {
        explodeC4Score_ = value;
      }
    }

    /// <summary>Field number for the "roundWinScore" field.</summary>
    public const int RoundWinScoreFieldNumber = 10;
    private int roundWinScore_;
    /// <summary>
    /// 回合胜利得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int RoundWinScore {
      get { return roundWinScore_; }
      set {
        roundWinScore_ = value;
      }
    }

    /// <summary>Field number for the "bigHeadScore" field.</summary>
    public const int BigHeadScoreFieldNumber = 11;
    private int bigHeadScore_;
    /// <summary>
    /// 变为巨人得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int BigHeadScore {
      get { return bigHeadScore_; }
      set {
        bigHeadScore_ = value;
      }
    }

    /// <summary>Field number for the "occupyScore" field.</summary>
    public const int OccupyScoreFieldNumber = 12;
    private int occupyScore_;
    /// <summary>
    /// 占领得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int OccupyScore {
      get { return occupyScore_; }
      set {
        occupyScore_ = value;
      }
    }

    /// <summary>Field number for the "betraiedRoundWinScore" field.</summary>
    public const int BetraiedRoundWinScoreFieldNumber = 13;
    private int betraiedRoundWinScore_;
    /// <summary>
    /// 叛变后回合胜利得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int BetraiedRoundWinScore {
      get { return betraiedRoundWinScore_; }
      set {
        betraiedRoundWinScore_ = value;
      }
    }

    /// <summary>Field number for the "jokerModeKillScore" field.</summary>
    public const int JokerModeKillScoreFieldNumber = 14;
    private int jokerModeKillScore_;
    /// <summary>
    /// 小丑模式杀人得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int JokerModeKillScore {
      get { return jokerModeKillScore_; }
      set {
        jokerModeKillScore_ = value;
      }
    }

    /// <summary>Field number for the "revengeScore" field.</summary>
    public const int RevengeScoreFieldNumber = 15;
    private int revengeScore_;
    /// <summary>
    /// 复仇得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int RevengeScore {
      get { return revengeScore_; }
      set {
        revengeScore_ = value;
      }
    }

    /// <summary>Field number for the "killTopRankScore" field.</summary>
    public const int KillTopRankScoreFieldNumber = 16;
    private int killTopRankScore_;
    /// <summary>
    /// 击杀前三得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int KillTopRankScore {
      get { return killTopRankScore_; }
      set {
        killTopRankScore_ = value;
      }
    }

    /// <summary>Field number for the "topRankKillScore" field.</summary>
    public const int TopRankKillScoreFieldNumber = 17;
    private int topRankKillScore_;
    /// <summary>
    /// 前三击杀得分 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int TopRankKillScore {
      get { return topRankKillScore_; }
      set {
        topRankKillScore_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as ModeScoreConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(ModeScoreConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (KillScore != other.KillScore) return false;
      if (AssistScore != other.AssistScore) return false;
      if (SuicideScore != other.SuicideScore) return false;
      if (KillMateScore != other.KillMateScore) return false;
      if (SetC4Score != other.SetC4Score) return false;
      if (TearC4Score != other.TearC4Score) return false;
      if (TearC4WithEnemyScore != other.TearC4WithEnemyScore) return false;
      if (ExplodeC4Score != other.ExplodeC4Score) return false;
      if (RoundWinScore != other.RoundWinScore) return false;
      if (BigHeadScore != other.BigHeadScore) return false;
      if (OccupyScore != other.OccupyScore) return false;
      if (BetraiedRoundWinScore != other.BetraiedRoundWinScore) return false;
      if (JokerModeKillScore != other.JokerModeKillScore) return false;
      if (RevengeScore != other.RevengeScore) return false;
      if (KillTopRankScore != other.KillTopRankScore) return false;
      if (TopRankKillScore != other.TopRankKillScore) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (KillScore != 0) hash ^= KillScore.GetHashCode();
      if (AssistScore != 0) hash ^= AssistScore.GetHashCode();
      if (SuicideScore != 0) hash ^= SuicideScore.GetHashCode();
      if (KillMateScore != 0) hash ^= KillMateScore.GetHashCode();
      if (SetC4Score != 0) hash ^= SetC4Score.GetHashCode();
      if (TearC4Score != 0) hash ^= TearC4Score.GetHashCode();
      if (TearC4WithEnemyScore != 0) hash ^= TearC4WithEnemyScore.GetHashCode();
      if (ExplodeC4Score != 0) hash ^= ExplodeC4Score.GetHashCode();
      if (RoundWinScore != 0) hash ^= RoundWinScore.GetHashCode();
      if (BigHeadScore != 0) hash ^= BigHeadScore.GetHashCode();
      if (OccupyScore != 0) hash ^= OccupyScore.GetHashCode();
      if (BetraiedRoundWinScore != 0) hash ^= BetraiedRoundWinScore.GetHashCode();
      if (JokerModeKillScore != 0) hash ^= JokerModeKillScore.GetHashCode();
      if (RevengeScore != 0) hash ^= RevengeScore.GetHashCode();
      if (KillTopRankScore != 0) hash ^= KillTopRankScore.GetHashCode();
      if (TopRankKillScore != 0) hash ^= TopRankKillScore.GetHashCode();
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
      if (KillScore != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(KillScore);
      }
      if (AssistScore != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(AssistScore);
      }
      if (SuicideScore != 0) {
        output.WriteRawTag(32);
        output.WriteInt32(SuicideScore);
      }
      if (KillMateScore != 0) {
        output.WriteRawTag(40);
        output.WriteInt32(KillMateScore);
      }
      if (SetC4Score != 0) {
        output.WriteRawTag(48);
        output.WriteInt32(SetC4Score);
      }
      if (TearC4Score != 0) {
        output.WriteRawTag(56);
        output.WriteInt32(TearC4Score);
      }
      if (TearC4WithEnemyScore != 0) {
        output.WriteRawTag(64);
        output.WriteInt32(TearC4WithEnemyScore);
      }
      if (ExplodeC4Score != 0) {
        output.WriteRawTag(72);
        output.WriteInt32(ExplodeC4Score);
      }
      if (RoundWinScore != 0) {
        output.WriteRawTag(80);
        output.WriteInt32(RoundWinScore);
      }
      if (BigHeadScore != 0) {
        output.WriteRawTag(88);
        output.WriteInt32(BigHeadScore);
      }
      if (OccupyScore != 0) {
        output.WriteRawTag(96);
        output.WriteInt32(OccupyScore);
      }
      if (BetraiedRoundWinScore != 0) {
        output.WriteRawTag(104);
        output.WriteInt32(BetraiedRoundWinScore);
      }
      if (JokerModeKillScore != 0) {
        output.WriteRawTag(112);
        output.WriteInt32(JokerModeKillScore);
      }
      if (RevengeScore != 0) {
        output.WriteRawTag(120);
        output.WriteInt32(RevengeScore);
      }
      if (KillTopRankScore != 0) {
        output.WriteRawTag(128, 1);
        output.WriteInt32(KillTopRankScore);
      }
      if (TopRankKillScore != 0) {
        output.WriteRawTag(136, 1);
        output.WriteInt32(TopRankKillScore);
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
      if (KillScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(KillScore);
      }
      if (AssistScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(AssistScore);
      }
      if (SuicideScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(SuicideScore);
      }
      if (KillMateScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(KillMateScore);
      }
      if (SetC4Score != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(SetC4Score);
      }
      if (TearC4Score != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(TearC4Score);
      }
      if (TearC4WithEnemyScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(TearC4WithEnemyScore);
      }
      if (ExplodeC4Score != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(ExplodeC4Score);
      }
      if (RoundWinScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(RoundWinScore);
      }
      if (BigHeadScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(BigHeadScore);
      }
      if (OccupyScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(OccupyScore);
      }
      if (BetraiedRoundWinScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(BetraiedRoundWinScore);
      }
      if (JokerModeKillScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(JokerModeKillScore);
      }
      if (RevengeScore != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(RevengeScore);
      }
      if (KillTopRankScore != 0) {
        size += 2 + pb::CodedOutputStream.ComputeInt32Size(KillTopRankScore);
      }
      if (TopRankKillScore != 0) {
        size += 2 + pb::CodedOutputStream.ComputeInt32Size(TopRankKillScore);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(ModeScoreConfig other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.KillScore != 0) {
        KillScore = other.KillScore;
      }
      if (other.AssistScore != 0) {
        AssistScore = other.AssistScore;
      }
      if (other.SuicideScore != 0) {
        SuicideScore = other.SuicideScore;
      }
      if (other.KillMateScore != 0) {
        KillMateScore = other.KillMateScore;
      }
      if (other.SetC4Score != 0) {
        SetC4Score = other.SetC4Score;
      }
      if (other.TearC4Score != 0) {
        TearC4Score = other.TearC4Score;
      }
      if (other.TearC4WithEnemyScore != 0) {
        TearC4WithEnemyScore = other.TearC4WithEnemyScore;
      }
      if (other.ExplodeC4Score != 0) {
        ExplodeC4Score = other.ExplodeC4Score;
      }
      if (other.RoundWinScore != 0) {
        RoundWinScore = other.RoundWinScore;
      }
      if (other.BigHeadScore != 0) {
        BigHeadScore = other.BigHeadScore;
      }
      if (other.OccupyScore != 0) {
        OccupyScore = other.OccupyScore;
      }
      if (other.BetraiedRoundWinScore != 0) {
        BetraiedRoundWinScore = other.BetraiedRoundWinScore;
      }
      if (other.JokerModeKillScore != 0) {
        JokerModeKillScore = other.JokerModeKillScore;
      }
      if (other.RevengeScore != 0) {
        RevengeScore = other.RevengeScore;
      }
      if (other.KillTopRankScore != 0) {
        KillTopRankScore = other.KillTopRankScore;
      }
      if (other.TopRankKillScore != 0) {
        TopRankKillScore = other.TopRankKillScore;
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
            KillScore = input.ReadInt32();
            break;
          }
          case 24: {
            AssistScore = input.ReadInt32();
            break;
          }
          case 32: {
            SuicideScore = input.ReadInt32();
            break;
          }
          case 40: {
            KillMateScore = input.ReadInt32();
            break;
          }
          case 48: {
            SetC4Score = input.ReadInt32();
            break;
          }
          case 56: {
            TearC4Score = input.ReadInt32();
            break;
          }
          case 64: {
            TearC4WithEnemyScore = input.ReadInt32();
            break;
          }
          case 72: {
            ExplodeC4Score = input.ReadInt32();
            break;
          }
          case 80: {
            RoundWinScore = input.ReadInt32();
            break;
          }
          case 88: {
            BigHeadScore = input.ReadInt32();
            break;
          }
          case 96: {
            OccupyScore = input.ReadInt32();
            break;
          }
          case 104: {
            BetraiedRoundWinScore = input.ReadInt32();
            break;
          }
          case 112: {
            JokerModeKillScore = input.ReadInt32();
            break;
          }
          case 120: {
            RevengeScore = input.ReadInt32();
            break;
          }
          case 128: {
            KillTopRankScore = input.ReadInt32();
            break;
          }
          case 136: {
            TopRankKillScore = input.ReadInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class ModeScoreConfig_Array : pb::IMessage<ModeScoreConfig_Array> {
    private static readonly pb::MessageParser<ModeScoreConfig_Array> _parser = new pb::MessageParser<ModeScoreConfig_Array>(() => new ModeScoreConfig_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<ModeScoreConfig_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansModescoreconfigReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ModeScoreConfig_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ModeScoreConfig_Array(ModeScoreConfig_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ModeScoreConfig_Array Clone() {
      return new ModeScoreConfig_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.ModeScoreConfig> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.ModeScoreConfig.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.ModeScoreConfig> items_ = new pbc::RepeatedField<global::D11.Pbeans.ModeScoreConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.ModeScoreConfig> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as ModeScoreConfig_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(ModeScoreConfig_Array other) {
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
    public void MergeFrom(ModeScoreConfig_Array other) {
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