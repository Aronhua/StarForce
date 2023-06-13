# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_rolelevelcatadef.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_rolelevelcatadef.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n xls_beans_rolelevelcatadef.proto\x12\nD11.Pbeans\"D\n\x10RoleLevelCataDef\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\nstartLevel\x18\x02 \x01(\r\x12\x10\n\x08\x65ndLevel\x18\x03 \x01(\r\"E\n\x16RoleLevelCataDef_Array\x12+\n\x05items\x18\x01 \x03(\x0b\x32\x1c.D11.Pbeans.RoleLevelCataDefb\x06proto3')
)




_ROLELEVELCATADEF = _descriptor.Descriptor(
  name='RoleLevelCataDef',
  full_name='D11.Pbeans.RoleLevelCataDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.RoleLevelCataDef.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startLevel', full_name='D11.Pbeans.RoleLevelCataDef.startLevel', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endLevel', full_name='D11.Pbeans.RoleLevelCataDef.endLevel', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=48,
  serialized_end=116,
)


_ROLELEVELCATADEF_ARRAY = _descriptor.Descriptor(
  name='RoleLevelCataDef_Array',
  full_name='D11.Pbeans.RoleLevelCataDef_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.RoleLevelCataDef_Array.items', index=0,
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
  serialized_start=118,
  serialized_end=187,
)

_ROLELEVELCATADEF_ARRAY.fields_by_name['items'].message_type = _ROLELEVELCATADEF
DESCRIPTOR.message_types_by_name['RoleLevelCataDef'] = _ROLELEVELCATADEF
DESCRIPTOR.message_types_by_name['RoleLevelCataDef_Array'] = _ROLELEVELCATADEF_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleLevelCataDef = _reflection.GeneratedProtocolMessageType('RoleLevelCataDef', (_message.Message,), {
  'DESCRIPTOR' : _ROLELEVELCATADEF,
  '__module__' : 'xls_beans_rolelevelcatadef_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleLevelCataDef)
  })
_sym_db.RegisterMessage(RoleLevelCataDef)

RoleLevelCataDef_Array = _reflection.GeneratedProtocolMessageType('RoleLevelCataDef_Array', (_message.Message,), {
  'DESCRIPTOR' : _ROLELEVELCATADEF_ARRAY,
  '__module__' : 'xls_beans_rolelevelcatadef_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleLevelCataDef_Array)
  })
_sym_db.RegisterMessage(RoleLevelCataDef_Array)


# @@protoc_insertion_point(module_scope)