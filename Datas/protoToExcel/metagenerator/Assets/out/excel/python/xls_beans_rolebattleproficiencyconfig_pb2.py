# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_rolebattleproficiencyconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_rolebattleproficiencyconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+xls_beans_rolebattleproficiencyconfig.proto\x12\nD11.Pbeans\"V\n\x1bRoleBattleProficiencyConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06showId\x18\x03 \x01(\r\x12\r\n\x05order\x18\x04 \x01(\r\"[\n!RoleBattleProficiencyConfig_Array\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.D11.Pbeans.RoleBattleProficiencyConfigb\x06proto3')
)




_ROLEBATTLEPROFICIENCYCONFIG = _descriptor.Descriptor(
  name='RoleBattleProficiencyConfig',
  full_name='D11.Pbeans.RoleBattleProficiencyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.RoleBattleProficiencyConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='D11.Pbeans.RoleBattleProficiencyConfig.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showId', full_name='D11.Pbeans.RoleBattleProficiencyConfig.showId', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='D11.Pbeans.RoleBattleProficiencyConfig.order', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=59,
  serialized_end=145,
)


_ROLEBATTLEPROFICIENCYCONFIG_ARRAY = _descriptor.Descriptor(
  name='RoleBattleProficiencyConfig_Array',
  full_name='D11.Pbeans.RoleBattleProficiencyConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.RoleBattleProficiencyConfig_Array.items', index=0,
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
  serialized_start=147,
  serialized_end=238,
)

_ROLEBATTLEPROFICIENCYCONFIG_ARRAY.fields_by_name['items'].message_type = _ROLEBATTLEPROFICIENCYCONFIG
DESCRIPTOR.message_types_by_name['RoleBattleProficiencyConfig'] = _ROLEBATTLEPROFICIENCYCONFIG
DESCRIPTOR.message_types_by_name['RoleBattleProficiencyConfig_Array'] = _ROLEBATTLEPROFICIENCYCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleBattleProficiencyConfig = _reflection.GeneratedProtocolMessageType('RoleBattleProficiencyConfig', (_message.Message,), {
  'DESCRIPTOR' : _ROLEBATTLEPROFICIENCYCONFIG,
  '__module__' : 'xls_beans_rolebattleproficiencyconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleBattleProficiencyConfig)
  })
_sym_db.RegisterMessage(RoleBattleProficiencyConfig)

RoleBattleProficiencyConfig_Array = _reflection.GeneratedProtocolMessageType('RoleBattleProficiencyConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _ROLEBATTLEPROFICIENCYCONFIG_ARRAY,
  '__module__' : 'xls_beans_rolebattleproficiencyconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleBattleProficiencyConfig_Array)
  })
_sym_db.RegisterMessage(RoleBattleProficiencyConfig_Array)


# @@protoc_insertion_point(module_scope)