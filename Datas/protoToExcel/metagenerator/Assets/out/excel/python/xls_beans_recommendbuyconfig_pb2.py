# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_recommendbuyconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_recommendbuyconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"xls_beans_recommendbuyconfig.proto\x12\nD11.Pbeans\"\xa3\x02\n\x12RecommendBuyConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x13\n\x0bWeaponOrder\x18\x02 \x01(\x05\x12\x16\n\x0eSubWeaponOrder\x18\x03 \x01(\x05\x12\x19\n\x11TacticalPropOrder\x18\x04 \x01(\x05\x12\x12\n\nEquipOrder\x18\x05 \x01(\x05\x12\x14\n\x0cGrenadeOrder\x18\x06 \x01(\x05\x12K\n\x11WeaponMoneyRanges\x18\x07 \x03(\x0b\x32\x30.D11.Pbeans.RecommendBuyConfig_WeaponMoneyRanges\x12\x18\n\x10\x41rmorMoneyRanges\x18\x08 \x03(\x05\x12\x11\n\tKeepMoney\x18\t \x01(\x05\x12\x15\n\rRepeatGrenade\x18\n \x01(\x08\"R\n$RecommendBuyConfig_WeaponMoneyRanges\x12\x0b\n\x03Max\x18\x01 \x01(\x05\x12\x0b\n\x03Min\x18\x02 \x01(\x05\x12\x10\n\x08\x44\x65\x63rease\x18\x03 \x01(\x05\"I\n\x18RecommendBuyConfig_Array\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.D11.Pbeans.RecommendBuyConfigb\x06proto3')
)




_RECOMMENDBUYCONFIG = _descriptor.Descriptor(
  name='RecommendBuyConfig',
  full_name='D11.Pbeans.RecommendBuyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.RecommendBuyConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='WeaponOrder', full_name='D11.Pbeans.RecommendBuyConfig.WeaponOrder', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SubWeaponOrder', full_name='D11.Pbeans.RecommendBuyConfig.SubWeaponOrder', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TacticalPropOrder', full_name='D11.Pbeans.RecommendBuyConfig.TacticalPropOrder', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EquipOrder', full_name='D11.Pbeans.RecommendBuyConfig.EquipOrder', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='GrenadeOrder', full_name='D11.Pbeans.RecommendBuyConfig.GrenadeOrder', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='WeaponMoneyRanges', full_name='D11.Pbeans.RecommendBuyConfig.WeaponMoneyRanges', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ArmorMoneyRanges', full_name='D11.Pbeans.RecommendBuyConfig.ArmorMoneyRanges', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='KeepMoney', full_name='D11.Pbeans.RecommendBuyConfig.KeepMoney', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RepeatGrenade', full_name='D11.Pbeans.RecommendBuyConfig.RepeatGrenade', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=51,
  serialized_end=342,
)


_RECOMMENDBUYCONFIG_WEAPONMONEYRANGES = _descriptor.Descriptor(
  name='RecommendBuyConfig_WeaponMoneyRanges',
  full_name='D11.Pbeans.RecommendBuyConfig_WeaponMoneyRanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Max', full_name='D11.Pbeans.RecommendBuyConfig_WeaponMoneyRanges.Max', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Min', full_name='D11.Pbeans.RecommendBuyConfig_WeaponMoneyRanges.Min', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Decrease', full_name='D11.Pbeans.RecommendBuyConfig_WeaponMoneyRanges.Decrease', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=344,
  serialized_end=426,
)


_RECOMMENDBUYCONFIG_ARRAY = _descriptor.Descriptor(
  name='RecommendBuyConfig_Array',
  full_name='D11.Pbeans.RecommendBuyConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.RecommendBuyConfig_Array.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=428,
  serialized_end=501,
)

_RECOMMENDBUYCONFIG.fields_by_name['WeaponMoneyRanges'].message_type = _RECOMMENDBUYCONFIG_WEAPONMONEYRANGES
_RECOMMENDBUYCONFIG_ARRAY.fields_by_name['items'].message_type = _RECOMMENDBUYCONFIG
DESCRIPTOR.message_types_by_name['RecommendBuyConfig'] = _RECOMMENDBUYCONFIG
DESCRIPTOR.message_types_by_name['RecommendBuyConfig_WeaponMoneyRanges'] = _RECOMMENDBUYCONFIG_WEAPONMONEYRANGES
DESCRIPTOR.message_types_by_name['RecommendBuyConfig_Array'] = _RECOMMENDBUYCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecommendBuyConfig = _reflection.GeneratedProtocolMessageType('RecommendBuyConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDBUYCONFIG,
  '__module__' : 'xls_beans_recommendbuyconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RecommendBuyConfig)
  })
_sym_db.RegisterMessage(RecommendBuyConfig)

RecommendBuyConfig_WeaponMoneyRanges = _reflection.GeneratedProtocolMessageType('RecommendBuyConfig_WeaponMoneyRanges', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDBUYCONFIG_WEAPONMONEYRANGES,
  '__module__' : 'xls_beans_recommendbuyconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RecommendBuyConfig_WeaponMoneyRanges)
  })
_sym_db.RegisterMessage(RecommendBuyConfig_WeaponMoneyRanges)

RecommendBuyConfig_Array = _reflection.GeneratedProtocolMessageType('RecommendBuyConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDBUYCONFIG_ARRAY,
  '__module__' : 'xls_beans_recommendbuyconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RecommendBuyConfig_Array)
  })
_sym_db.RegisterMessage(RecommendBuyConfig_Array)


# @@protoc_insertion_point(module_scope)