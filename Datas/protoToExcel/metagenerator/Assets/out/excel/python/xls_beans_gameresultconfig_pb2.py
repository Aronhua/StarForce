# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_gameresultconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_gameresultconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n xls_beans_gameresultconfig.proto\x12\nD11.Pbeans\"\x9c\x02\n\x10GameResultConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nresultTeam\x18\x03 \x01(\r\x12\x12\n\nresultData\x18\x04 \x01(\r\x12\x12\n\nresultDesc\x18\x05 \x01(\x08\x12\x13\n\x0bresultParam\x18\x06 \x01(\t\x12\x17\n\x0fresultDescParam\x18\x07 \x01(\t\x12\x12\n\nshowReport\x18\x08 \x01(\x08\x12\x15\n\rshowScoreType\x18\t \x01(\r\x12\x11\n\tshowAgain\x18\n \x01(\r\x12\x15\n\rcountDownTime\x18\x0b \x01(\r\x12\x13\n\x0bshowLoading\x18\x0c \x01(\x08\x12\x1a\n\x12showCharacterScore\x18\r \x01(\x08\"E\n\x16GameResultConfig_Array\x12+\n\x05items\x18\x01 \x03(\x0b\x32\x1c.D11.Pbeans.GameResultConfigb\x06proto3')
)




_GAMERESULTCONFIG = _descriptor.Descriptor(
  name='GameResultConfig',
  full_name='D11.Pbeans.GameResultConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.GameResultConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.GameResultConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultTeam', full_name='D11.Pbeans.GameResultConfig.resultTeam', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultData', full_name='D11.Pbeans.GameResultConfig.resultData', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultDesc', full_name='D11.Pbeans.GameResultConfig.resultDesc', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultParam', full_name='D11.Pbeans.GameResultConfig.resultParam', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultDescParam', full_name='D11.Pbeans.GameResultConfig.resultDescParam', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showReport', full_name='D11.Pbeans.GameResultConfig.showReport', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showScoreType', full_name='D11.Pbeans.GameResultConfig.showScoreType', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showAgain', full_name='D11.Pbeans.GameResultConfig.showAgain', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countDownTime', full_name='D11.Pbeans.GameResultConfig.countDownTime', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showLoading', full_name='D11.Pbeans.GameResultConfig.showLoading', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showCharacterScore', full_name='D11.Pbeans.GameResultConfig.showCharacterScore', index=12,
      number=13, type=8, cpp_type=7, label=1,
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
  serialized_start=49,
  serialized_end=333,
)


_GAMERESULTCONFIG_ARRAY = _descriptor.Descriptor(
  name='GameResultConfig_Array',
  full_name='D11.Pbeans.GameResultConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.GameResultConfig_Array.items', index=0,
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
  serialized_start=335,
  serialized_end=404,
)

_GAMERESULTCONFIG_ARRAY.fields_by_name['items'].message_type = _GAMERESULTCONFIG
DESCRIPTOR.message_types_by_name['GameResultConfig'] = _GAMERESULTCONFIG
DESCRIPTOR.message_types_by_name['GameResultConfig_Array'] = _GAMERESULTCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameResultConfig = _reflection.GeneratedProtocolMessageType('GameResultConfig', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESULTCONFIG,
  '__module__' : 'xls_beans_gameresultconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.GameResultConfig)
  })
_sym_db.RegisterMessage(GameResultConfig)

GameResultConfig_Array = _reflection.GeneratedProtocolMessageType('GameResultConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESULTCONFIG_ARRAY,
  '__module__' : 'xls_beans_gameresultconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.GameResultConfig_Array)
  })
_sym_db.RegisterMessage(GameResultConfig_Array)


# @@protoc_insertion_point(module_scope)