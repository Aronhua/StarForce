# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WeaponHitSceneDecalComponentData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WeaponHitSceneDecalComponentData.proto',
  package='D11.Pjson',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&WeaponHitSceneDecalComponentData.proto\x12\tD11.Pjson\"\xa5\x0b\n WeaponHitSceneDecalComponentData\x12\x14\n\x0c\x44\x65\x66\x61ultDecal\x18\x01 \x01(\x05\x12\x12\n\nEarthDecal\x18\x02 \x03(\x05\x12\x12\n\nMetalDecal\x18\x03 \x03(\x05\x12\x11\n\tWoodDecal\x18\x04 \x03(\x05\x12\x12\n\nStoneDecal\x18\x05 \x03(\x05\x12\x13\n\x0b\x46\x61\x62ricDecal\x18\x06 \x03(\x05\x12\x12\n\nGlassDecal\x18\x07 \x03(\x05\x12\x10\n\x08OilDecal\x18\x08 \x03(\x05\x12\x11\n\tPawnDecal\x18\t \x03(\x05\x12\x11\n\tLeafDecal\x18\n \x03(\x05\x12\x14\n\x0cPlasticDecal\x18\x0b \x03(\x05\x12\x13\n\x0bRubeerDecal\x18\x0c \x03(\x05\x12\x11\n\tSandDecal\x18\r \x03(\x05\x12\x13\n\x0b\x43\x65mentDecal\x18\x0e \x03(\x05\x12\x16\n\x0eHitEarthEffect\x18\x0f \x01(\x05\x12\x16\n\x0eHitMetalEffect\x18\x10 \x01(\x05\x12\x15\n\rHitWoodEffect\x18\x11 \x01(\x05\x12\x16\n\x0eHitStoneEffect\x18\x12 \x01(\x05\x12\x17\n\x0fHitFabricEffect\x18\x13 \x01(\x05\x12\x16\n\x0eHitGlassEffect\x18\x14 \x01(\x05\x12\x14\n\x0cHitOilEffect\x18\x15 \x01(\x05\x12\x15\n\rHitPawnEffect\x18\x16 \x01(\x05\x12\x15\n\rHitLeafEffect\x18\x17 \x01(\x05\x12\x18\n\x10HitPlasticEffect\x18\x18 \x01(\x05\x12\x17\n\x0fHitRubeerEffect\x18\x19 \x01(\x05\x12\x15\n\rHitSandEffect\x18\x1a \x01(\x05\x12\x17\n\x0fHitCementEffect\x18\x1b \x01(\x05\x12\x17\n\x0fMeleeHitSoundFP\x18\x1c \x01(\t\x12\x17\n\x0fMeleeHitSoundTP\x18\x1d \x01(\t\x12\x14\n\x0cHitWallSound\x18\x1e \x01(\t\x12\x16\n\x0e\x42odyHitSound1P\x18\x1f \x01(\t\x12\x16\n\x0eHeadHitSound1P\x18  \x01(\t\x12\x1c\n\x14ShieldBodyHitSound1P\x18! \x01(\t\x12\x1c\n\x14ShieldHeadHitSound1P\x18\" \x01(\t\x12\x16\n\x0e\x42odyHitSound3P\x18# \x01(\t\x12\x16\n\x0eHeadHitSound3P\x18$ \x01(\t\x12\x18\n\x10ShieldHitSound3P\x18% \x01(\t\x12\x15\n\rDamagedEffect\x18& \x01(\x05\x12\x19\n\x11\x44\x61magedHeadEffect\x18\' \x01(\x05\x12\x1e\n\x16\x44\x61magedExplosionEffect\x18( \x01(\x05\x12\x1b\n\x13\x44\x61magedHelmetEffect\x18) \x01(\x05\x12\x14\n\x0c\x44\x61magedDecal\x18* \x03(\x05\x12\x19\n\x11\x44\x61magedDecalLegal\x18+ \x03(\x05\x12\x17\n\x0f\x44\x61magedDecalLow\x18, \x01(\x05\x12\x18\n\x10TpDeadAudioEvent\x18- \x01(\t\x12\x14\n\x0cTpDeadEffect\x18. \x01(\r\x12\x1b\n\x13TpDeadRagDollEnable\x18/ \x01(\x08\x12\x1e\n\x16TpDeadEffectTypeOnBody\x18\x30 \x01(\x05\x12\x13\n\x0bSkinKillVFX\x18\x31 \x01(\x05\x12\x15\n\rSkinKillAudio\x18\x32 \x01(\t\x12\x19\n\x11SkinKillAllowAnim\x18\x33 \x01(\x08\x12\x17\n\x0fSkinLastKillVFX\x18\x34 \x01(\x05\x12\x19\n\x11SkinLastKillAudio\x18\x35 \x01(\t\x12\x1d\n\x15SkinLastKillAllowAnim\x18\x36 \x01(\x08\x12$\n\x1cSkinLastKillCameraShakeAsset\x18\x37 \x01(\t\x12)\n!SkinLastKillCameraShakeDelayTimes\x18\x38 \x01(\x02\x12\"\n\x1aSkinLastKillAmplitudeRange\x18\x39 \x01(\x02\x62\x06proto3')
)




