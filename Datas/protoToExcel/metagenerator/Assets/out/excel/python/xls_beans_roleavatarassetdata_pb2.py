# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_roleavatarassetdata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_roleavatarassetdata.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#xls_beans_roleavatarassetdata.proto\x12\nD11.Pbeans\"\xb5\x01\n\x13RoleAvatarAssetData\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04\x63\x61mp\x18\x02 \x01(\t\x12\x12\n\nfallbackid\x18\x03 \x01(\r\x12\x13\n\x0b\x66passetname\x18\x04 \x01(\t\x12\x13\n\x0btpassetname\x18\x05 \x01(\t\x12\x18\n\x10\x66pchestassetname\x18\x06 \x01(\t\x12\x11\n\trobotUsed\x18\x07 \x01(\r\x12\x19\n\x11\x45nterSceneVoiceId\x18\x08 \x01(\r\"K\n\x19RoleAvatarAssetData_Array\x12.\n\x05items\x18\x01 \x03(\x0b\x32\x1f.D11.Pbeans.RoleAvatarAssetDatab\x06proto3')
)




_ROLEAVATARASSETDATA = _descriptor.Descriptor(
  name='RoleAvatarAssetData',
  full_name='D11.Pbeans.RoleAvatarAssetData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.RoleAvatarAssetData.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camp', full_name='D11.Pbeans.RoleAvatarAssetData.camp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fallbackid', full_name='D11.Pbeans.RoleAvatarAssetData.fallbackid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fpassetname', full_name='D11.Pbeans.RoleAvatarAssetData.fpassetname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tpassetname', full_name='D11.Pbeans.RoleAvatarAssetData.tpassetname', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fpchestassetname', full_name='D11.Pbeans.RoleAvatarAssetData.fpchestassetname', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robotUsed', full_name='D11.Pbeans.RoleAvatarAssetData.robotUsed', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EnterSceneVoiceId', full_name='D11.Pbeans.RoleAvatarAssetData.EnterSceneVoiceId', index=7,
      number=8, type=13, cpp_type=3, label=1,
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
  serialized_start=52,
  serialized_end=233,
)


_ROLEAVATARASSETDATA_ARRAY = _descriptor.Descriptor(
  name='RoleAvatarAssetData_Array',
  full_name='D11.Pbeans.RoleAvatarAssetData_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.RoleAvatarAssetData_Array.items', index=0,
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
  serialized_start=235,
  serialized_end=310,
)

_ROLEAVATARASSETDATA_ARRAY.fields_by_name['items'].message_type = _ROLEAVATARASSETDATA
DESCRIPTOR.message_types_by_name['RoleAvatarAssetData'] = _ROLEAVATARASSETDATA
DESCRIPTOR.message_types_by_name['RoleAvatarAssetData_Array'] = _ROLEAVATARASSETDATA_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAvatarAssetData = _reflection.GeneratedProtocolMessageType('RoleAvatarAssetData', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAVATARASSETDATA,
  '__module__' : 'xls_beans_roleavatarassetdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleAvatarAssetData)
  })
_sym_db.RegisterMessage(RoleAvatarAssetData)

RoleAvatarAssetData_Array = _reflection.GeneratedProtocolMessageType('RoleAvatarAssetData_Array', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAVATARASSETDATA_ARRAY,
  '__module__' : 'xls_beans_roleavatarassetdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.RoleAvatarAssetData_Array)
  })
_sym_db.RegisterMessage(RoleAvatarAssetData_Array)


# @@protoc_insertion_point(module_scope)