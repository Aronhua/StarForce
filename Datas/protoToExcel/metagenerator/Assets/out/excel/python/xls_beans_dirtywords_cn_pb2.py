# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_dirtywords_cn.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_dirtywords_cn.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dxls_beans_dirtywords_cn.proto\x12\nD11.Pbeans\"\x1d\n\rDirtyWords_CN\x12\x0c\n\x04word\x18\x01 \x01(\t\"?\n\x13\x44irtyWords_CN_Array\x12(\n\x05items\x18\x01 \x03(\x0b\x32\x19.D11.Pbeans.DirtyWords_CNb\x06proto3')
)




_DIRTYWORDS_CN = _descriptor.Descriptor(
  name='DirtyWords_CN',
  full_name='D11.Pbeans.DirtyWords_CN',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='D11.Pbeans.DirtyWords_CN.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=45,
  serialized_end=74,
)


_DIRTYWORDS_CN_ARRAY = _descriptor.Descriptor(
  name='DirtyWords_CN_Array',
  full_name='D11.Pbeans.DirtyWords_CN_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.DirtyWords_CN_Array.items', index=0,
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
  serialized_start=76,
  serialized_end=139,
)

_DIRTYWORDS_CN_ARRAY.fields_by_name['items'].message_type = _DIRTYWORDS_CN
DESCRIPTOR.message_types_by_name['DirtyWords_CN'] = _DIRTYWORDS_CN
DESCRIPTOR.message_types_by_name['DirtyWords_CN_Array'] = _DIRTYWORDS_CN_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DirtyWords_CN = _reflection.GeneratedProtocolMessageType('DirtyWords_CN', (_message.Message,), {
  'DESCRIPTOR' : _DIRTYWORDS_CN,
  '__module__' : 'xls_beans_dirtywords_cn_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.DirtyWords_CN)
  })
_sym_db.RegisterMessage(DirtyWords_CN)

DirtyWords_CN_Array = _reflection.GeneratedProtocolMessageType('DirtyWords_CN_Array', (_message.Message,), {
  'DESCRIPTOR' : _DIRTYWORDS_CN_ARRAY,
  '__module__' : 'xls_beans_dirtywords_cn_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.DirtyWords_CN_Array)
  })
_sym_db.RegisterMessage(DirtyWords_CN_Array)


# @@protoc_insertion_point(module_scope)