--[[
* @file:   GMInstruction
* @brief:  这个文件是通过工具自动生成的，建议不要手动修改
]]--

local GMInstructionTable = 
{
	[10101] = {clientOrServer = 1, defaultParam = '1', id = 10101, instruction = 'allinvincible', name = '所有人无敌模式开关', sheet = 1, showPriority = 96, type = 1}, 
	[10201] = {clientOrServer = 1, defaultParam = '', id = 10201, instruction = 'suicide', name = ' 原地去世', sheet = 1, showPriority = 97, type = 2}, 
	[10202] = {clientOrServer = 2, defaultParam = '', id = 10202, instruction = 'resetinneruisafearea', name = '重置局内UI安全区设置', sheet = 1, showPriority = 0, type = 2}, 
	[10203] = {clientOrServer = 1, defaultParam = '', id = 10203, instruction = 'tryweapon', name = '换一把配置表武器', sheet = 1, showPriority = 0, type = 2}, 
	[10204] = {clientOrServer = 1, defaultParam = '', id = 10204, instruction = 'tryallweapon', name = '测试所有配置武器', sheet = 1, showPriority = 0, type = 2}, 
	[10205] = {clientOrServer = 2, defaultParam = '', id = 10205, instruction = 'triggerrollback', name = '触发一次rollback', sheet = 1, showPriority = 96, type = 2}, 
	[10301] = {clientOrServer = 1, defaultParam = '16908289 16908289 50 111040005', id = 10301, instruction = 'hurtonepro', name = '对某人造成x伤害', sheet = 1, showPriority = 98, type = 3}, 
	[10302] = {clientOrServer = 1, defaultParam = '2', id = 10302, instruction = 'switchgm', name = 'GM模式开关', sheet = 1, showPriority = 99, type = 3}, 
	[10303] = {clientOrServer = 1, defaultParam = '10', id = 10303, instruction = 'addtime', name = '加时间', sheet = 1, showPriority = 0, type = 3}, 
	[10304] = {clientOrServer = 2, defaultParam = '100', id = 10304, instruction = 'setinneruisafearea', name = '设置局内UI安全区', sheet = 1, showPriority = 0, type = 3}, 
	[10305] = {clientOrServer = 1, defaultParam = '26', id = 10305, instruction = 'addtalent', name = '添加天赋', sheet = 1, showPriority = 0, type = 3}, 
	[10306] = {clientOrServer = 1, defaultParam = '101003', id = 10306, instruction = 'addbuff', name = '添加buff', sheet = 1, showPriority = 0, type = 3}, 
	[10307] = {clientOrServer = 1, defaultParam = '', id = 10307, instruction = 'killallmonster', name = '清怪', sheet = 1, showPriority = 0, type = 3}, 
	[10308] = {clientOrServer = 1, defaultParam = '100001', id = 10308, instruction = 'addskill', name = '添加技能', sheet = 1, showPriority = 0, type = 3}, 
	[10309] = {clientOrServer = 3, defaultParam = '1005001 10', id = 10309, instruction = 'additem', name = '添加道具', sheet = 1, showPriority = 95, type = 3}, 
	[10310] = {clientOrServer = 2, defaultParam = '1', id = 10310, instruction = 'setframedebuggercapture', name = '捕捉FrameDebugger数据', sheet = 1, showPriority = 99, type = 3}, 
	[10311] = {clientOrServer = 3, defaultParam = '0', id = 10311, instruction = 'setplayerprofession', name = '设置玩家职业', sheet = 1, showPriority = 0, type = 3}, 
	[10312] = {clientOrServer = 1, defaultParam = '', id = 10312, instruction = 'nextspawnpoint', name = '传送到下一出生点', sheet = 1, showPriority = 0, type = 3}, 
	[10313] = {clientOrServer = 2, defaultParam = '1', id = 10313, instruction = 'setsvcdatacapture', name = '捕捉shader.createGPUprogram数据', sheet = 1, showPriority = 0, type = 3}, 
	[20101] = {clientOrServer = 1, defaultParam = '1', id = 20101, instruction = 'friendlydamage', name = '关闭/开启友军伤害', sheet = 2, showPriority = 0, type = 1}, 
	[20102] = {clientOrServer = 2, defaultParam = '0', id = 20102, instruction = 'switchspread', name = '关闭/开启散发', sheet = 2, showPriority = 0, type = 1}, 
	[20103] = {clientOrServer = 2, defaultParam = '0', id = 20103, instruction = 'switchrecoil', name = '关闭/开启后坐力', sheet = 2, showPriority = 0, type = 1}, 
	[20104] = {clientOrServer = 2, defaultParam = '1', id = 20104, instruction = 'switchspreadshow', name = '关闭/显示散发圈', sheet = 2, showPriority = 0, type = 1}, 
	[20105] = {clientOrServer = 2, defaultParam = '1', id = 20105, instruction = 'switchshowprojectiletrail', name = '关闭/显示投掷物轨迹线', sheet = 2, showPriority = 0, type = 1}, 
	[20106] = {clientOrServer = 2, defaultParam = '1', id = 20106, instruction = 'switchshow3dui', name = '关闭/显示3dUI', sheet = 2, showPriority = 0, type = 1}, 
	[20201] = {clientOrServer = 1, defaultParam = '', id = 20201, instruction = 'throwknife', name = '丢刀', sheet = 2, showPriority = 0, type = 2}, 
	[20202] = {clientOrServer = 1, defaultParam = '', id = 20202, instruction = 'swapcamp', name = '切换阵营', sheet = 2, showPriority = 0, type = 2}, 
	[20203] = {clientOrServer = 2, defaultParam = '', id = 20203, instruction = 'exitinnergametotestds', name = '退出单局至TestDS', sheet = 2, showPriority = 0, type = 2}, 
	[20204] = {clientOrServer = 2, defaultParam = '', id = 20204, instruction = 'exitinnergametohall', name = '退出单局至大厅', sheet = 2, showPriority = 0, type = 2}, 
	[20205] = {clientOrServer = 3, defaultParam = '', id = 20205, instruction = 'infinitecarriedammo', name = '无限备弹', sheet = 2, showPriority = 0, type = 2}, 
	[20215] = {clientOrServer = 1, defaultParam = '', id = 20215, instruction = 'resetinteract', name = '重置交互物', sheet = 2, showPriority = 97, type = 2}, 
	[20221] = {clientOrServer = 2, defaultParam = '1', id = 20221, instruction = 'closetitle', name = '发行要求关闭title', sheet = 2, showPriority = 0, type = 2}, 
	[20301] = {clientOrServer = 1, defaultParam = '6', id = 20301, instruction = 'SetSwapTeamsRound', name = '设置切换阵营回合数', sheet = 2, showPriority = 0, type = 3}, 
	[20302] = {clientOrServer = 1, defaultParam = '29654', id = 20302, instruction = 'allsetmoney', name = '设置全员金钱为x', sheet = 2, showPriority = 99, type = 3}, 
	[20303] = {clientOrServer = 1, defaultParam = '10', id = 20303, instruction = 'respawninvincible', name = '设置复活无敌时间为x秒', sheet = 2, showPriority = 0, type = 3}, 
	[20304] = {clientOrServer = 1, defaultParam = '1', id = 20304, instruction = 'allycollider', name = '关闭/开启队友碰撞', sheet = 2, showPriority = 0, type = 3}, 
	[20305] = {clientOrServer = 1, defaultParam = '5 0', id = 20305, instruction = 'advanceendround', name = '关闭/开启提前胜利结束回合', sheet = 2, showPriority = 97, type = 3}, 
	[20306] = {clientOrServer = 1, defaultParam = '5', id = 20306, instruction = 'advanceendgame', name = '关闭/开启提前胜利结束比赛', sheet = 2, showPriority = 96, type = 3}, 
	[20307] = {clientOrServer = 1, defaultParam = '99999999', id = 20307, instruction = 'maxhp', name = '将自己血量上限设置为x', sheet = 2, showPriority = 98, type = 3}, 
	[20308] = {clientOrServer = 1, defaultParam = '', id = 20308, instruction = 'buyunlimit', name = '全图购买', sheet = 2, showPriority = 0, type = 3}, 
	[20309] = {clientOrServer = 1, defaultParam = '111030001', id = 20309, instruction = 'setfunctionweapon', name = '生成附加弹幕和武器词条的武器', sheet = 2, showPriority = 100, type = 3}, 
	[20310] = {clientOrServer = 1, defaultParam = '111030001', id = 20310, instruction = 'setgunbuffweapon', name = '生成附加武器词条的武器', sheet = 2, showPriority = 100, type = 3}, 
	[20311] = {clientOrServer = 1, defaultParam = '1|30000', id = 20311, instruction = 'allsetmoney', name = '随机设置全员金钱为x', sheet = 2, showPriority = 0, type = 3}, 
	[20312] = {clientOrServer = 1, defaultParam = '111070002 4001|4002', id = 20312, instruction = 'weaponaddability', name = '设置武器技能', sheet = 2, showPriority = 0, type = 3}, 
	[20313] = {clientOrServer = 3, defaultParam = '', id = 20313, instruction = 'kickoutpawn', name = '踢出玩家', sheet = 2, showPriority = 95, type = 3}, 
	[20314] = {clientOrServer = 3, defaultParam = '', id = 20314, instruction = 'killtower', name = '推一座塔', sheet = 2, showPriority = 95, type = 3}, 
	[20315] = {clientOrServer = 2, defaultParam = '200 4', id = 20315, instruction = 'netlatencytest', name = '开始测试网络延迟', sheet = 2, showPriority = 0, type = 3}, 
	[20316] = {clientOrServer = 1, defaultParam = '0 10', id = 20316, instruction = 'br_setpoisoncircle', name = '设置毒圈', sheet = 2, showPriority = 0, type = 3}, 
	[20317] = {clientOrServer = 1, defaultParam = '0', id = 20317, instruction = 'br_immunepoisoncircledamage', name = '是否免疫毒圈伤害', sheet = 2, showPriority = 0, type = 3}, 
	[20319] = {clientOrServer = 1, defaultParam = '90002 500', id = 20319, instruction = 'br_additem', name = 'BR背包加道具', sheet = 2, showPriority = 95, type = 3}, 
	[20320] = {clientOrServer = 1, defaultParam = '1', id = 20320, instruction = 'br_pausepoisoncircle', name = 'BR毒圈暂停', sheet = 2, showPriority = 0, type = 3}, 
	[20322] = {clientOrServer = 1, defaultParam = '3,100,3,-561,750,1004,1063,750,-428', id = 20322, instruction = 'br_setairline', name = '设置航线', sheet = 2, showPriority = 0, type = 3}, 
	[20323] = {clientOrServer = 3, defaultParam = '0', id = 20323, instruction = 'br_addbrweaponbuff', name = 'BR武器BUFF组', sheet = 2, showPriority = 0, type = 3}, 
	[30101] = {clientOrServer = 1, defaultParam = '1', id = 30101, instruction = 'infiniteprojectile', name = '无限投掷物', sheet = 3, showPriority = 0, type = 1}, 
	[30102] = {clientOrServer = 2, defaultParam = '1', id = 30102, instruction = 'switchshowbottitleview', name = '开启/关闭BOT头顶护甲血量状态', sheet = 3, showPriority = 0, type = 1}, 
	[30201] = {clientOrServer = 1, defaultParam = '', id = 30201, instruction = 'lastprojectile', name = '重新丢出上一个投掷物', sheet = 3, showPriority = 0, type = 2}, 
	[30202] = {clientOrServer = 1, defaultParam = '', id = 30202, instruction = 'allkickbot', name = '踢出所有电脑', sheet = 3, showPriority = 93, type = 2}, 
	[30203] = {clientOrServer = 1, defaultParam = '', id = 30203, instruction = 'allkillbot', name = '处死所有电脑', sheet = 3, showPriority = 92, type = 2}, 
	[30204] = {clientOrServer = 1, defaultParam = '', id = 30204, instruction = 'kickctbot', name = '踢出一名CT', sheet = 3, showPriority = 95, type = 2}, 
	[30205] = {clientOrServer = 1, defaultParam = '', id = 30205, instruction = 'kicktbot', name = '踢出一名T', sheet = 3, showPriority = 94, type = 2}, 
	[30206] = {clientOrServer = 1, defaultParam = '', id = 30206, instruction = 'testmonster', name = '怪物定身且血量高', sheet = 3, showPriority = 95, type = 2}, 
	[30301] = {clientOrServer = 1, defaultParam = '111030001', id = 30301, instruction = 'addweapon', name = '生成/给予武器 填入武器id', sheet = 3, showPriority = 98, type = 3}, 
	[30302] = {clientOrServer = 1, defaultParam = '1', id = 30302, instruction = 'allbotstopmove', name = '开启/关闭让bot原地站着不动', sheet = 3, showPriority = 99, type = 3}, 
	[30303] = {clientOrServer = 1, defaultParam = '0', id = 30303, instruction = 'addctbot', name = '增加一名CT', sheet = 3, showPriority = 97, type = 3}, 
	[30304] = {clientOrServer = 1, defaultParam = '0', id = 30304, instruction = 'addtbot', name = '增加一名T', sheet = 3, showPriority = 96, type = 3}, 
	[30305] = {clientOrServer = 1, defaultParam = '111020001', id = 30305, instruction = 'dropweapon', name = '掉落枪械', sheet = 3, showPriority = 0, type = 3}, 
	[30306] = {clientOrServer = 1, defaultParam = '111020001', id = 30306, instruction = 'allbotweapon', name = 'bot换武器', sheet = 3, showPriority = 0, type = 3}, 
	[30307] = {clientOrServer = 1, defaultParam = '1', id = 30307, instruction = 'botlevel', name = 'AI难度', sheet = 3, showPriority = 0, type = 3}, 
	[30308] = {clientOrServer = 2, defaultParam = '16908290', id = 30308, instruction = 'moveplayertocamp', name = '将玩家位置移到本正营内', sheet = 3, showPriority = 0, type = 3}, 
	[30309] = {clientOrServer = 1, defaultParam = '16908290 0 0 0', id = 30309, instruction = 'moveplayer', name = '将玩家移到某个坐标', sheet = 3, showPriority = 0, type = 3}, 
	[30310] = {clientOrServer = 1, defaultParam = '16908290 1', id = 30310, instruction = 'bigheadgrade', name = '设置玩家大头等级', sheet = 3, showPriority = 0, type = 3}, 
	[30311] = {clientOrServer = 1, defaultParam = '16908289', id = 30311, instruction = 'jokerreassemble', name = '小丑模式变换当前阵营', sheet = 3, showPriority = 0, type = 3}, 
	[30312] = {clientOrServer = 1, defaultParam = '6 1', id = 30312, instruction = 'addchicken', name = '加鸡', sheet = 3, showPriority = 0, type = 3}, 
	[30313] = {clientOrServer = 1, defaultParam = '1001 1', id = 30313, instruction = 'addzombie', name = '加僵尸', sheet = 3, showPriority = 0, type = 3}, 
	[30314] = {clientOrServer = 2, defaultParam = '', id = 30314, instruction = 'showentityid', name = '玩家名字显示EntityId与否', sheet = 3, showPriority = 0, type = 3}, 
	[30315] = {clientOrServer = 1, defaultParam = '111030001', id = 30315, instruction = 'addweaponwithskin', name = '生成/给予皮肤武器 填入武器id', sheet = 3, showPriority = 98, type = 3}, 
	[30316] = {clientOrServer = 3, defaultParam = '1', id = 30316, instruction = 'replaceai', name = '顶替AI', sheet = 3, showPriority = 0, type = 3}, 
	[30317] = {clientOrServer = 2, defaultParam = '17629205', id = 30317, instruction = 'reinitializeentity', name = '本地RinitEntity', sheet = 3, showPriority = 0, type = 3}, 
	[30318] = {clientOrServer = 2, defaultParam = '1', id = 30318, instruction = 'patroltestlatency', name = '测试同步延迟', sheet = 3, showPriority = 0, type = 3}
}
return GMInstructionTable