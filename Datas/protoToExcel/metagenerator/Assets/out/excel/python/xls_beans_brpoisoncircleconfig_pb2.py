# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_brpoisoncircleconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_brpoisoncircleconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$xls_beans_brpoisoncircleconfig.proto\x12\nD11.Pbeans\"\x9d\x02\n\x14\x42RPoisonCircleConfig\x12\x0e\n\x06modeId\x18\x01 \x01(\r\x12\x0f\n\x07sceneId\x18\x02 \x01(\r\x12\x0f\n\x07roundId\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x04 \x01(\x02\x12\x13\n\x0b\x63reateDelay\x18\x05 \x01(\r\x12\x10\n\x08stayTime\x18\x06 \x01(\r\x12\x10\n\x08moveTime\x18\x07 \x01(\r\x12\x1b\n\x13punishmentParameter\x18\x08 \x01(\x02\x12\x1b\n\x13punishmentFrequency\x18\t \x01(\x02\x12\x18\n\x10maxImmovableArea\x18\n \x01(\x02\x12\x0c\n\x04minX\x18\x0b \x01(\x05\x12\x0c\n\x04maxX\x18\x0c \x01(\x05\x12\x0c\n\x04minZ\x18\r \x01(\x05\x12\x0c\n\x04maxZ\x18\x0e \x01(\x05\"M\n\x1a\x42RPoisonCircleConfig_Array\x12/\n\x05items\x18\x01 \x03(\x0b\x32 .D11.Pbeans.BRPoisonCircleConfigb\x06proto3')
)




_BRPOISONCIRCLECONFIG = _descriptor.Descriptor(
  name='BRPoisonCircleConfig',
  full_name='D11.Pbeans.BRPoisonCircleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modeId', full_name='D11.Pbeans.BRPoisonCircleConfig.modeId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sceneId', full_name='D11.Pbeans.BRPoisonCircleConfig.sceneId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roundId', full_name='D11.Pbeans.BRPoisonCircleConfig.roundId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='D11.Pbeans.BRPoisonCircleConfig.radius', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createDelay', full_name='D11.Pbeans.BRPoisonCircleConfig.createDelay', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stayTime', full_name='D11.Pbeans.BRPoisonCircleConfig.stayTime', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moveTime', full_name='D11.Pbeans.BRPoisonCircleConfig.moveTime', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='punishmentParameter', full_name='D11.Pbeans.BRPoisonCircleConfig.punishmentParameter', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='punishmentFrequency', full_name='D11.Pbeans.BRPoisonCircleConfig.punishmentFrequency', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxImmovableArea', full_name='D11.Pbeans.BRPoisonCircleConfig.maxImmovableArea', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minX', full_name='D11.Pbeans.BRPoisonCircleConfig.minX', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxX', full_name='D11.Pbeans.BRPoisonCircleConfig.maxX', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minZ', full_name='D11.Pbeans.BRPoisonCircleConfig.minZ', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxZ', full_name='D11.Pbeans.BRPoisonCircleConfig.maxZ', index=13,
      number=14, type=5, cpp_type=1, label=1,
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
  serialized_start=53,
  serialized_end=338,
)


_BRPOISONCIRCLECONFIG_ARRAY = _descriptor.Descriptor(
  name='BRPoisonCircleConfig_Array',
  full_name='D11.Pbeans.BRPoisonCircleConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.BRPoisonCircleConfig_Array.items', index=0,
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
  serialized_start=340,
  serialized_end=417,
)

_BRPOISONCIRCLECONFIG_ARRAY.fields_by_name['items'].message_type = _BRPOISONCIRCLECONFIG
DESCRIPTOR.message_types_by_name['BRPoisonCircleConfig'] = _BRPOISONCIRCLECONFIG
DESCRIPTOR.message_types_by_name['BRPoisonCircleConfig_Array'] = _BRPOISONCIRCLECONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BRPoisonCircleConfig = _reflection.GeneratedProtocolMessageType('BRPoisonCircleConfig', (_message.Message,), {
  'DESCRIPTOR' : _BRPOISONCIRCLECONFIG,
  '__module__' : 'xls_beans_brpoisoncircleconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.BRPoisonCircleConfig)
  })
_sym_db.RegisterMessage(BRPoisonCircleConfig)

BRPoisonCircleConfig_Array = _reflection.GeneratedProtocolMessageType('BRPoisonCircleConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _BRPOISONCIRCLECONFIG_ARRAY,
  '__module__' : 'xls_beans_brpoisoncircleconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.BRPoisonCircleConfig_Array)
  })
_sym_db.RegisterMessage(BRPoisonCircleConfig_Array)


# @@protoc_insertion_point(module_scope)