# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_musicboxkeyconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_musicboxkeyconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!xls_beans_musicboxkeyconfig.proto\x12\nD11.Pbeans\"-\n\x11MusicBoxKeyConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"G\n\x17MusicBoxKeyConfig_Array\x12,\n\x05items\x18\x01 \x03(\x0b\x32\x1d.D11.Pbeans.MusicBoxKeyConfigb\x06proto3')
)




_MUSICBOXKEYCONFIG = _descriptor.Descriptor(
  name='MusicBoxKeyConfig',
  full_name='D11.Pbeans.MusicBoxKeyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.MusicBoxKeyConfig.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.MusicBoxKeyConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=49,
  serialized_end=94,
)


_MUSICBOXKEYCONFIG_ARRAY = _descriptor.Descriptor(
  name='MusicBoxKeyConfig_Array',
  full_name='D11.Pbeans.MusicBoxKeyConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.MusicBoxKeyConfig_Array.items', index=0,
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
  serialized_end=167,
)

_MUSICBOXKEYCONFIG_ARRAY.fields_by_name['items'].message_type = _MUSICBOXKEYCONFIG
DESCRIPTOR.message_types_by_name['MusicBoxKeyConfig'] = _MUSICBOXKEYCONFIG
DESCRIPTOR.message_types_by_name['MusicBoxKeyConfig_Array'] = _MUSICBOXKEYCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MusicBoxKeyConfig = _reflection.GeneratedProtocolMessageType('MusicBoxKeyConfig', (_message.Message,), {
  'DESCRIPTOR' : _MUSICBOXKEYCONFIG,
  '__module__' : 'xls_beans_musicboxkeyconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MusicBoxKeyConfig)
  })
_sym_db.RegisterMessage(MusicBoxKeyConfig)

MusicBoxKeyConfig_Array = _reflection.GeneratedProtocolMessageType('MusicBoxKeyConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _MUSICBOXKEYCONFIG_ARRAY,
  '__module__' : 'xls_beans_musicboxkeyconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MusicBoxKeyConfig_Array)
  })
_sym_db.RegisterMessage(MusicBoxKeyConfig_Array)


# @@protoc_insertion_point(module_scope)