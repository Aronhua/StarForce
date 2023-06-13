// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: xls_beans_weapongroupcard.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace D11.Pbeans {

  /// <summary>Holder for reflection information generated from xls_beans_weapongroupcard.proto</summary>
  public static partial class XlsBeansWeapongroupcardReflection {

    #region Descriptor
    /// <summary>File descriptor for xls_beans_weapongroupcard.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static XlsBeansWeapongroupcardReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch94bHNfYmVhbnNfd2VhcG9uZ3JvdXBjYXJkLnByb3RvEgpEMTEuUGJlYW5z",
            "IuoBCg9XZWFwb25Hcm91cENhcmQSCgoCaWQYASABKA0SDgoGY2FyZElkGAIg",
            "ASgNEg4KBm1vZGVJZBgDIAEoDRIQCghwb29sVHlwZRgEIAEoDRIOCgZwb29s",
            "SWQYBSABKA0SDgoGc3VpdElkGAYgASgNEhAKCHN1aXROYW1lGAcgASgJEg8K",
            "B3F1YWxpdHkYCCABKA0SEAoIZml4ZWROdW0YCSABKA0SDgoGd2VpZ2h0GAog",
            "ASgNEg8KB2l0ZW1JZHMYCyADKA0SDQoFcHJpY2UYDCABKA0SFAoMc2hvcFNo",
            "b3dJdGVtGA0gASgNIkMKFVdlYXBvbkdyb3VwQ2FyZF9BcnJheRIqCgVpdGVt",
            "cxgBIAMoCzIbLkQxMS5QYmVhbnMuV2VhcG9uR3JvdXBDYXJkYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.WeaponGroupCard), global::D11.Pbeans.WeaponGroupCard.Parser, new[]{ "Id", "CardId", "ModeId", "PoolType", "PoolId", "SuitId", "SuitName", "Quality", "FixedNum", "Weight", "ItemIds", "Price", "ShopShowItem" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::D11.Pbeans.WeaponGroupCard_Array), global::D11.Pbeans.WeaponGroupCard_Array.Parser, new[]{ "Items" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class WeaponGroupCard : pb::IMessage<WeaponGroupCard> {
    private static readonly pb::MessageParser<WeaponGroupCard> _parser = new pb::MessageParser<WeaponGroupCard>(() => new WeaponGroupCard());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<WeaponGroupCard> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansWeapongroupcardReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public WeaponGroupCard() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public WeaponGroupCard(WeaponGroupCard other) : this() {
      id_ = other.id_;
      cardId_ = other.cardId_;
      modeId_ = other.modeId_;
      poolType_ = other.poolType_;
      poolId_ = other.poolId_;
      suitId_ = other.suitId_;
      suitName_ = other.suitName_;
      quality_ = other.quality_;
      fixedNum_ = other.fixedNum_;
      weight_ = other.weight_;
      itemIds_ = other.itemIds_.Clone();
      price_ = other.price_;
      shopShowItem_ = other.shopShowItem_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public WeaponGroupCard Clone() {
      return new WeaponGroupCard(this);
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

    /// <summary>Field number for the "cardId" field.</summary>
    public const int CardIdFieldNumber = 2;
    private uint cardId_;
    /// <summary>
    /// 套装ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint CardId {
      get { return cardId_; }
      set {
        cardId_ = value;
      }
    }

    /// <summary>Field number for the "modeId" field.</summary>
    public const int ModeIdFieldNumber = 3;
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

    /// <summary>Field number for the "poolType" field.</summary>
    public const int PoolTypeFieldNumber = 4;
    private uint poolType_;
    /// <summary>
    /// 卡池类型 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint PoolType {
      get { return poolType_; }
      set {
        poolType_ = value;
      }
    }

    /// <summary>Field number for the "poolId" field.</summary>
    public const int PoolIdFieldNumber = 5;
    private uint poolId_;
    /// <summary>
    /// 卡池id 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint PoolId {
      get { return poolId_; }
      set {
        poolId_ = value;
      }
    }

    /// <summary>Field number for the "suitId" field.</summary>
    public const int SuitIdFieldNumber = 6;
    private uint suitId_;
    /// <summary>
    /// 套装ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint SuitId {
      get { return suitId_; }
      set {
        suitId_ = value;
      }
    }

    /// <summary>Field number for the "suitName" field.</summary>
    public const int SuitNameFieldNumber = 7;
    private string suitName_ = "";
    /// <summary>
    /// 套装名称 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string SuitName {
      get { return suitName_; }
      set {
        suitName_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "quality" field.</summary>
    public const int QualityFieldNumber = 8;
    private uint quality_;
    /// <summary>
    /// 卡牌品阶 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Quality {
      get { return quality_; }
      set {
        quality_ = value;
      }
    }

    /// <summary>Field number for the "fixedNum" field.</summary>
    public const int FixedNumFieldNumber = 9;
    private uint fixedNum_;
    /// <summary>
    /// 固定分配数 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint FixedNum {
      get { return fixedNum_; }
      set {
        fixedNum_ = value;
      }
    }

    /// <summary>Field number for the "weight" field.</summary>
    public const int WeightFieldNumber = 10;
    private uint weight_;
    /// <summary>
    /// 概率权重 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Weight {
      get { return weight_; }
      set {
        weight_ = value;
      }
    }

    /// <summary>Field number for the "itemIds" field.</summary>
    public const int ItemIdsFieldNumber = 11;
    private static readonly pb::FieldCodec<uint> _repeated_itemIds_codec
        = pb::FieldCodec.ForUInt32(90);
    private readonly pbc::RepeatedField<uint> itemIds_ = new pbc::RepeatedField<uint>();
    /// <summary>
    /// 主武器ID 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<uint> ItemIds {
      get { return itemIds_; }
    }

    /// <summary>Field number for the "price" field.</summary>
    public const int PriceFieldNumber = 12;
    private uint price_;
    /// <summary>
    /// 价格 
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint Price {
      get { return price_; }
      set {
        price_ = value;
      }
    }

    /// <summary>Field number for the "shopShowItem" field.</summary>
    public const int ShopShowItemFieldNumber = 13;
    private uint shopShowItem_;
    /// <summary>
    ///  
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint ShopShowItem {
      get { return shopShowItem_; }
      set {
        shopShowItem_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as WeaponGroupCard);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(WeaponGroupCard other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (CardId != other.CardId) return false;
      if (ModeId != other.ModeId) return false;
      if (PoolType != other.PoolType) return false;
      if (PoolId != other.PoolId) return false;
      if (SuitId != other.SuitId) return false;
      if (SuitName != other.SuitName) return false;
      if (Quality != other.Quality) return false;
      if (FixedNum != other.FixedNum) return false;
      if (Weight != other.Weight) return false;
      if(!itemIds_.Equals(other.itemIds_)) return false;
      if (Price != other.Price) return false;
      if (ShopShowItem != other.ShopShowItem) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0) hash ^= Id.GetHashCode();
      if (CardId != 0) hash ^= CardId.GetHashCode();
      if (ModeId != 0) hash ^= ModeId.GetHashCode();
      if (PoolType != 0) hash ^= PoolType.GetHashCode();
      if (PoolId != 0) hash ^= PoolId.GetHashCode();
      if (SuitId != 0) hash ^= SuitId.GetHashCode();
      if (SuitName.Length != 0) hash ^= SuitName.GetHashCode();
      if (Quality != 0) hash ^= Quality.GetHashCode();
      if (FixedNum != 0) hash ^= FixedNum.GetHashCode();
      if (Weight != 0) hash ^= Weight.GetHashCode();
      hash ^= itemIds_.GetHashCode();
      if (Price != 0) hash ^= Price.GetHashCode();
      if (ShopShowItem != 0) hash ^= ShopShowItem.GetHashCode();
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
      if (CardId != 0) {
        output.WriteRawTag(16);
        output.WriteUInt32(CardId);
      }
      if (ModeId != 0) {
        output.WriteRawTag(24);
        output.WriteUInt32(ModeId);
      }
      if (PoolType != 0) {
        output.WriteRawTag(32);
        output.WriteUInt32(PoolType);
      }
      if (PoolId != 0) {
        output.WriteRawTag(40);
        output.WriteUInt32(PoolId);
      }
      if (SuitId != 0) {
        output.WriteRawTag(48);
        output.WriteUInt32(SuitId);
      }
      if (SuitName.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(SuitName);
      }
      if (Quality != 0) {
        output.WriteRawTag(64);
        output.WriteUInt32(Quality);
      }
      if (FixedNum != 0) {
        output.WriteRawTag(72);
        output.WriteUInt32(FixedNum);
      }
      if (Weight != 0) {
        output.WriteRawTag(80);
        output.WriteUInt32(Weight);
      }
      itemIds_.WriteTo(output, _repeated_itemIds_codec);
      if (Price != 0) {
        output.WriteRawTag(96);
        output.WriteUInt32(Price);
      }
      if (ShopShowItem != 0) {
        output.WriteRawTag(104);
        output.WriteUInt32(ShopShowItem);
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
      if (CardId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(CardId);
      }
      if (ModeId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(ModeId);
      }
      if (PoolType != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(PoolType);
      }
      if (PoolId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(PoolId);
      }
      if (SuitId != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(SuitId);
      }
      if (SuitName.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(SuitName);
      }
      if (Quality != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Quality);
      }
      if (FixedNum != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(FixedNum);
      }
      if (Weight != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Weight);
      }
      size += itemIds_.CalculateSize(_repeated_itemIds_codec);
      if (Price != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Price);
      }
      if (ShopShowItem != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(ShopShowItem);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(WeaponGroupCard other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0) {
        Id = other.Id;
      }
      if (other.CardId != 0) {
        CardId = other.CardId;
      }
      if (other.ModeId != 0) {
        ModeId = other.ModeId;
      }
      if (other.PoolType != 0) {
        PoolType = other.PoolType;
      }
      if (other.PoolId != 0) {
        PoolId = other.PoolId;
      }
      if (other.SuitId != 0) {
        SuitId = other.SuitId;
      }
      if (other.SuitName.Length != 0) {
        SuitName = other.SuitName;
      }
      if (other.Quality != 0) {
        Quality = other.Quality;
      }
      if (other.FixedNum != 0) {
        FixedNum = other.FixedNum;
      }
      if (other.Weight != 0) {
        Weight = other.Weight;
      }
      itemIds_.Add(other.itemIds_);
      if (other.Price != 0) {
        Price = other.Price;
      }
      if (other.ShopShowItem != 0) {
        ShopShowItem = other.ShopShowItem;
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
            CardId = input.ReadUInt32();
            break;
          }
          case 24: {
            ModeId = input.ReadUInt32();
            break;
          }
          case 32: {
            PoolType = input.ReadUInt32();
            break;
          }
          case 40: {
            PoolId = input.ReadUInt32();
            break;
          }
          case 48: {
            SuitId = input.ReadUInt32();
            break;
          }
          case 58: {
            SuitName = input.ReadString();
            break;
          }
          case 64: {
            Quality = input.ReadUInt32();
            break;
          }
          case 72: {
            FixedNum = input.ReadUInt32();
            break;
          }
          case 80: {
            Weight = input.ReadUInt32();
            break;
          }
          case 90:
          case 88: {
            itemIds_.AddEntriesFrom(input, _repeated_itemIds_codec);
            break;
          }
          case 96: {
            Price = input.ReadUInt32();
            break;
          }
          case 104: {
            ShopShowItem = input.ReadUInt32();
            break;
          }
        }
      }
    }

  }

  public sealed partial class WeaponGroupCard_Array : pb::IMessage<WeaponGroupCard_Array> {
    private static readonly pb::MessageParser<WeaponGroupCard_Array> _parser = new pb::MessageParser<WeaponGroupCard_Array>(() => new WeaponGroupCard_Array());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<WeaponGroupCard_Array> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::D11.Pbeans.XlsBeansWeapongroupcardReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public WeaponGroupCard_Array() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public WeaponGroupCard_Array(WeaponGroupCard_Array other) : this() {
      items_ = other.items_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public WeaponGroupCard_Array Clone() {
      return new WeaponGroupCard_Array(this);
    }

    /// <summary>Field number for the "items" field.</summary>
    public const int ItemsFieldNumber = 1;
    private static readonly pb::FieldCodec<global::D11.Pbeans.WeaponGroupCard> _repeated_items_codec
        = pb::FieldCodec.ForMessage(10, global::D11.Pbeans.WeaponGroupCard.Parser);
    private readonly pbc::RepeatedField<global::D11.Pbeans.WeaponGroupCard> items_ = new pbc::RepeatedField<global::D11.Pbeans.WeaponGroupCard>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::RepeatedField<global::D11.Pbeans.WeaponGroupCard> Items {
      get { return items_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as WeaponGroupCard_Array);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(WeaponGroupCard_Array other) {
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
    public void MergeFrom(WeaponGroupCard_Array other) {
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