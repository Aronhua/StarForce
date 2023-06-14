//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------
using Bright.Serialization;
using System.Collections.Generic;


namespace cfg.luban
{
public sealed partial class ItemExchange :  Bright.Config.BeanBase 
{
    public ItemExchange(ByteBuf _buf) 
    {
        Id = _buf.ReadInt();
        Num = _buf.ReadInt();
        PostInit();
    }

    public static ItemExchange DeserializeItemExchange(ByteBuf _buf)
    {
        return new luban.ItemExchange(_buf);
    }

    /// <summary>
    /// 道具id
    /// </summary>
    public int Id { get; private set; }
    /// <summary>
    /// 道具数量
    /// </summary>
    public int Num { get; private set; }

    public const int __ID__ = -1076242050;
    public override int GetTypeId() => __ID__;

    public  void Resolve(Dictionary<string, object> _tables)
    {
        PostResolve();
    }

    public  void TranslateText(System.Func<string, string, string> translator)
    {
    }

    public override string ToString()
    {
        return "{ "
        + "Id:" + Id + ","
        + "Num:" + Num + ","
        + "}";
    }
    
    partial void PostInit();
    partial void PostResolve();
}

}