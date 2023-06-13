# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_matchmodeorderconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_matchmodeorderconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$xls_beans_matchmodeorderconfig.proto\x12\nD11.Pbeans\"D\n\x14MatchModeOrderConfig\x12\x10\n\x08randomId\x18\x01 \x01(\r\x12\x0c\n\x04mode\x18\x02 \x01(\r\x12\x0c\n\x04step\x18\x03 \x01(\r\"M\n\x1aMatchModeOrderConfig_Array\x12/\n\x05items\x18\x01 \x03(\x0b\x32 .D11.Pbeans.MatchModeOrderConfigb\x06proto3')
)




_MATCHMODEORDERCONFIG = _descriptor.Descriptor(
  name='MatchModeOrderConfig',
  full_name='D11.Pbeans.MatchModeOrderConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='randomId', full_name='D11.Pbeans.MatchModeOrderConfig.randomId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='D11.Pbeans.MatchModeOrderConfig.mode', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='D11.Pbeans.MatchModeOrderConfig.step', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=52,
  serialized_end=120,
)


_MATCHMODEORDERCONFIG_ARRAY = _descriptor.Descriptor(
  name='MatchModeOrderConfig_Array',
  full_name='D11.Pbeans.MatchModeOrderConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.MatchModeOrderConfig_Array.items', index=0,
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
  serialized_start=122,
  serialized_end=199,
)

_MATCHMODEORDERCONFIG_ARRAY.fields_by_name['items'].message_type = _MATCHMODEORDERCONFIG
DESCRIPTOR.message_types_by_name['MatchModeOrderConfig'] = _MATCHMODEORDERCONFIG
DESCRIPTOR.message_types_by_name['MatchModeOrderConfig_Array'] = _MATCHMODEORDERCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchModeOrderConfig = _reflection.GeneratedProtocolMessageType('MatchModeOrderConfig', (_message.Message,), {
  'DESCRIPTOR' : _MATCHMODEORDERCONFIG,
  '__module__' : 'xls_beans_matchmodeorderconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchModeOrderConfig)
  })
_sym_db.RegisterMessage(MatchModeOrderConfig)

MatchModeOrderConfig_Array = _reflection.GeneratedProtocolMessageType('MatchModeOrderConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _MATCHMODEORDERCONFIG_ARRAY,
  '__module__' : 'xls_beans_matchmodeorderconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchModeOrderConfig_Array)
  })
_sym_db.RegisterMessage(MatchModeOrderConfig_Array)


# @@protoc_insertion_point(module_scope)