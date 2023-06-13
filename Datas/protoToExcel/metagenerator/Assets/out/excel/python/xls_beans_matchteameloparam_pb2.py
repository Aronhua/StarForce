# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_matchteameloparam.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_matchteameloparam.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!xls_beans_matchteameloparam.proto\x12\nD11.Pbeans\"U\n\x11MatchTeamEloParam\x12\n\n\x02id\x18\x01 \x01(\r\x12\x34\n\x06ParamK\x18\x02 \x03(\x0b\x32$.D11.Pbeans.MatchTeamEloParam_ParamK\"j\n\x18MatchTeamEloParam_ParamK\x12\x12\n\nTeamMember\x18\x01 \x01(\r\x12\x10\n\x08\x45loParam\x18\x02 \x01(\x02\x12\x10\n\x08LvlParam\x18\x03 \x01(\x02\x12\x16\n\x0eRankScoreParam\x18\x04 \x01(\x02\"G\n\x17MatchTeamEloParam_Array\x12,\n\x05items\x18\x01 \x03(\x0b\x32\x1d.D11.Pbeans.MatchTeamEloParamb\x06proto3')
)




_MATCHTEAMELOPARAM = _descriptor.Descriptor(
  name='MatchTeamEloParam',
  full_name='D11.Pbeans.MatchTeamEloParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.MatchTeamEloParam.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ParamK', full_name='D11.Pbeans.MatchTeamEloParam.ParamK', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=49,
  serialized_end=134,
)


_MATCHTEAMELOPARAM_PARAMK = _descriptor.Descriptor(
  name='MatchTeamEloParam_ParamK',
  full_name='D11.Pbeans.MatchTeamEloParam_ParamK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TeamMember', full_name='D11.Pbeans.MatchTeamEloParam_ParamK.TeamMember', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EloParam', full_name='D11.Pbeans.MatchTeamEloParam_ParamK.EloParam', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LvlParam', full_name='D11.Pbeans.MatchTeamEloParam_ParamK.LvlParam', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RankScoreParam', full_name='D11.Pbeans.MatchTeamEloParam_ParamK.RankScoreParam', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=136,
  serialized_end=242,
)


_MATCHTEAMELOPARAM_ARRAY = _descriptor.Descriptor(
  name='MatchTeamEloParam_Array',
  full_name='D11.Pbeans.MatchTeamEloParam_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.MatchTeamEloParam_Array.items', index=0,
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
  serialized_start=244,
  serialized_end=315,
)

_MATCHTEAMELOPARAM.fields_by_name['ParamK'].message_type = _MATCHTEAMELOPARAM_PARAMK
_MATCHTEAMELOPARAM_ARRAY.fields_by_name['items'].message_type = _MATCHTEAMELOPARAM
DESCRIPTOR.message_types_by_name['MatchTeamEloParam'] = _MATCHTEAMELOPARAM
DESCRIPTOR.message_types_by_name['MatchTeamEloParam_ParamK'] = _MATCHTEAMELOPARAM_PARAMK
DESCRIPTOR.message_types_by_name['MatchTeamEloParam_Array'] = _MATCHTEAMELOPARAM_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchTeamEloParam = _reflection.GeneratedProtocolMessageType('MatchTeamEloParam', (_message.Message,), {
  'DESCRIPTOR' : _MATCHTEAMELOPARAM,
  '__module__' : 'xls_beans_matchteameloparam_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchTeamEloParam)
  })
_sym_db.RegisterMessage(MatchTeamEloParam)

MatchTeamEloParam_ParamK = _reflection.GeneratedProtocolMessageType('MatchTeamEloParam_ParamK', (_message.Message,), {
  'DESCRIPTOR' : _MATCHTEAMELOPARAM_PARAMK,
  '__module__' : 'xls_beans_matchteameloparam_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchTeamEloParam_ParamK)
  })
_sym_db.RegisterMessage(MatchTeamEloParam_ParamK)

MatchTeamEloParam_Array = _reflection.GeneratedProtocolMessageType('MatchTeamEloParam_Array', (_message.Message,), {
  'DESCRIPTOR' : _MATCHTEAMELOPARAM_ARRAY,
  '__module__' : 'xls_beans_matchteameloparam_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchTeamEloParam_Array)
  })
_sym_db.RegisterMessage(MatchTeamEloParam_Array)


# @@protoc_insertion_point(module_scope)