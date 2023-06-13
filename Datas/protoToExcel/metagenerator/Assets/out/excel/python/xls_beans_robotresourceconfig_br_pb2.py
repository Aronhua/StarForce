# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_robotresourceconfig_br.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_robotresourceconfig_br.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&xls_beans_robotresourceconfig_br.proto\x12\nD11.Pbeans\"\x86\x01\n\x16RobotResourceConfig_BR\x12\x14\n\x0cresourceType\x18\x01 \x01(\t\x12\x13\n\x0b\x65\x66\x66\x65\x63tScope\x18\x02 \x01(\r\x12\x41\n\nrandomList\x18\x03 \x03(\x0b\x32-.D11.Pbeans.RobotResourceConfig_BR_randomList\"Q\n!RobotResourceConfig_BR_randomList\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06weight\x18\x02 \x01(\r\x12\x10\n\x08openTime\x18\x03 \x01(\x03\"Q\n\x1cRobotResourceConfig_BR_Array\x12\x31\n\x05items\x18\x01 \x03(\x0b\x32\".D11.Pbeans.RobotResourceConfig_BRb\x06proto3')
)




_ROBOTRESOURCECONFIG_BR = _descriptor.Descriptor(
  name='RobotResourceConfig_BR',
  full_name='D11.Pbeans.RobotResourceConfig_BR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resourceType', full_name='D11.Pbeans.RobotResourceConfig_BR.resourceType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effectScope', full_name='D11.Pbeans.RobotResourceConfig_BR.effectScope', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='randomList', full_name='D11.Pbeans.RobotResourceConfig_BR.randomList', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=55,
  serialized_end=189,
)


_ROBOTRESOURCECONFIG_BR_RANDOMLIST = _descriptor.Descriptor(
  name='RobotResourceConfig_BR_randomList',
  full_name='D11.Pbeans.RobotResourceConfig_BR_randomList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.RobotResourceConfig_BR_randomList.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='D11.Pbeans.RobotResourceConfig_BR_randomList.weight', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='openTime', full_name='D11.Pbeans.RobotResourceConfig_BR_randomList.openTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=191,
  serialized_end=272,
)


_ROBOTRESOURCECONFIG_BR_ARRAY = _descriptor.Descriptor(
  name='RobotResourceConfig_BR_Array',
  full_name='D11.Pbeans.RobotResourceConfig_BR_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.RobotResourceConfig_BR_Array.items', index=0,
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
  serialized_start=274,
  serialized_end=355,
)

_ROBOTRESOURCECONFIG_BR.fields_by_name['randomList'].message_type = _ROBOTRESOURCECONFIG_BR_RANDOMLIST
_ROBOTRESOURCECONFIG_BR_ARRAY.fields_by_name['items'].message_type = _ROBOTRESOURCECONFIG_BR
DESCRIPTOR.message_types_by_name['RobotResourceConfig_BR'] = _ROBOTRESOURCECONFIG_BR
DESCRIPTOR.message_types_by_name['RobotResourceConfig_BR_randomList'] = _ROBOTRESOURCECONFIG_BR_RANDOMLIST
DESCRIPTOR.message_types_by_name['RobotResourceConfig_BR_Array'] = _ROBOTRESOURCECONFIG_BR_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RobotResourceConfig_BR = _reflection.GeneratedProtocolMessageType('RobotResourceConfig_BR', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTRESOURCECONFIG_BR,
  '__module__' : 'xls_beans_robotresourceconfig_br_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RobotResourceConfig_BR)
  })
_sym_db.RegisterMessage(RobotResourceConfig_BR)

RobotResourceConfig_BR_randomList = _reflection.GeneratedProtocolMessageType('RobotResourceConfig_BR_randomList', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTRESOURCECONFIG_BR_RANDOMLIST,
  '__module__' : 'xls_beans_robotresourceconfig_br_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RobotResourceConfig_BR_randomList)
  })
_sym_db.RegisterMessage(RobotResourceConfig_BR_randomList)

RobotResourceConfig_BR_Array = _reflection.GeneratedProtocolMessageType('RobotResourceConfig_BR_Array', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTRESOURCECONFIG_BR_ARRAY,
  '__module__' : 'xls_beans_robotresourceconfig_br_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RobotResourceConfig_BR_Array)
  })
_sym_db.RegisterMessage(RobotResourceConfig_BR_Array)


# @@protoc_insertion_point(module_scope)