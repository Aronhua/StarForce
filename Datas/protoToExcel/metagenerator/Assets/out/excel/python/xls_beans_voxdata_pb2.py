# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_voxdata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_voxdata.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17xls_beans_voxdata.proto\x12\nD11.Pbeans\"\x80\x05\n\x07VoxData\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\nobjectType\x18\x02 \x01(\r\x12\x10\n\x08playMode\x18\x03 \x03(\r\x12\x12\n\nunPlayMode\x18\x04 \x03(\r\x12\x15\n\risGlobalVoice\x18\x05 \x01(\x08\x12\x12\n\nstopAllVox\x18\x06 \x01(\x08\x12\x12\n\nfrontEvent\x18\x07 \x01(\t\x12\x14\n\x0cvoxCTMaleDes\x18\x08 \x01(\t\x12\x16\n\x0evoxCTFeMaleDes\x18\t \x01(\t\x12\x13\n\x0bvoxTMaleDes\x18\n \x01(\t\x12\x15\n\rvoxTFeMaleDes\x18\x0b \x01(\t\x12\x30\n\tctMale_1P\x18\x0c \x01(\x0b\x32\x1d.D11.Pbeans.VoxData_ctMale_1P\x12\x30\n\tctMale_3P\x18\r \x01(\x0b\x32\x1d.D11.Pbeans.VoxData_ctMale_3P\x12\x34\n\x0b\x63tFeMale_1P\x18\x0e \x01(\x0b\x32\x1f.D11.Pbeans.VoxData_ctFeMale_1P\x12\x34\n\x0b\x63tFeMale_3P\x18\x0f \x01(\x0b\x32\x1f.D11.Pbeans.VoxData_ctFeMale_3P\x12.\n\x08tMale_1P\x18\x10 \x01(\x0b\x32\x1c.D11.Pbeans.VoxData_tMale_1P\x12.\n\x08tMale_3P\x18\x11 \x01(\x0b\x32\x1c.D11.Pbeans.VoxData_tMale_3P\x12\x32\n\ntFeMale_1P\x18\x12 \x01(\x0b\x32\x1e.D11.Pbeans.VoxData_tFeMale_1P\x12\x32\n\ntFeMale_3P\x18\x13 \x01(\x0b\x32\x1e.D11.Pbeans.VoxData_tFeMale_3P\"/\n\x11VoxData_ctMale_1P\x12\x0c\n\x04play\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\t\"/\n\x11VoxData_ctMale_3P\x12\x0c\n\x04play\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\t\"1\n\x13VoxData_ctFeMale_1P\x12\x0c\n\x04play\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\t\"1\n\x13VoxData_ctFeMale_3P\x12\x0c\n\x04play\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\t\".\n\x10VoxData_tMale_1P\x12\x0c\n\x04play\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\t\".\n\x10VoxData_tMale_3P\x12\x0c\n\x04play\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\t\"0\n\x12VoxData_tFeMale_1P\x12\x0c\n\x04play\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\t\"0\n\x12VoxData_tFeMale_3P\x12\x0c\n\x04play\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\t\"3\n\rVoxData_Array\x12\"\n\x05items\x18\x01 \x03(\x0b\x32\x13.D11.Pbeans.VoxDatab\x06proto3')
)




_VOXDATA = _descriptor.Descriptor(
  name='VoxData',
  full_name='D11.Pbeans.VoxData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.VoxData.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectType', full_name='D11.Pbeans.VoxData.objectType', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playMode', full_name='D11.Pbeans.VoxData.playMode', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unPlayMode', full_name='D11.Pbeans.VoxData.unPlayMode', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isGlobalVoice', full_name='D11.Pbeans.VoxData.isGlobalVoice', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stopAllVox', full_name='D11.Pbeans.VoxData.stopAllVox', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frontEvent', full_name='D11.Pbeans.VoxData.frontEvent', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voxCTMaleDes', full_name='D11.Pbeans.VoxData.voxCTMaleDes', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voxCTFeMaleDes', full_name='D11.Pbeans.VoxData.voxCTFeMaleDes', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voxTMaleDes', full_name='D11.Pbeans.VoxData.voxTMaleDes', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voxTFeMaleDes', full_name='D11.Pbeans.VoxData.voxTFeMaleDes', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctMale_1P', full_name='D11.Pbeans.VoxData.ctMale_1P', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctMale_3P', full_name='D11.Pbeans.VoxData.ctMale_3P', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctFeMale_1P', full_name='D11.Pbeans.VoxData.ctFeMale_1P', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctFeMale_3P', full_name='D11.Pbeans.VoxData.ctFeMale_3P', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tMale_1P', full_name='D11.Pbeans.VoxData.tMale_1P', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tMale_3P', full_name='D11.Pbeans.VoxData.tMale_3P', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tFeMale_1P', full_name='D11.Pbeans.VoxData.tFeMale_1P', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tFeMale_3P', full_name='D11.Pbeans.VoxData.tFeMale_3P', index=18,
      number=19, type=11, cpp_type=10, label=1,
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
  serialized_start=40,
  serialized_end=680,
)


