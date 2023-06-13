# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_achievementreward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_achievementreward.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!xls_beans_achievementreward.proto\x12\nD11.Pbeans\"U\n\x11\x41\x63hievementReward\x12\n\n\x02id\x18\x01 \x01(\r\x12\x34\n\x06\x65\x66\x66\x65\x63t\x18\x02 \x01(\x0b\x32$.D11.Pbeans.AchievementReward_effect\"{\n\x18\x41\x63hievementReward_effect\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r\x12\x10\n\x08lockTime\x18\x03 \x01(\r\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\r\x12\x10\n\x08statTrak\x18\x05 \x01(\r\x12\x10\n\x08paintKit\x18\x06 \x01(\r\"G\n\x17\x41\x63hievementReward_Array\x12,\n\x05items\x18\x01 \x03(\x0b\x32\x1d.D11.Pbeans.AchievementRewardb\x06proto3')
)




_ACHIEVEMENTREWARD = _descriptor.Descriptor(
  name='AchievementReward',
  full_name='D11.Pbeans.AchievementReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.AchievementReward.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effect', full_name='D11.Pbeans.AchievementReward.effect', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=49,
  serialized_end=134,
)


_ACHIEVEMENTREWARD_EFFECT = _descriptor.Descriptor(
  name='AchievementReward_effect',
  full_name='D11.Pbeans.AchievementReward_effect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.AchievementReward_effect.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='D11.Pbeans.AchievementReward_effect.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lockTime', full_name='D11.Pbeans.AchievementReward_effect.lockTime', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expire', full_name='D11.Pbeans.AchievementReward_effect.expire', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statTrak', full_name='D11.Pbeans.AchievementReward_effect.statTrak', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paintKit', full_name='D11.Pbeans.AchievementReward_effect.paintKit', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=136,
  serialized_end=259,
)


_ACHIEVEMENTREWARD_ARRAY = _descriptor.Descriptor(
  name='AchievementReward_Array',
  full_name='D11.Pbeans.AchievementReward_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.AchievementReward_Array.items', index=0,
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
  serialized_start=261,
  serialized_end=332,
)

_ACHIEVEMENTREWARD.fields_by_name['effect'].message_type = _ACHIEVEMENTREWARD_EFFECT
_ACHIEVEMENTREWARD_ARRAY.fields_by_name['items'].message_type = _ACHIEVEMENTREWARD
DESCRIPTOR.message_types_by_name['AchievementReward'] = _ACHIEVEMENTREWARD
DESCRIPTOR.message_types_by_name['AchievementReward_effect'] = _ACHIEVEMENTREWARD_EFFECT
DESCRIPTOR.message_types_by_name['AchievementReward_Array'] = _ACHIEVEMENTREWARD_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AchievementReward = _reflection.GeneratedProtocolMessageType('AchievementReward', (_message.Message,), {
  'DESCRIPTOR' : _ACHIEVEMENTREWARD,
  '__module__' : 'xls_beans_achievementreward_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.AchievementReward)
  })
_sym_db.RegisterMessage(AchievementReward)

AchievementReward_effect = _reflection.GeneratedProtocolMessageType('AchievementReward_effect', (_message.Message,), {
  'DESCRIPTOR' : _ACHIEVEMENTREWARD_EFFECT,
  '__module__' : 'xls_beans_achievementreward_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.AchievementReward_effect)
  })
_sym_db.RegisterMessage(AchievementReward_effect)

AchievementReward_Array = _reflection.GeneratedProtocolMessageType('AchievementReward_Array', (_message.Message,), {
  'DESCRIPTOR' : _ACHIEVEMENTREWARD_ARRAY,
  '__module__' : 'xls_beans_achievementreward_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.AchievementReward_Array)
  })
_sym_db.RegisterMessage(AchievementReward_Array)


# @@protoc_insertion_point(module_scope)