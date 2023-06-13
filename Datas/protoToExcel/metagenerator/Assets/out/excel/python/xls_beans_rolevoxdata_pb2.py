# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_rolevoxdata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_rolevoxdata.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bxls_beans_rolevoxdata.proto\x12\nD11.Pbeans\"\xb7\x01\n\x0bRoleVoxData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06RoleId\x18\x02 \x01(\r\x12\r\n\x05VoxId\x18\x03 \x01(\r\x12\x10\n\x08voxCTDes\x18\x04 \x01(\t\x12\x0f\n\x07voxTDes\x18\x05 \x01(\t\x12,\n\x05Vox1P\x18\x06 \x01(\x0b\x32\x1d.D11.Pbeans.RoleVoxData_Vox1P\x12,\n\x05Vox3P\x18\x07 \x01(\x0b\x32\x1d.D11.Pbeans.RoleVoxData_Vox3P\"/\n\x11RoleVoxData_Vox1P\x12\x0c\n\x04Play\x18\x01 \x01(\t\x12\x0c\n\x04Stop\x18\x02 \x01(\t\"/\n\x11RoleVoxData_Vox3P\x12\x0c\n\x04Play\x18\x01 \x01(\t\x12\x0c\n\x04Stop\x18\x02 \x01(\t\";\n\x11RoleVoxData_Array\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.D11.Pbeans.RoleVoxDatab\x06proto3')
)




_ROLEVOXDATA = _descriptor.Descriptor(
  name='RoleVoxData',
  full_name='D11.Pbeans.RoleVoxData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.RoleVoxData.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RoleId', full_name='D11.Pbeans.RoleVoxData.RoleId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VoxId', full_name='D11.Pbeans.RoleVoxData.VoxId', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voxCTDes', full_name='D11.Pbeans.RoleVoxData.voxCTDes', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voxTDes', full_name='D11.Pbeans.RoleVoxData.voxTDes', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Vox1P', full_name='D11.Pbeans.RoleVoxData.Vox1P', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Vox3P', full_name='D11.Pbeans.RoleVoxData.Vox3P', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=44,
  serialized_end=227,
)


_ROLEVOXDATA_VOX1P = _descriptor.Descriptor(
  name='RoleVoxData_Vox1P',
  full_name='D11.Pbeans.RoleVoxData_Vox1P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Play', full_name='D11.Pbeans.RoleVoxData_Vox1P.Play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Stop', full_name='D11.Pbeans.RoleVoxData_Vox1P.Stop', index=1,
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
  serialized_start=229,
  serialized_end=276,
)


_ROLEVOXDATA_VOX3P = _descriptor.Descriptor(
  name='RoleVoxData_Vox3P',
  full_name='D11.Pbeans.RoleVoxData_Vox3P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Play', full_name='D11.Pbeans.RoleVoxData_Vox3P.Play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Stop', full_name='D11.Pbeans.RoleVoxData_Vox3P.Stop', index=1,
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
  serialized_start=278,
  serialized_end=325,
)


_ROLEVOXDATA_ARRAY = _descriptor.Descriptor(
  name='RoleVoxData_Array',
  full_name='D11.Pbeans.RoleVoxData_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.RoleVoxData_Array.items', index=0,
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
  serialized_start=327,
  serialized_end=386,
)

_ROLEVOXDATA.fields_by_name['Vox1P'].message_type = _ROLEVOXDATA_VOX1P
_ROLEVOXDATA.fields_by_name['Vox3P'].message_type = _ROLEVOXDATA_VOX3P
_ROLEVOXDATA_ARRAY.fields_by_name['items'].message_type = _ROLEVOXDATA
DESCRIPTOR.message_types_by_name['RoleVoxData'] = _ROLEVOXDATA
DESCRIPTOR.message_types_by_name['RoleVoxData_Vox1P'] = _ROLEVOXDATA_VOX1P
DESCRIPTOR.message_types_by_name['RoleVoxData_Vox3P'] = _ROLEVOXDATA_VOX3P
DESCRIPTOR.message_types_by_name['RoleVoxData_Array'] = _ROLEVOXDATA_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleVoxData = _reflection.GeneratedProtocolMessageType('RoleVoxData', (_message.Message,), {
  'DESCRIPTOR' : _ROLEVOXDATA,
  '__module__' : 'xls_beans_rolevoxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleVoxData)
  })
_sym_db.RegisterMessage(RoleVoxData)

RoleVoxData_Vox1P = _reflection.GeneratedProtocolMessageType('RoleVoxData_Vox1P', (_message.Message,), {
  'DESCRIPTOR' : _ROLEVOXDATA_VOX1P,
  '__module__' : 'xls_beans_rolevoxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleVoxData_Vox1P)
  })
_sym_db.RegisterMessage(RoleVoxData_Vox1P)

RoleVoxData_Vox3P = _reflection.GeneratedProtocolMessageType('RoleVoxData_Vox3P', (_message.Message,), {
  'DESCRIPTOR' : _ROLEVOXDATA_VOX3P,
  '__module__' : 'xls_beans_rolevoxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleVoxData_Vox3P)
  })
_sym_db.RegisterMessage(RoleVoxData_Vox3P)

RoleVoxData_Array = _reflection.GeneratedProtocolMessageType('RoleVoxData_Array', (_message.Message,), {
  'DESCRIPTOR' : _ROLEVOXDATA_ARRAY,
  '__module__' : 'xls_beans_rolevoxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleVoxData_Array)
  })
_sym_db.RegisterMessage(RoleVoxData_Array)


# @@protoc_insertion_point(module_scope)