# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_roledecoration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_roledecoration.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1exls_beans_roledecoration.proto\x12\nD11.Pbeans\"\xce\x01\n\x0eRoleDecoration\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\nfallbackid\x18\x02 \x01(\r\x12\x14\n\x0c\x66\x65malefpPath\x18\x03 \x01(\t\x12\x14\n\x0c\x66\x65maletpPath\x18\x04 \x01(\t\x12\x12\n\nmalefpPath\x18\x05 \x01(\t\x12\x12\n\nmaletpPath\x18\x06 \x01(\t\x12\x12\n\nGlovesType\x18\x07 \x01(\r\x12\x11\n\tpointName\x18\x08 \x01(\t\x12\x11\n\troleLimit\x18\t \x01(\x08\x12\x0e\n\x06roleid\x18\n \x03(\r\"A\n\x14RoleDecoration_Array\x12)\n\x05items\x18\x01 \x03(\x0b\x32\x1a.D11.Pbeans.RoleDecorationb\x06proto3')
)




_ROLEDECORATION = _descriptor.Descriptor(
  name='RoleDecoration',
  full_name='D11.Pbeans.RoleDecoration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.RoleDecoration.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fallbackid', full_name='D11.Pbeans.RoleDecoration.fallbackid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='femalefpPath', full_name='D11.Pbeans.RoleDecoration.femalefpPath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='femaletpPath', full_name='D11.Pbeans.RoleDecoration.femaletpPath', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='malefpPath', full_name='D11.Pbeans.RoleDecoration.malefpPath', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maletpPath', full_name='D11.Pbeans.RoleDecoration.maletpPath', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='GlovesType', full_name='D11.Pbeans.RoleDecoration.GlovesType', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pointName', full_name='D11.Pbeans.RoleDecoration.pointName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roleLimit', full_name='D11.Pbeans.RoleDecoration.roleLimit', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roleid', full_name='D11.Pbeans.RoleDecoration.roleid', index=9,
      number=10, type=13, cpp_type=3, label=3,
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
  serialized_end=253,
)


_ROLEDECORATION_ARRAY = _descriptor.Descriptor(
  name='RoleDecoration_Array',
  full_name='D11.Pbeans.RoleDecoration_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.RoleDecoration_Array.items', index=0,
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
  serialized_start=255,
  serialized_end=320,
)

_ROLEDECORATION_ARRAY.fields_by_name['items'].message_type = _ROLEDECORATION
DESCRIPTOR.message_types_by_name['RoleDecoration'] = _ROLEDECORATION
DESCRIPTOR.message_types_by_name['RoleDecoration_Array'] = _ROLEDECORATION_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleDecoration = _reflection.GeneratedProtocolMessageType('RoleDecoration', (_message.Message,), {
  'DESCRIPTOR' : _ROLEDECORATION,
  '__module__' : 'xls_beans_roledecoration_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleDecoration)
  })
_sym_db.RegisterMessage(RoleDecoration)

RoleDecoration_Array = _reflection.GeneratedProtocolMessageType('RoleDecoration_Array', (_message.Message,), {
  'DESCRIPTOR' : _ROLEDECORATION_ARRAY,
  '__module__' : 'xls_beans_roledecoration_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleDecoration_Array)
  })
_sym_db.RegisterMessage(RoleDecoration_Array)


# @@protoc_insertion_point(module_scope)