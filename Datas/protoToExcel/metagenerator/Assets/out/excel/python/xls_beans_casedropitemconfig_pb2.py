# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_casedropitemconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_casedropitemconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"xls_beans_casedropitemconfig.proto\x12\nD11.Pbeans\"[\n\x12\x43\x61seDropItemConfig\x12\x0e\n\x06\x64ropID\x18\x01 \x01(\r\x12\x35\n\x06reward\x18\x02 \x01(\x0b\x32%.D11.Pbeans.CaseDropItemConfig_reward\"\x90\x01\n\x19\x43\x61seDropItemConfig_reward\x12\x0e\n\x06itemid\x18\x01 \x01(\r\x12\x0e\n\x06weight\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\r\x12\x10\n\x08statTrak\x18\x04 \x01(\r\x12\x10\n\x08lockTime\x18\x05 \x01(\r\x12\x0e\n\x06\x65xpire\x18\x06 \x01(\r\x12\x10\n\x08paintKit\x18\x07 \x01(\r\"I\n\x18\x43\x61seDropItemConfig_Array\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.D11.Pbeans.CaseDropItemConfigb\x06proto3')
)




_CASEDROPITEMCONFIG = _descriptor.Descriptor(
  name='CaseDropItemConfig',
  full_name='D11.Pbeans.CaseDropItemConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dropID', full_name='D11.Pbeans.CaseDropItemConfig.dropID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='D11.Pbeans.CaseDropItemConfig.reward', index=1,
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
  serialized_start=50,
  serialized_end=141,
)


_CASEDROPITEMCONFIG_REWARD = _descriptor.Descriptor(
  name='CaseDropItemConfig_reward',
  full_name='D11.Pbeans.CaseDropItemConfig_reward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemid', full_name='D11.Pbeans.CaseDropItemConfig_reward.itemid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='D11.Pbeans.CaseDropItemConfig_reward.weight', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='D11.Pbeans.CaseDropItemConfig_reward.value', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statTrak', full_name='D11.Pbeans.CaseDropItemConfig_reward.statTrak', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lockTime', full_name='D11.Pbeans.CaseDropItemConfig_reward.lockTime', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expire', full_name='D11.Pbeans.CaseDropItemConfig_reward.expire', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paintKit', full_name='D11.Pbeans.CaseDropItemConfig_reward.paintKit', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=144,
  serialized_end=288,
)


_CASEDROPITEMCONFIG_ARRAY = _descriptor.Descriptor(
  name='CaseDropItemConfig_Array',
  full_name='D11.Pbeans.CaseDropItemConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.CaseDropItemConfig_Array.items', index=0,
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
  serialized_start=290,
  serialized_end=363,
)

_CASEDROPITEMCONFIG.fields_by_name['reward'].message_type = _CASEDROPITEMCONFIG_REWARD
_CASEDROPITEMCONFIG_ARRAY.fields_by_name['items'].message_type = _CASEDROPITEMCONFIG
DESCRIPTOR.message_types_by_name['CaseDropItemConfig'] = _CASEDROPITEMCONFIG
DESCRIPTOR.message_types_by_name['CaseDropItemConfig_reward'] = _CASEDROPITEMCONFIG_REWARD
DESCRIPTOR.message_types_by_name['CaseDropItemConfig_Array'] = _CASEDROPITEMCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CaseDropItemConfig = _reflection.GeneratedProtocolMessageType('CaseDropItemConfig', (_message.Message,), {
  'DESCRIPTOR' : _CASEDROPITEMCONFIG,
  '__module__' : 'xls_beans_casedropitemconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseDropItemConfig)
  })
_sym_db.RegisterMessage(CaseDropItemConfig)

CaseDropItemConfig_reward = _reflection.GeneratedProtocolMessageType('CaseDropItemConfig_reward', (_message.Message,), {
  'DESCRIPTOR' : _CASEDROPITEMCONFIG_REWARD,
  '__module__' : 'xls_beans_casedropitemconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseDropItemConfig_reward)
  })
_sym_db.RegisterMessage(CaseDropItemConfig_reward)

CaseDropItemConfig_Array = _reflection.GeneratedProtocolMessageType('CaseDropItemConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _CASEDROPITEMCONFIG_ARRAY,
  '__module__' : 'xls_beans_casedropitemconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseDropItemConfig_Array)
  })
_sym_db.RegisterMessage(CaseDropItemConfig_Array)


# @@protoc_insertion_point(module_scope)