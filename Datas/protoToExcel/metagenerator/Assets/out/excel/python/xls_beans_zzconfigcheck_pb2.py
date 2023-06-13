# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_zzconfigcheck.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_zzconfigcheck.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dxls_beans_zzconfigcheck.proto\x12\nD11.Pbeans\"\x9c\x01\n\rZZConfigCheck\x12\x12\n\nconfigName\x18\x01 \x01(\t\x12\x11\n\tfieldName\x18\x02 \x01(\t\x12\x16\n\x0erelyConfigName\x18\x03 \x01(\t\x12\x15\n\rrelyFieldName\x18\x04 \x01(\t\x12\x10\n\x08relyType\x18\x05 \x01(\r\x12\x10\n\x08skipZero\x18\x06 \x01(\x08\x12\x11\n\trelyParam\x18\x07 \x03(\t\"?\n\x13ZZConfigCheck_Array\x12(\n\x05items\x18\x01 \x03(\x0b\x32\x19.D11.Pbeans.ZZConfigCheckb\x06proto3')
)




_ZZCONFIGCHECK = _descriptor.Descriptor(
  name='ZZConfigCheck',
  full_name='D11.Pbeans.ZZConfigCheck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configName', full_name='D11.Pbeans.ZZConfigCheck.configName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fieldName', full_name='D11.Pbeans.ZZConfigCheck.fieldName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relyConfigName', full_name='D11.Pbeans.ZZConfigCheck.relyConfigName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relyFieldName', full_name='D11.Pbeans.ZZConfigCheck.relyFieldName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relyType', full_name='D11.Pbeans.ZZConfigCheck.relyType', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skipZero', full_name='D11.Pbeans.ZZConfigCheck.skipZero', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relyParam', full_name='D11.Pbeans.ZZConfigCheck.relyParam', index=6,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=46,
  serialized_end=202,
)


_ZZCONFIGCHECK_ARRAY = _descriptor.Descriptor(
  name='ZZConfigCheck_Array',
  full_name='D11.Pbeans.ZZConfigCheck_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.ZZConfigCheck_Array.items', index=0,
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
  serialized_start=204,
  serialized_end=267,
)

_ZZCONFIGCHECK_ARRAY.fields_by_name['items'].message_type = _ZZCONFIGCHECK
DESCRIPTOR.message_types_by_name['ZZConfigCheck'] = _ZZCONFIGCHECK
DESCRIPTOR.message_types_by_name['ZZConfigCheck_Array'] = _ZZCONFIGCHECK_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZZConfigCheck = _reflection.GeneratedProtocolMessageType('ZZConfigCheck', (_message.Message,), {
  'DESCRIPTOR' : _ZZCONFIGCHECK,
  '__module__' : 'xls_beans_zzconfigcheck_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ZZConfigCheck)
  })
_sym_db.RegisterMessage(ZZConfigCheck)

ZZConfigCheck_Array = _reflection.GeneratedProtocolMessageType('ZZConfigCheck_Array', (_message.Message,), {
  'DESCRIPTOR' : _ZZCONFIGCHECK_ARRAY,
  '__module__' : 'xls_beans_zzconfigcheck_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ZZConfigCheck_Array)
  })
_sym_db.RegisterMessage(ZZConfigCheck_Array)


# @@protoc_insertion_point(module_scope)