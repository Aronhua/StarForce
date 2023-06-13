# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_loginconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_loginconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bxls_beans_loginconfig.proto\x12\nD11.Pbeans\"x\n\x0bLoginConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\r\x12\x10\n\x08OpenType\x18\x04 \x01(\r\x12\x18\n\x10navigateFuncName\x18\x05 \x01(\t\x12\x15\n\rnavigateParam\x18\x06 \x01(\r\";\n\x11LoginConfig_Array\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.D11.Pbeans.LoginConfigb\x06proto3')
)




_LOGINCONFIG = _descriptor.Descriptor(
  name='LoginConfig',
  full_name='D11.Pbeans.LoginConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.LoginConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.LoginConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='D11.Pbeans.LoginConfig.icon', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='OpenType', full_name='D11.Pbeans.LoginConfig.OpenType', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigateFuncName', full_name='D11.Pbeans.LoginConfig.navigateFuncName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigateParam', full_name='D11.Pbeans.LoginConfig.navigateParam', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=43,
  serialized_end=163,
)


_LOGINCONFIG_ARRAY = _descriptor.Descriptor(
  name='LoginConfig_Array',
  full_name='D11.Pbeans.LoginConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.LoginConfig_Array.items', index=0,
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
  serialized_start=165,
  serialized_end=224,
)

_LOGINCONFIG_ARRAY.fields_by_name['items'].message_type = _LOGINCONFIG
DESCRIPTOR.message_types_by_name['LoginConfig'] = _LOGINCONFIG
DESCRIPTOR.message_types_by_name['LoginConfig_Array'] = _LOGINCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginConfig = _reflection.GeneratedProtocolMessageType('LoginConfig', (_message.Message,), {
  'DESCRIPTOR' : _LOGINCONFIG,
  '__module__' : 'xls_beans_loginconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.LoginConfig)
  })
_sym_db.RegisterMessage(LoginConfig)

LoginConfig_Array = _reflection.GeneratedProtocolMessageType('LoginConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _LOGINCONFIG_ARRAY,
  '__module__' : 'xls_beans_loginconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.LoginConfig_Array)
  })
_sym_db.RegisterMessage(LoginConfig_Array)


# @@protoc_insertion_point(module_scope)