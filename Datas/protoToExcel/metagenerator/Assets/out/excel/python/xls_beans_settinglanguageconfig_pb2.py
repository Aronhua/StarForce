# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_settinglanguageconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_settinglanguageconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%xls_beans_settinglanguageconfig.proto\x12\nD11.Pbeans\"\xa8\x01\n\x15SettingLanguageConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05order\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08language\x18\x04 \x01(\t\x12\x14\n\x0csubPackageId\x18\x05 \x01(\t\x12\x15\n\raudioLanguage\x18\x06 \x01(\t\x12\x19\n\x11\x61udioSubPackageId\x18\x07 \x01(\t\x12\x0c\n\x04show\x18\x08 \x01(\x08\"O\n\x1bSettingLanguageConfig_Array\x12\x30\n\x05items\x18\x01 \x03(\x0b\x32!.D11.Pbeans.SettingLanguageConfigb\x06proto3')
)




_SETTINGLANGUAGECONFIG = _descriptor.Descriptor(
  name='SettingLanguageConfig',
  full_name='D11.Pbeans.SettingLanguageConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.SettingLanguageConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='D11.Pbeans.SettingLanguageConfig.order', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.SettingLanguageConfig.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='D11.Pbeans.SettingLanguageConfig.language', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subPackageId', full_name='D11.Pbeans.SettingLanguageConfig.subPackageId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audioLanguage', full_name='D11.Pbeans.SettingLanguageConfig.audioLanguage', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audioSubPackageId', full_name='D11.Pbeans.SettingLanguageConfig.audioSubPackageId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show', full_name='D11.Pbeans.SettingLanguageConfig.show', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=54,
  serialized_end=222,
)


_SETTINGLANGUAGECONFIG_ARRAY = _descriptor.Descriptor(
  name='SettingLanguageConfig_Array',
  full_name='D11.Pbeans.SettingLanguageConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.SettingLanguageConfig_Array.items', index=0,
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
  serialized_start=224,
  serialized_end=303,
)

_SETTINGLANGUAGECONFIG_ARRAY.fields_by_name['items'].message_type = _SETTINGLANGUAGECONFIG
DESCRIPTOR.message_types_by_name['SettingLanguageConfig'] = _SETTINGLANGUAGECONFIG
DESCRIPTOR.message_types_by_name['SettingLanguageConfig_Array'] = _SETTINGLANGUAGECONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SettingLanguageConfig = _reflection.GeneratedProtocolMessageType('SettingLanguageConfig', (_message.Message,), {
  'DESCRIPTOR' : _SETTINGLANGUAGECONFIG,
  '__module__' : 'xls_beans_settinglanguageconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.SettingLanguageConfig)
  })
_sym_db.RegisterMessage(SettingLanguageConfig)

SettingLanguageConfig_Array = _reflection.GeneratedProtocolMessageType('SettingLanguageConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _SETTINGLANGUAGECONFIG_ARRAY,
  '__module__' : 'xls_beans_settinglanguageconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.SettingLanguageConfig_Array)
  })
_sym_db.RegisterMessage(SettingLanguageConfig_Array)


# @@protoc_insertion_point(module_scope)