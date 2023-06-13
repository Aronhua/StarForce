# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_matchrankseasonaward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_matchrankseasonaward.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$xls_beans_matchrankseasonaward.proto\x12\nD11.Pbeans\"n\n\x14MatchRankSeasonAward\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\trankLevel\x18\x02 \x01(\r\x12\x37\n\x06\x65\x66\x66\x65\x63t\x18\x03 \x03(\x0b\x32\'.D11.Pbeans.MatchRankSeasonAward_effect\"~\n\x1bMatchRankSeasonAward_effect\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r\x12\x10\n\x08lockTime\x18\x03 \x01(\r\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\r\x12\x10\n\x08statTrak\x18\x05 \x01(\r\x12\x10\n\x08paintKit\x18\x06 \x01(\r\"M\n\x1aMatchRankSeasonAward_Array\x12/\n\x05items\x18\x01 \x03(\x0b\x32 .D11.Pbeans.MatchRankSeasonAwardb\x06proto3')
)




_MATCHRANKSEASONAWARD = _descriptor.Descriptor(
  name='MatchRankSeasonAward',
  full_name='D11.Pbeans.MatchRankSeasonAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.MatchRankSeasonAward.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rankLevel', full_name='D11.Pbeans.MatchRankSeasonAward.rankLevel', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effect', full_name='D11.Pbeans.MatchRankSeasonAward.effect', index=2,
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
  serialized_start=52,
  serialized_end=162,
)


_MATCHRANKSEASONAWARD_EFFECT = _descriptor.Descriptor(
  name='MatchRankSeasonAward_effect',
  full_name='D11.Pbeans.MatchRankSeasonAward_effect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.MatchRankSeasonAward_effect.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='D11.Pbeans.MatchRankSeasonAward_effect.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lockTime', full_name='D11.Pbeans.MatchRankSeasonAward_effect.lockTime', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expire', full_name='D11.Pbeans.MatchRankSeasonAward_effect.expire', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statTrak', full_name='D11.Pbeans.MatchRankSeasonAward_effect.statTrak', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paintKit', full_name='D11.Pbeans.MatchRankSeasonAward_effect.paintKit', index=5,
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
  serialized_start=164,
  serialized_end=290,
)


_MATCHRANKSEASONAWARD_ARRAY = _descriptor.Descriptor(
  name='MatchRankSeasonAward_Array',
  full_name='D11.Pbeans.MatchRankSeasonAward_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.MatchRankSeasonAward_Array.items', index=0,
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
  serialized_start=292,
  serialized_end=369,
)

_MATCHRANKSEASONAWARD.fields_by_name['effect'].message_type = _MATCHRANKSEASONAWARD_EFFECT
_MATCHRANKSEASONAWARD_ARRAY.fields_by_name['items'].message_type = _MATCHRANKSEASONAWARD
DESCRIPTOR.message_types_by_name['MatchRankSeasonAward'] = _MATCHRANKSEASONAWARD
DESCRIPTOR.message_types_by_name['MatchRankSeasonAward_effect'] = _MATCHRANKSEASONAWARD_EFFECT
DESCRIPTOR.message_types_by_name['MatchRankSeasonAward_Array'] = _MATCHRANKSEASONAWARD_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchRankSeasonAward = _reflection.GeneratedProtocolMessageType('MatchRankSeasonAward', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRANKSEASONAWARD,
  '__module__' : 'xls_beans_matchrankseasonaward_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRankSeasonAward)
  })
_sym_db.RegisterMessage(MatchRankSeasonAward)

MatchRankSeasonAward_effect = _reflection.GeneratedProtocolMessageType('MatchRankSeasonAward_effect', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRANKSEASONAWARD_EFFECT,
  '__module__' : 'xls_beans_matchrankseasonaward_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRankSeasonAward_effect)
  })
_sym_db.RegisterMessage(MatchRankSeasonAward_effect)

MatchRankSeasonAward_Array = _reflection.GeneratedProtocolMessageType('MatchRankSeasonAward_Array', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRANKSEASONAWARD_ARRAY,
  '__module__' : 'xls_beans_matchrankseasonaward_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRankSeasonAward_Array)
  })
_sym_db.RegisterMessage(MatchRankSeasonAward_Array)


# @@protoc_insertion_point(module_scope)