_VOXDATA_CTMALE_1P = _descriptor.Descriptor(
  name='VoxData_ctMale_1P',
  full_name='D11.Pbeans.VoxData_ctMale_1P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='D11.Pbeans.VoxData_ctMale_1P.play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='D11.Pbeans.VoxData_ctMale_1P.stop', index=1,
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
  serialized_start=682,
  serialized_end=729,
)


_VOXDATA_CTMALE_3P = _descriptor.Descriptor(
  name='VoxData_ctMale_3P',
  full_name='D11.Pbeans.VoxData_ctMale_3P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='D11.Pbeans.VoxData_ctMale_3P.play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='D11.Pbeans.VoxData_ctMale_3P.stop', index=1,
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
  serialized_start=731,
  serialized_end=778,
)


_VOXDATA_CTFEMALE_1P = _descriptor.Descriptor(
  name='VoxData_ctFeMale_1P',
  full_name='D11.Pbeans.VoxData_ctFeMale_1P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='D11.Pbeans.VoxData_ctFeMale_1P.play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='D11.Pbeans.VoxData_ctFeMale_1P.stop', index=1,
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
  serialized_start=780,
  serialized_end=829,
)


_VOXDATA_CTFEMALE_3P = _descriptor.Descriptor(
  name='VoxData_ctFeMale_3P',
  full_name='D11.Pbeans.VoxData_ctFeMale_3P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='D11.Pbeans.VoxData_ctFeMale_3P.play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='D11.Pbeans.VoxData_ctFeMale_3P.stop', index=1,
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
  serialized_start=831,
  serialized_end=880,
)


_VOXDATA_TMALE_1P = _descriptor.Descriptor(
  name='VoxData_tMale_1P',
  full_name='D11.Pbeans.VoxData_tMale_1P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='D11.Pbeans.VoxData_tMale_1P.play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='D11.Pbeans.VoxData_tMale_1P.stop', index=1,
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
  serialized_start=882,
  serialized_end=928,
)


_VOXDATA_TMALE_3P = _descriptor.Descriptor(
  name='VoxData_tMale_3P',
  full_name='D11.Pbeans.VoxData_tMale_3P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='D11.Pbeans.VoxData_tMale_3P.play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='D11.Pbeans.VoxData_tMale_3P.stop', index=1,
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
  serialized_start=930,
  serialized_end=976,
)


_VOXDATA_TFEMALE_1P = _descriptor.Descriptor(
  name='VoxData_tFeMale_1P',
  full_name='D11.Pbeans.VoxData_tFeMale_1P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='D11.Pbeans.VoxData_tFeMale_1P.play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='D11.Pbeans.VoxData_tFeMale_1P.stop', index=1,
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
  serialized_start=978,
  serialized_end=1026,
)


_VOXDATA_TFEMALE_3P = _descriptor.Descriptor(
  name='VoxData_tFeMale_3P',
  full_name='D11.Pbeans.VoxData_tFeMale_3P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='D11.Pbeans.VoxData_tFeMale_3P.play', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='D11.Pbeans.VoxData_tFeMale_3P.stop', index=1,
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
  serialized_start=1028,
  serialized_end=1076,
)


_VOXDATA_ARRAY = _descriptor.Descriptor(
  name='VoxData_Array',
  full_name='D11.Pbeans.VoxData_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.VoxData_Array.items', index=0,
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
  serialized_start=1078,
  serialized_end=1129,
)

