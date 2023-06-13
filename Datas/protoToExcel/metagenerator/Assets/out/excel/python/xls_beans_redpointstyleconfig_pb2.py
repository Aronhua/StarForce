# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_redpointstyleconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_redpointstyleconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#xls_beans_redpointstyleconfig.proto\x12\nD11.Pbeans\"\x85\x01\n\x13RedpointStyleConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\ncreateFunc\x18\x02 \x01(\t\x12\x12\n\nupdateFunc\x18\x03 \x01(\t\x12\x12\n\nprefabPath\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t\x12\x0b\n\x03num\x18\x06 \x01(\x05\x12\x0b\n\x03str\x18\x07 \x01(\t\"K\n\x19RedpointStyleConfig_Array\x12.\n\x05items\x18\x01 \x03(\x0b\x32\x1f.D11.Pbeans.RedpointStyleConfigb\x06proto3')
)




_REDPOINTSTYLECONFIG = _descriptor.Descriptor(
  name='RedpointStyleConfig',
  full_name='D11.Pbeans.RedpointStyleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.RedpointStyleConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createFunc', full_name='D11.Pbeans.RedpointStyleConfig.createFunc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateFunc', full_name='D11.Pbeans.RedpointStyleConfig.updateFunc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefabPath', full_name='D11.Pbeans.RedpointStyleConfig.prefabPath', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='D11.Pbeans.RedpointStyleConfig.text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='D11.Pbeans.RedpointStyleConfig.num', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str', full_name='D11.Pbeans.RedpointStyleConfig.str', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=52,
  serialized_end=185,
)


_REDPOINTSTYLECONFIG_ARRAY = _descriptor.Descriptor(
  name='RedpointStyleConfig_Array',
  full_name='D11.Pbeans.RedpointStyleConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.RedpointStyleConfig_Array.items', index=0,
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
  serialized_start=187,
  serialized_end=262,
)

_REDPOINTSTYLECONFIG_ARRAY.fields_by_name['items'].message_type = _REDPOINTSTYLECONFIG
DESCRIPTOR.message_types_by_name['RedpointStyleConfig'] = _REDPOINTSTYLECONFIG
DESCRIPTOR.message_types_by_name['RedpointStyleConfig_Array'] = _REDPOINTSTYLECONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedpointStyleConfig = _reflection.GeneratedProtocolMessageType('RedpointStyleConfig', (_message.Message,), {
  'DESCRIPTOR' : _REDPOINTSTYLECONFIG,
  '__module__' : 'xls_beans_redpointstyleconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RedpointStyleConfig)
  })
_sym_db.RegisterMessage(RedpointStyleConfig)

RedpointStyleConfig_Array = _reflection.GeneratedProtocolMessageType('RedpointStyleConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _REDPOINTSTYLECONFIG_ARRAY,
  '__module__' : 'xls_beans_redpointstyleconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RedpointStyleConfig_Array)
  })
_sym_db.RegisterMessage(RedpointStyleConfig_Array)


# @@protoc_insertion_point(module_scope)