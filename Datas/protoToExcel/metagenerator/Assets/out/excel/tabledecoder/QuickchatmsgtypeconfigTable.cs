using System;
using System.Collections.Generic;
namespace D11.Pbeans
{
	public class QuickchatmsgtypeconfigTable : BaseTable
	{
		private Dictionary<uint, QuickChatMsgTypeConfig> quickchatmsgtypeconfig_map = new Dictionary<uint, QuickChatMsgTypeConfig>();

		public override void LoadConfig(byte[] buffer, int offset, int length)
		{
			try
			{
				QuickChatMsgTypeConfig_Array quickchatmsgtypeconfig_array = QuickChatMsgTypeConfig_Array.Parser.ParseFrom(buffer, offset, length);
				foreach (var item in quickchatmsgtypeconfig_array.Items)
				{
					quickchatmsgtypeconfig_map.Add(item.Id, item);
				}
			}
			catch (Exception ex)
			{
				string errorMsg = "QuickChatMsgTypeConfig_Array.LoadConfig Error\n{0}";
				throw new Exception(string.Format(errorMsg, ex.ToString()));
			}
		}

		public Dictionary<uint, QuickChatMsgTypeConfig> GetTable()
		{
			return quickchatmsgtypeconfig_map;
		}

		public QuickChatMsgTypeConfig GetRecorder(uint key)
		{
			if (!quickchatmsgtypeconfig_map.ContainsKey(key))
			{
				return null;
			}
			return quickchatmsgtypeconfig_map[key];
		}

	}
}