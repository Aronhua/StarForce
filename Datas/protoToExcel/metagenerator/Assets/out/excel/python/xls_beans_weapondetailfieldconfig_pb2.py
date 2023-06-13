# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_weapondetailfieldconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_weapondetailfieldconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'xls_beans_weapondetailfieldconfig.proto\x12\nD11.Pbeans\"S\n\x17WeaponDetailFieldConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08maxValue\x18\x03 \x01(\r\x12\x0c\n\x04unit\x18\x04 \x01(\t\"S\n\x1dWeaponDetailFieldConfig_Array\x12\x32\n\x05items\x18\x01 \x03(\x0b\x32#.D11.Pbeans.WeaponDetailFieldConfigb\x06proto3')
)




_WEAPONDETAILFIELDCONFIG = _descriptor.Descriptor(
  name='WeaponDetailFieldConfig',
  full_name='D11.Pbeans.WeaponDetailFieldConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.WeaponDetailFieldConfig.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.WeaponDetailFieldConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxValue', full_name='D11.Pbeans.WeaponDetailFieldConfig.maxValue', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='D11.Pbeans.WeaponDetailFieldConfig.unit', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=55,
  serialized_end=138,
)


_WEAPONDETAILFIELDCONFIG_ARRAY = _descriptor.Descriptor(
  name='WeaponDetailFieldConfig_Array',
  full_name='D11.Pbeans.WeaponDetailFieldConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.WeaponDetailFieldConfig_Array.items', index=0,
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
  serialized_start=140,
  serialized_end=223,
)

_WEAPONDETAILFIELDCONFIG_ARRAY.fields_by_name['items'].message_type = _WEAPONDETAILFIELDCONFIG
DESCRIPTOR.message_types_by_name['WeaponDetailFieldConfig'] = _WEAPONDETAILFIELDCONFIG
DESCRIPTOR.message_types_by_name['WeaponDetailFieldConfig_Array'] = _WEAPONDETAILFIELDCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WeaponDetailFieldConfig = _reflection.GeneratedProtocolMessageType('WeaponDetailFieldConfig', (_message.Message,), {
  'DESCRIPTOR' : _WEAPONDETAILFIELDCONFIG,
  '__module__' : 'xls_beans_weapondetailfieldconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.WeaponDetailFieldConfig)
  })
_sym_db.RegisterMessage(WeaponDetailFieldConfig)

WeaponDetailFieldConfig_Array = _reflection.GeneratedProtocolMessageType('WeaponDetailFieldConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _WEAPONDETAILFIELDCONFIG_ARRAY,
  '__module__' : 'xls_beans_weapondetailfieldconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.WeaponDetailFieldConfig_Array)
  })
_sym_db.RegisterMessage(WeaponDetailFieldConfig_Array)


# @@protoc_insertion_point(module_scope)