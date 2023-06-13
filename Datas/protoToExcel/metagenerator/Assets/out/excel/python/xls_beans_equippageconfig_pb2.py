# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_equippageconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_equippageconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fxls_beans_equippageconfig.proto\x12\nD11.Pbeans\"]\n\x0f\x45quipPageConfig\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x30\n\x05Types\x18\x03 \x03(\x0b\x32!.D11.Pbeans.EquipPageConfig_Types\":\n\x15\x45quipPageConfig_Types\x12\x10\n\x08mainType\x18\x01 \x01(\x05\x12\x0f\n\x07subType\x18\x02 \x01(\x05\"C\n\x15\x45quipPageConfig_Array\x12*\n\x05items\x18\x01 \x03(\x0b\x32\x1b.D11.Pbeans.EquipPageConfigb\x06proto3')
)




_EQUIPPAGECONFIG = _descriptor.Descriptor(
  name='EquipPageConfig',
  full_name='D11.Pbeans.EquipPageConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.EquipPageConfig.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.EquipPageConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Types', full_name='D11.Pbeans.EquipPageConfig.Types', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=47,
  serialized_end=140,
)


_EQUIPPAGECONFIG_TYPES = _descriptor.Descriptor(
  name='EquipPageConfig_Types',
  full_name='D11.Pbeans.EquipPageConfig_Types',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mainType', full_name='D11.Pbeans.EquipPageConfig_Types.mainType', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subType', full_name='D11.Pbeans.EquipPageConfig_Types.subType', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=142,
  serialized_end=200,
)


_EQUIPPAGECONFIG_ARRAY = _descriptor.Descriptor(
  name='EquipPageConfig_Array',
  full_name='D11.Pbeans.EquipPageConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.EquipPageConfig_Array.items', index=0,
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
  serialized_start=202,
  serialized_end=269,
)

_EQUIPPAGECONFIG.fields_by_name['Types'].message_type = _EQUIPPAGECONFIG_TYPES
_EQUIPPAGECONFIG_ARRAY.fields_by_name['items'].message_type = _EQUIPPAGECONFIG
DESCRIPTOR.message_types_by_name['EquipPageConfig'] = _EQUIPPAGECONFIG
DESCRIPTOR.message_types_by_name['EquipPageConfig_Types'] = _EQUIPPAGECONFIG_TYPES
DESCRIPTOR.message_types_by_name['EquipPageConfig_Array'] = _EQUIPPAGECONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipPageConfig = _reflection.GeneratedProtocolMessageType('EquipPageConfig', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPPAGECONFIG,
  '__module__' : 'xls_beans_equippageconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.EquipPageConfig)
  })
_sym_db.RegisterMessage(EquipPageConfig)

EquipPageConfig_Types = _reflection.GeneratedProtocolMessageType('EquipPageConfig_Types', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPPAGECONFIG_TYPES,
  '__module__' : 'xls_beans_equippageconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.EquipPageConfig_Types)
  })
_sym_db.RegisterMessage(EquipPageConfig_Types)

EquipPageConfig_Array = _reflection.GeneratedProtocolMessageType('EquipPageConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPPAGECONFIG_ARRAY,
  '__module__' : 'xls_beans_equippageconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.EquipPageConfig_Array)
  })
_sym_db.RegisterMessage(EquipPageConfig_Array)


# @@protoc_insertion_point(module_scope)