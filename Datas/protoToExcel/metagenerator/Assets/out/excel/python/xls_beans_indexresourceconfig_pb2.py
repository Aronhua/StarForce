# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_indexresourceconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_indexresourceconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#xls_beans_indexresourceconfig.proto\x12\nD11.Pbeans\"\xa0\x01\n\x13IndexResourceConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0b\n\x03num\x18\x03 \x03(\x05\x12\x0e\n\x06maxNum\x18\x04 \x03(\x05\x12\x13\n\x0bisWhiteList\x18\x05 \x01(\x08\x12\x0c\n\x04mode\x18\x06 \x03(\x05\x12\x11\n\tclearFlag\x18\x07 \x03(\r\x12\x1c\n\x14\x65xtremityMaxMultiple\x18\x08 \x01(\x05\"K\n\x19IndexResourceConfig_Array\x12.\n\x05items\x18\x01 \x03(\x0b\x32\x1f.D11.Pbeans.IndexResourceConfigb\x06proto3')
)




_INDEXRESOURCECONFIG = _descriptor.Descriptor(
  name='IndexResourceConfig',
  full_name='D11.Pbeans.IndexResourceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.IndexResourceConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='D11.Pbeans.IndexResourceConfig.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='D11.Pbeans.IndexResourceConfig.num', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxNum', full_name='D11.Pbeans.IndexResourceConfig.maxNum', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isWhiteList', full_name='D11.Pbeans.IndexResourceConfig.isWhiteList', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='D11.Pbeans.IndexResourceConfig.mode', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clearFlag', full_name='D11.Pbeans.IndexResourceConfig.clearFlag', index=6,
      number=7, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extremityMaxMultiple', full_name='D11.Pbeans.IndexResourceConfig.extremityMaxMultiple', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_end=212,
)


_INDEXRESOURCECONFIG_ARRAY = _descriptor.Descriptor(
  name='IndexResourceConfig_Array',
  full_name='D11.Pbeans.IndexResourceConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.IndexResourceConfig_Array.items', index=0,
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
  serialized_start=214,
  serialized_end=289,
)

_INDEXRESOURCECONFIG_ARRAY.fields_by_name['items'].message_type = _INDEXRESOURCECONFIG
DESCRIPTOR.message_types_by_name['IndexResourceConfig'] = _INDEXRESOURCECONFIG
DESCRIPTOR.message_types_by_name['IndexResourceConfig_Array'] = _INDEXRESOURCECONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IndexResourceConfig = _reflection.GeneratedProtocolMessageType('IndexResourceConfig', (_message.Message,), {
  'DESCRIPTOR' : _INDEXRESOURCECONFIG,
  '__module__' : 'xls_beans_indexresourceconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.IndexResourceConfig)
  })
_sym_db.RegisterMessage(IndexResourceConfig)

IndexResourceConfig_Array = _reflection.GeneratedProtocolMessageType('IndexResourceConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _INDEXRESOURCECONFIG_ARRAY,
  '__module__' : 'xls_beans_indexresourceconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.IndexResourceConfig_Array)
  })
_sym_db.RegisterMessage(IndexResourceConfig_Array)


# @@protoc_insertion_point(module_scope)