_WEAPONHITSCENEDECALCOMPONENTDATA = _descriptor.Descriptor(
  name='WeaponHitSceneDecalComponentData',
  full_name='D11.Pjson.WeaponHitSceneDecalComponentData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DefaultDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.DefaultDecal', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EarthDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.EarthDecal', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MetalDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.MetalDecal', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='WoodDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.WoodDecal', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StoneDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.StoneDecal', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FabricDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.FabricDecal', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='GlassDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.GlassDecal', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='OilDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.OilDecal', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PawnDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.PawnDecal', index=8,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LeafDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.LeafDecal', index=9,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PlasticDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.PlasticDecal', index=10,
      number=11, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RubeerDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.RubeerDecal', index=11,
      number=12, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SandDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SandDecal', index=12,
      number=13, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CementDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.CementDecal', index=13,
      number=14, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitEarthEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitEarthEffect', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitMetalEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitMetalEffect', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitWoodEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitWoodEffect', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitStoneEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitStoneEffect', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitFabricEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitFabricEffect', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitGlassEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitGlassEffect', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitOilEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitOilEffect', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitPawnEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitPawnEffect', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitLeafEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitLeafEffect', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitPlasticEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitPlasticEffect', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitRubeerEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitRubeerEffect', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitSandEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitSandEffect', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitCementEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitCementEffect', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MeleeHitSoundFP', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.MeleeHitSoundFP', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MeleeHitSoundTP', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.MeleeHitSoundTP', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HitWallSound', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HitWallSound', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BodyHitSound1P', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.BodyHitSound1P', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HeadHitSound1P', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HeadHitSound1P', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ShieldBodyHitSound1P', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.ShieldBodyHitSound1P', index=32,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ShieldHeadHitSound1P', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.ShieldHeadHitSound1P', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BodyHitSound3P', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.BodyHitSound3P', index=34,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='HeadHitSound3P', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.HeadHitSound3P', index=35,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ShieldHitSound3P', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.ShieldHitSound3P', index=36,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DamagedEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.DamagedEffect', index=37,
      number=38, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DamagedHeadEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.DamagedHeadEffect', index=38,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DamagedExplosionEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.DamagedExplosionEffect', index=39,
      number=40, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DamagedHelmetEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.DamagedHelmetEffect', index=40,
      number=41, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DamagedDecal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.DamagedDecal', index=41,
      number=42, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DamagedDecalLegal', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.DamagedDecalLegal', index=42,
      number=43, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DamagedDecalLow', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.DamagedDecalLow', index=43,
      number=44, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TpDeadAudioEvent', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.TpDeadAudioEvent', index=44,
      number=45, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TpDeadEffect', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.TpDeadEffect', index=45,
      number=46, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TpDeadRagDollEnable', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.TpDeadRagDollEnable', index=46,
      number=47, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TpDeadEffectTypeOnBody', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.TpDeadEffectTypeOnBody', index=47,
      number=48, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinKillVFX', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinKillVFX', index=48,
      number=49, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinKillAudio', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinKillAudio', index=49,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinKillAllowAnim', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinKillAllowAnim', index=50,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinLastKillVFX', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinLastKillVFX', index=51,
      number=52, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinLastKillAudio', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinLastKillAudio', index=52,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinLastKillAllowAnim', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinLastKillAllowAnim', index=53,
      number=54, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinLastKillCameraShakeAsset', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinLastKillCameraShakeAsset', index=54,
      number=55, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinLastKillCameraShakeDelayTimes', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinLastKillCameraShakeDelayTimes', index=55,
      number=56, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkinLastKillAmplitudeRange', full_name='D11.Pjson.WeaponHitSceneDecalComponentData.SkinLastKillAmplitudeRange', index=56,
      number=57, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=1499,
)

DESCRIPTOR.message_types_by_name['WeaponHitSceneDecalComponentData'] = _WEAPONHITSCENEDECALCOMPONENTDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WeaponHitSceneDecalComponentData = _reflection.GeneratedProtocolMessageType('WeaponHitSceneDecalComponentData', (_message.Message,), {
  'DESCRIPTOR' : _WEAPONHITSCENEDECALCOMPONENTDATA,
  '__module__' : 'WeaponHitSceneDecalComponentData_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pjson.WeaponHitSceneDecalComponentData)
  })
_sym_db.RegisterMessage(WeaponHitSceneDecalComponentData)


# @@protoc_insertion_point(module_scope)