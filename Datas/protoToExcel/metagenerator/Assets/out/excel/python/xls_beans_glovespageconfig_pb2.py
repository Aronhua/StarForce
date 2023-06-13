# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_glovespageconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_glovespageconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n xls_beans_glovespageconfig.proto\x12\nD11.Pbeans\";\n\x10GlovesPageConfig\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05Types\x18\x03 \x03(\x05\"E\n\x16GlovesPageConfig_Array\x12+\n\x05items\x18\x01 \x03(\x0b\x32\x1c.D11.Pbeans.GlovesPageConfigb\x06proto3')
)




_GLOVESPAGECONFIG = _descriptor.Descriptor(
  name='GlovesPageConfig',
  full_name='D11.Pbeans.GlovesPageConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.GlovesPageConfig.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.GlovesPageConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Types', full_name='D11.Pbeans.GlovesPageConfig.Types', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=48,
  serialized_end=107,
)


_GLOVESPAGECONFIG_ARRAY = _descriptor.Descriptor(
  name='GlovesPageConfig_Array',
  full_name='D11.Pbeans.GlovesPageConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.GlovesPageConfig_Array.items', index=0,
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
  serialized_start=109,
  serialized_end=178,
)

_GLOVESPAGECONFIG_ARRAY.fields_by_name['items'].message_type = _GLOVESPAGECONFIG
DESCRIPTOR.message_types_by_name['GlovesPageConfig'] = _GLOVESPAGECONFIG
DESCRIPTOR.message_types_by_name['GlovesPageConfig_Array'] = _GLOVESPAGECONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GlovesPageConfig = _reflection.GeneratedProtocolMessageType('GlovesPageConfig', (_message.Message,), {
  'DESCRIPTOR' : _GLOVESPAGECONFIG,
  '__module__' : 'xls_beans_glovespageconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.GlovesPageConfig)
  })
_sym_db.RegisterMessage(GlovesPageConfig)

GlovesPageConfig_Array = _reflection.GeneratedProtocolMessageType('GlovesPageConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _GLOVESPAGECONFIG_ARRAY,
  '__module__' : 'xls_beans_glovespageconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.GlovesPageConfig_Array)
  })
_sym_db.RegisterMessage(GlovesPageConfig_Array)


# @@protoc_insertion_point(module_scope)