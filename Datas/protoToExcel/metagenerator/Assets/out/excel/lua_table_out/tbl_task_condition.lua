--[[
* @file:   TaskCondition
* @brief:  这个文件是通过工具自动生成的，建议不要手动修改
]]--

local TaskConditionTable = 
{
	["battleFirstKill"] = {condEvent = 'Gaming', id = 'battleFirstKill', processFlag = 0}, 
	["winCount"] = {condEvent = 'Gaming', id = 'winCount', processFlag = 1}, 
	["joinCount"] = {condEvent = 'Gaming', id = 'joinCount', processFlag = 1}, 
	["gameTime"] = {condEvent = 'Gaming', id = 'gameTime', processFlag = 1}, 
	["killCount"] = {condEvent = 'Gaming', id = 'killCount', processFlag = 0}, 
	["totalKillCount"] = {condEvent = 'Gaming', id = 'totalKillCount', processFlag = 1}, 
	["damage"] = {condEvent = 'Gaming', id = 'damage', processFlag = 0}, 
	["totalDamage"] = {condEvent = 'Gaming', id = 'totalDamage', processFlag = 1}, 
	["limitLogin"] = {condEvent = 'RoleTick', id = 'limitLogin', processFlag = 0}, 
	["online"] = {condEvent = 'RoleTick', id = 'online', processFlag = 2}, 
	["totalLogin"] = {condEvent = 'Login', id = 'totalLogin', processFlag = 1}, 
	["continueLogin"] = {condEvent = 'Login', id = 'continueLogin', processFlag = 0}, 
	["attrChange1"] = {condEvent = 'AttrChange1', id = 'attrChange1', processFlag = 1}, 
	["attrChange2"] = {condEvent = 'AttrChange2', id = 'attrChange2', processFlag = 0}, 
	["attrChange3"] = {condEvent = 'AttrChange3', id = 'attrChange3', processFlag = 0}, 
	["attrChange4"] = {condEvent = 'AttrChange4', id = 'attrChange4', processFlag = 1}, 
	["attrChange5"] = {condEvent = 'AttrChange5', id = 'attrChange5', processFlag = 0}, 
	["attrChange6"] = {condEvent = 'AttrChange6', id = 'attrChange6', processFlag = 0}, 
	["attrChange7"] = {condEvent = 'AttrChange7', id = 'attrChange7', processFlag = 0}, 
	["attrChange8"] = {condEvent = 'AttrChange8', id = 'attrChange8', processFlag = 0}, 
	["attrChange9"] = {condEvent = 'AttrChange9', id = 'attrChange9', processFlag = 0}, 
	["attrChange10"] = {condEvent = 'AttrChange10', id = 'attrChange10', processFlag = 0}, 
	["attrChange11"] = {condEvent = 'AttrChange11', id = 'attrChange11', processFlag = 0}, 
	["attrChange12"] = {condEvent = 'AttrChange12', id = 'attrChange12', processFlag = 0}, 
	["attrChange13"] = {condEvent = 'AttrChange13', id = 'attrChange13', processFlag = 0}, 
	["attrChange14"] = {condEvent = 'AttrChange14', id = 'attrChange14', processFlag = 1}, 
	["attrChange15"] = {condEvent = 'AttrChange15', id = 'attrChange15', processFlag = 0}, 
	["attrChange16"] = {condEvent = 'AttrChange16', id = 'attrChange16', processFlag = 0}, 
	["attrChange17"] = {condEvent = 'AttrChange17', id = 'attrChange17', processFlag = 0}, 
	["attrChange18"] = {condEvent = 'AttrChange18', id = 'attrChange18', processFlag = 0}, 
	["attrChange22"] = {condEvent = 'AttrChange22', id = 'attrChange22', processFlag = 0}, 
	["attrChange23"] = {condEvent = 'AttrChange23', id = 'attrChange23', processFlag = 0}, 
	["attrChange24"] = {condEvent = 'AttrChange24', id = 'attrChange24', processFlag = 0}, 
	["attrChange25"] = {condEvent = 'AttrChange25', id = 'attrChange25', processFlag = 0}, 
	["attrChange27"] = {condEvent = 'AttrChange27', id = 'attrChange27', processFlag = 0}, 
	["attrChange28"] = {condEvent = 'AttrChange28', id = 'attrChange28', processFlag = 0}, 
	["attrChange29"] = {condEvent = 'AttrChange29', id = 'attrChange29', processFlag = 0}, 
	["attrChange30"] = {condEvent = 'AttrChange30', id = 'attrChange30', processFlag = 0}, 
	["attrChange33"] = {condEvent = 'AttrChange33', id = 'attrChange33', processFlag = 0}, 
	["follower"] = {condEvent = 'FansChange', id = 'follower', processFlag = 0}, 
	["finishQuestionare"] = {condEvent = 'FinishQuestionare', id = 'finishQuestionare', processFlag = 0}, 
	["doLike"] = {condEvent = 'DoLike', id = 'doLike', processFlag = 1}, 
	["beLiked"] = {condEvent = 'BeLiked', id = 'beLiked', processFlag = 1}, 
	["following"] = {condEvent = 'Following', id = 'following', processFlag = 1}, 
	["itemBoxOpen"] = {condEvent = 'ItemUse', id = 'itemBoxOpen', processFlag = 1}, 
	["gainItem"] = {condEvent = 'GainItem', id = 'gainItem', processFlag = 1}, 
	["channelChat"] = {condEvent = 'ChatTask', id = 'channelChat', processFlag = 1}, 
	["recruit"] = {condEvent = 'RecruitTask', id = 'recruit', processFlag = 1}, 
	["shopTrade"] = {condEvent = 'ShopTrade', id = 'shopTrade', processFlag = 1}, 
	["battleWithFollow"] = {condEvent = 'Gaming', id = 'battleWithFollow', processFlag = 1}, 
	["battlePurchase"] = {condEvent = 'Gaming', id = 'battlePurchase', processFlag = 1}, 
	["totalHeadShotKill"] = {condEvent = 'Gaming', id = 'totalHeadShotKill', processFlag = 1}, 
	["headShotKill"] = {condEvent = 'Gaming', id = 'headShotKill', processFlag = 1}, 
	["gainMvp"] = {condEvent = 'Gaming', id = 'gainMvp', processFlag = 1}, 
	["setUpC4"] = {condEvent = 'Gaming', id = 'setUpC4', processFlag = 1}, 
	["defuseC4"] = {condEvent = 'Gaming', id = 'defuseC4', processFlag = 1}, 
	["killMonster"] = {condEvent = 'Gaming', id = 'killMonster', processFlag = 1}, 
	["totalHitCount"] = {condEvent = 'Gaming', id = 'totalHitCount', processFlag = 1}, 
	["totalFireCount"] = {condEvent = 'Gaming', id = 'totalFireCount', processFlag = 1}, 
	["invite"] = {condEvent = 'Invite', id = 'invite', processFlag = 0}, 
	["invitationAgreed"] = {condEvent = 'InviteAnswer', id = 'invitationAgreed', processFlag = 0}, 
	["battleLike"] = {condEvent = 'BattleLike', id = 'battleLike', processFlag = 1}, 
	["battleLiked"] = {condEvent = 'BattleLiked', id = 'battleLiked', processFlag = 1}, 
	["totalWinRound"] = {condEvent = 'Gaming', id = 'totalWinRound', processFlag = 0}, 
	["totalMoveDistance"] = {condEvent = 'Gaming', id = 'totalMoveDistance', processFlag = 0}, 
	["limitCamp"] = {condEvent = 'Gaming', id = 'limitCamp', processFlag = 0}, 
	["roundTotalMoney"] = {condEvent = 'Gaming', id = 'roundTotalMoney', processFlag = 0}, 
	["limitWinType"] = {condEvent = 'Gaming', id = 'limitWinType', processFlag = 0}, 
	["battleTitle"] = {condEvent = 'Gaming', id = 'battleTitle', processFlag = 0}, 
	["battleRank"] = {condEvent = 'Gaming', id = 'battleRank', processFlag = 0}, 
	["totalAssist"] = {condEvent = 'Gaming', id = 'totalAssist', processFlag = 0}, 
	["multiKillCount"] = {condEvent = 'Gaming', id = 'multiKillCount', processFlag = 0}, 
	["totalBlindKill"] = {condEvent = 'Gaming', id = 'totalBlindKill', processFlag = 0}, 
	["continueDeathNoKill"] = {condEvent = 'Gaming', id = 'continueDeathNoKill', processFlag = 0}, 
	["leaveGame"] = {condEvent = 'BattleQuit', id = 'leaveGame', processFlag = 0}, 
	["campSurvive"] = {condEvent = 'Gaming', id = 'campSurvive', processFlag = 0}, 
	["lastSurvive"] = {condEvent = 'Gaming', id = 'lastSurvive', processFlag = 0}, 
	["variedWeaponKill"] = {condEvent = 'Gaming', id = 'variedWeaponKill', processFlag = 0}, 
	["limitRole"] = {condEvent = 'Gaming', id = 'limitRole', processFlag = 0}, 
	["killAllEnemyAndTeamUnhurt"] = {condEvent = 'Gaming', id = 'killAllEnemyAndTeamUnhurt', processFlag = 0}, 
	["killDefuseC4ByGrenades"] = {condEvent = 'Gaming', id = 'killDefuseC4ByGrenades', processFlag = 0}, 
	["gunKillFromBack"] = {condEvent = 'Gaming', id = 'gunKillFromBack', processFlag = 0}, 
	["daggerKillFromBack"] = {condEvent = 'Gaming', id = 'daggerKillFromBack', processFlag = 0}, 
	["killOpenMirrorByDagger"] = {condEvent = 'Gaming', id = 'killOpenMirrorByDagger', processFlag = 0}, 
	["flashedDagger"] = {condEvent = 'Gaming', id = 'flashedDagger', processFlag = 0}, 
	["killEnemyInSmoke"] = {condEvent = 'Gaming', id = 'killEnemyInSmoke', processFlag = 0}, 
	["killWithoutMirror"] = {condEvent = 'Gaming', id = 'killWithoutMirror', processFlag = 0}, 
	["throwWeaponCount"] = {condEvent = 'Gaming', id = 'throwWeaponCount', processFlag = 1}, 
	["throwWeaponHitTotal"] = {condEvent = 'Gaming', id = 'throwWeaponHitTotal', processFlag = 0}, 
	["weaponAssist"] = {condEvent = 'Gaming', id = 'weaponAssist', processFlag = 0}, 
	["throwWeaponkill"] = {condEvent = 'Gaming', id = 'throwWeaponkill', processFlag = 0}, 
	["throwWeaponHit"] = {condEvent = 'Gaming', id = 'throwWeaponHit', processFlag = 0}, 
	["oneBulletKill"] = {condEvent = 'Gaming', id = 'oneBulletKill', processFlag = 0}, 
	["multiAttackSurvived"] = {condEvent = 'Gaming', id = 'multiAttackSurvived', processFlag = 0}, 
	["killLowHpEnemy"] = {condEvent = 'Gaming', id = 'killLowHpEnemy', processFlag = 0}, 
	["suicide"] = {condEvent = 'Gaming', id = 'suicide', processFlag = 0}, 
	["grenadesKillWhenDead"] = {condEvent = 'Gaming', id = 'grenadesKillWhenDead', processFlag = 0}, 
	["dyingKillEnemy"] = {condEvent = 'Gaming', id = 'dyingKillEnemy', processFlag = 0}, 
	["killedByProjectile"] = {condEvent = 'Gaming', id = 'killedByProjectile', processFlag = 0}, 
	["killedInSmoke"] = {condEvent = 'Gaming', id = 'killedInSmoke', processFlag = 0}, 
	["deadInFlashByTeam"] = {condEvent = 'Gaming', id = 'deadInFlashByTeam', processFlag = 0}, 
	["uronKillAssist"] = {condEvent = 'Gaming', id = 'uronKillAssist', processFlag = 0}, 
	["uronDamageByProjectile"] = {condEvent = 'Gaming', id = 'uronDamageByProjectile', processFlag = 0}, 
	["uronAssistByFlash"] = {condEvent = 'Gaming', id = 'uronAssistByFlash', processFlag = 0}, 
	["sceneDestroyed"] = {condEvent = 'Gaming', id = 'sceneDestroyed', processFlag = 0}, 
	["easterEgg"] = {condEvent = 'Gaming', id = 'easterEgg', processFlag = 0}, 
	["setUpC4ToKill"] = {condEvent = 'Gaming', id = 'setUpC4ToKill', processFlag = 0}, 
	["defuseC4AndEnemySurvive"] = {condEvent = 'Gaming', id = 'defuseC4AndEnemySurvive', processFlag = 0}, 
	["comingEndSetUpC4"] = {condEvent = 'Gaming', id = 'comingEndSetUpC4', processFlag = 0}, 
	["killDefusingC4"] = {condEvent = 'Gaming', id = 'killDefusingC4', processFlag = 0}, 
	["defusingC4Kill"] = {condEvent = 'Gaming', id = 'defusingC4Kill', processFlag = 0}, 
	["killSetUpC4"] = {condEvent = 'Gaming', id = 'killSetUpC4', processFlag = 0}, 
	["comingEndDefuseC4"] = {condEvent = 'Gaming', id = 'comingEndDefuseC4', processFlag = 0}, 
	["killChickenByBurn"] = {condEvent = 'Gaming', id = 'killChickenByBurn', processFlag = 0}, 
	["smallKillBig"] = {condEvent = 'Gaming', id = 'smallKillBig', processFlag = 0}, 
	["notHeadshotKill"] = {condEvent = 'Gaming', id = 'notHeadshotKill', processFlag = 0}, 
	["killByDagger"] = {condEvent = 'Gaming', id = 'killByDagger', processFlag = 0}, 
	["killJoker"] = {condEvent = 'Gaming', id = 'killJoker', processFlag = 0}, 
	["killPolice"] = {condEvent = 'Gaming', id = 'killPolice', processFlag = 0}, 
	["capturePoint"] = {condEvent = 'Gaming', id = 'capturePoint', processFlag = 0}, 
	["perfectDance"] = {condEvent = 'Gaming', id = 'perfectDance', processFlag = 0}, 
	["killAllAndDefuseC4"] = {condEvent = 'Gaming', id = 'killAllAndDefuseC4', processFlag = 0}, 
	["killDefuseC4ComingEnd"] = {condEvent = 'Gaming', id = 'killDefuseC4ComingEnd', processFlag = 0}, 
	["defuseC4ButExplosion"] = {condEvent = 'Gaming', id = 'defuseC4ButExplosion', processFlag = 0}, 
	["lastAmmoKill"] = {condEvent = 'Gaming', id = 'lastAmmoKill', processFlag = 0}, 
	["surviveTimeWithLowHp"] = {condEvent = 'Gaming', id = 'surviveTimeWithLowHp', processFlag = 0}, 
	["surviveTillEnd"] = {condEvent = 'Gaming', id = 'surviveTillEnd', processFlag = 0}, 
	["bigHeadTime"] = {condEvent = 'Gaming', id = 'bigHeadTime', processFlag = 0}, 
	["assistKill"] = {condEvent = 'Gaming', id = 'assistKill', processFlag = 0}, 
	["roundHitRate"] = {condEvent = 'Gaming', id = 'roundHitRate', processFlag = 0}, 
	["roundKillAllEnemyBySelf"] = {condEvent = 'Gaming', id = 'roundKillAllEnemyBySelf', processFlag = 0}, 
	["talentTotal"] = {condEvent = 'Gaming', id = 'talentTotal', processFlag = 1}, 
	["usePropTotal"] = {condEvent = 'Gaming', id = 'usePropTotal', processFlag = 1}, 
	["equipTakeOn"] = {condEvent = 'ERoleEquipChange', id = 'equipTakeOn', processFlag = 0}, 
	["killBig"] = {condEvent = 'Gaming', id = 'killBig', processFlag = 0}, 
	["killEnemyInAir"] = {condEvent = 'Gaming', id = 'killEnemyInAir', processFlag = 0}, 
	["meleeFireHeavyKill"] = {condEvent = 'Gaming', id = 'meleeFireHeavyKill', processFlag = 0}, 
	["killBlindedEnemy"] = {condEvent = 'Gaming', id = 'killBlindedEnemy', processFlag = 0}, 
	["killRankedPlayer"] = {condEvent = 'Gaming', id = 'killRankedPlayer', processFlag = 0}, 
	["beRankedPlayer"] = {condEvent = 'Gaming', id = 'beRankedPlayer', processFlag = 0}, 
	["lastKill"] = {condEvent = 'Gaming', id = 'lastKill', processFlag = 0}, 
	["pickUpItem "] = {condEvent = 'Gaming', id = 'pickUpItem ', processFlag = 0}, 
	["killEnemyAfterDeath"] = {condEvent = 'Gaming', id = 'killEnemyAfterDeath', processFlag = 0}, 
	["finishTaskCount"] = {condEvent = 'FinishTask', id = 'finishTaskCount', processFlag = 1}, 
	["firstRoundWin"] = {condEvent = 'Gaming', id = 'firstRoundWin', processFlag = 0}, 
	["finishResourcePacket"] = {condEvent = 'DownLoadPacket', id = 'finishResourcePacket', processFlag = 0}, 
	["killSmokedEnemy"] = {condEvent = 'Gaming', id = 'killSmokedEnemy', processFlag = 0}, 
	["surviveWithLowHp"] = {condEvent = 'Gaming', id = 'surviveWithLowHp', processFlag = 0}, 
	["killEnemyWithMixedSmoke"] = {condEvent = 'Gaming', id = 'killEnemyWithMixedSmoke', processFlag = 0}, 
	["luckyDraw"] = {condEvent = 'LuckyDraw', id = 'luckyDraw', processFlag = 0}, 
	["streakKill"] = {condEvent = 'Gaming', id = 'streakKill', processFlag = 0}, 
	["pveNobodyHelpRespawn"] = {condEvent = 'Gaming', id = 'pveNobodyHelpRespawn', processFlag = 0}, 
	["deadByZombieGrenades"] = {condEvent = 'Gaming', id = 'deadByZombieGrenades', processFlag = 0}, 
	["pveRespawnTotalCount"] = {condEvent = 'Gaming', id = 'pveRespawnTotalCount', processFlag = 0}, 
	["pveHelpRespawnCount"] = {condEvent = 'Gaming', id = 'pveHelpRespawnCount', processFlag = 0}, 
	["WinBySetC4OfDeadPartner"] = {condEvent = 'Gaming', id = 'WinBySetC4OfDeadPartner', processFlag = 0}, 
	["equipGsTotalScore"] = {condEvent = 'EquipGSChange', id = 'equipGsTotalScore', processFlag = 1}, 
	["equipGsTotalActive"] = {condEvent = 'EquipGSChange', id = 'equipGsTotalActive', processFlag = 0}, 
	["snipeKillNotMirror"] = {condEvent = 'Gaming', id = 'snipeKillNotMirror', processFlag = 0}, 
	["noviceShoot"] = {condEvent = 'NoviceShoot', id = 'noviceShoot', processFlag = 0}, 
	["damageToMonster"] = {condEvent = 'Gaming', id = 'damageToMonster', processFlag = 1}, 
	["updateClientApp"] = {condEvent = 'Login', id = 'updateClientApp', processFlag = 0}, 
	["updateClientResource"] = {condEvent = 'Login', id = 'updateClientResource', processFlag = 0}, 
	["friendGiftSend"] = {condEvent = 'FriendGift', id = 'friendGiftSend', processFlag = 0}, 
	["friendGiftRecv"] = {condEvent = 'FriendGift', id = 'friendGiftRecv', processFlag = 0}
}
return TaskConditionTable