_VOXDATA.fields_by_name['ctMale_1P'].message_type = _VOXDATA_CTMALE_1P
_VOXDATA.fields_by_name['ctMale_3P'].message_type = _VOXDATA_CTMALE_3P
_VOXDATA.fields_by_name['ctFeMale_1P'].message_type = _VOXDATA_CTFEMALE_1P
_VOXDATA.fields_by_name['ctFeMale_3P'].message_type = _VOXDATA_CTFEMALE_3P
_VOXDATA.fields_by_name['tMale_1P'].message_type = _VOXDATA_TMALE_1P
_VOXDATA.fields_by_name['tMale_3P'].message_type = _VOXDATA_TMALE_3P
_VOXDATA.fields_by_name['tFeMale_1P'].message_type = _VOXDATA_TFEMALE_1P
_VOXDATA.fields_by_name['tFeMale_3P'].message_type = _VOXDATA_TFEMALE_3P
_VOXDATA_ARRAY.fields_by_name['items'].message_type = _VOXDATA
DESCRIPTOR.message_types_by_name['VoxData'] = _VOXDATA
DESCRIPTOR.message_types_by_name['VoxData_ctMale_1P'] = _VOXDATA_CTMALE_1P
DESCRIPTOR.message_types_by_name['VoxData_ctMale_3P'] = _VOXDATA_CTMALE_3P
DESCRIPTOR.message_types_by_name['VoxData_ctFeMale_1P'] = _VOXDATA_CTFEMALE_1P
DESCRIPTOR.message_types_by_name['VoxData_ctFeMale_3P'] = _VOXDATA_CTFEMALE_3P
DESCRIPTOR.message_types_by_name['VoxData_tMale_1P'] = _VOXDATA_TMALE_1P
DESCRIPTOR.message_types_by_name['VoxData_tMale_3P'] = _VOXDATA_TMALE_3P
DESCRIPTOR.message_types_by_name['VoxData_tFeMale_1P'] = _VOXDATA_TFEMALE_1P
DESCRIPTOR.message_types_by_name['VoxData_tFeMale_3P'] = _VOXDATA_TFEMALE_3P
DESCRIPTOR.message_types_by_name['VoxData_Array'] = _VOXDATA_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VoxData = _reflection.GeneratedProtocolMessageType('VoxData', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData)
  })
_sym_db.RegisterMessage(VoxData)

VoxData_ctMale_1P = _reflection.GeneratedProtocolMessageType('VoxData_ctMale_1P', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_CTMALE_1P,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_ctMale_1P)
  })
_sym_db.RegisterMessage(VoxData_ctMale_1P)

VoxData_ctMale_3P = _reflection.GeneratedProtocolMessageType('VoxData_ctMale_3P', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_CTMALE_3P,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_ctMale_3P)
  })
_sym_db.RegisterMessage(VoxData_ctMale_3P)

VoxData_ctFeMale_1P = _reflection.GeneratedProtocolMessageType('VoxData_ctFeMale_1P', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_CTFEMALE_1P,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_ctFeMale_1P)
  })
_sym_db.RegisterMessage(VoxData_ctFeMale_1P)

VoxData_ctFeMale_3P = _reflection.GeneratedProtocolMessageType('VoxData_ctFeMale_3P', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_CTFEMALE_3P,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_ctFeMale_3P)
  })
_sym_db.RegisterMessage(VoxData_ctFeMale_3P)

VoxData_tMale_1P = _reflection.GeneratedProtocolMessageType('VoxData_tMale_1P', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_TMALE_1P,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_tMale_1P)
  })
_sym_db.RegisterMessage(VoxData_tMale_1P)

VoxData_tMale_3P = _reflection.GeneratedProtocolMessageType('VoxData_tMale_3P', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_TMALE_3P,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_tMale_3P)
  })
_sym_db.RegisterMessage(VoxData_tMale_3P)

VoxData_tFeMale_1P = _reflection.GeneratedProtocolMessageType('VoxData_tFeMale_1P', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_TFEMALE_1P,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_tFeMale_1P)
  })
_sym_db.RegisterMessage(VoxData_tFeMale_1P)

VoxData_tFeMale_3P = _reflection.GeneratedProtocolMessageType('VoxData_tFeMale_3P', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_TFEMALE_3P,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_tFeMale_3P)
  })
_sym_db.RegisterMessage(VoxData_tFeMale_3P)

VoxData_Array = _reflection.GeneratedProtocolMessageType('VoxData_Array', (_message.Message,), {
  'DESCRIPTOR' : _VOXDATA_ARRAY,
  '__module__' : 'xls_beans_voxdata_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.VoxData_Array)
  })
_sym_db.RegisterMessage(VoxData_Array)


# @@protoc_insertion_point(module_scope)