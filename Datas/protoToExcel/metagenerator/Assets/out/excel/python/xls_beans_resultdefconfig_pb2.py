# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_resultdefconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_resultdefconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fxls_beans_resultdefconfig.proto\x12\nD11.Pbeans\"/\n\x0fResultDefConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08\x64uration\x18\x02 \x01(\x02\"C\n\x15ResultDefConfig_Array\x12*\n\x05items\x18\x01 \x03(\x0b\x32\x1b.D11.Pbeans.ResultDefConfigb\x06proto3')
)




_RESULTDEFCONFIG = _descriptor.Descriptor(
  name='ResultDefConfig',
  full_name='D11.Pbeans.ResultDefConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.ResultDefConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='D11.Pbeans.ResultDefConfig.duration', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=47,
  serialized_end=94,
)


_RESULTDEFCONFIG_ARRAY = _descriptor.Descriptor(
  name='ResultDefConfig_Array',
  full_name='D11.Pbeans.ResultDefConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.ResultDefConfig_Array.items', index=0,
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
  serialized_start=96,
  serialized_end=163,
)

_RESULTDEFCONFIG_ARRAY.fields_by_name['items'].message_type = _RESULTDEFCONFIG
DESCRIPTOR.message_types_by_name['ResultDefConfig'] = _RESULTDEFCONFIG
DESCRIPTOR.message_types_by_name['ResultDefConfig_Array'] = _RESULTDEFCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResultDefConfig = _reflection.GeneratedProtocolMessageType('ResultDefConfig', (_message.Message,), {
  'DESCRIPTOR' : _RESULTDEFCONFIG,
  '__module__' : 'xls_beans_resultdefconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ResultDefConfig)
  })
_sym_db.RegisterMessage(ResultDefConfig)

ResultDefConfig_Array = _reflection.GeneratedProtocolMessageType('ResultDefConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _RESULTDEFCONFIG_ARRAY,
  '__module__' : 'xls_beans_resultdefconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ResultDefConfig_Array)
  })
_sym_db.RegisterMessage(ResultDefConfig_Array)


# @@protoc_insertion_point(module_scope)