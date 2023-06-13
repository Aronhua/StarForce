# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_matchrankseason.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_matchrankseason.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fxls_beans_matchrankseason.proto\x12\nD11.Pbeans\"\xc8\x01\n\x0fMatchRankSeason\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0fseasonStartTime\x18\x03 \x01(\x03\x12\x15\n\rseasonEndTime\x18\x04 \x01(\x03\x12\x12\n\nseasonYear\x18\x05 \x01(\r\x12\x11\n\tvideoPath\x18\x06 \x01(\t\x12\x0e\n\x06\x62gPath\x18\x07 \x01(\t\x12\x1a\n\x12\x64isplayAwardBgPath\x18\x08 \x01(\t\x12\x18\n\x10\x64isplayAwardDesc\x18\t \x01(\t\"C\n\x15MatchRankSeason_Array\x12*\n\x05items\x18\x01 \x03(\x0b\x32\x1b.D11.Pbeans.MatchRankSeasonb\x06proto3')
)




_MATCHRANKSEASON = _descriptor.Descriptor(
  name='MatchRankSeason',
  full_name='D11.Pbeans.MatchRankSeason',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.MatchRankSeason.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.MatchRankSeason.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seasonStartTime', full_name='D11.Pbeans.MatchRankSeason.seasonStartTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seasonEndTime', full_name='D11.Pbeans.MatchRankSeason.seasonEndTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seasonYear', full_name='D11.Pbeans.MatchRankSeason.seasonYear', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='videoPath', full_name='D11.Pbeans.MatchRankSeason.videoPath', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bgPath', full_name='D11.Pbeans.MatchRankSeason.bgPath', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayAwardBgPath', full_name='D11.Pbeans.MatchRankSeason.displayAwardBgPath', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayAwardDesc', full_name='D11.Pbeans.MatchRankSeason.displayAwardDesc', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=48,
  serialized_end=248,
)


_MATCHRANKSEASON_ARRAY = _descriptor.Descriptor(
  name='MatchRankSeason_Array',
  full_name='D11.Pbeans.MatchRankSeason_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.MatchRankSeason_Array.items', index=0,
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
  serialized_start=250,
  serialized_end=317,
)

_MATCHRANKSEASON_ARRAY.fields_by_name['items'].message_type = _MATCHRANKSEASON
DESCRIPTOR.message_types_by_name['MatchRankSeason'] = _MATCHRANKSEASON
DESCRIPTOR.message_types_by_name['MatchRankSeason_Array'] = _MATCHRANKSEASON_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchRankSeason = _reflection.GeneratedProtocolMessageType('MatchRankSeason', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRANKSEASON,
  '__module__' : 'xls_beans_matchrankseason_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRankSeason)
  })
_sym_db.RegisterMessage(MatchRankSeason)

MatchRankSeason_Array = _reflection.GeneratedProtocolMessageType('MatchRankSeason_Array', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRANKSEASON_ARRAY,
  '__module__' : 'xls_beans_matchrankseason_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRankSeason_Array)
  })
_sym_db.RegisterMessage(MatchRankSeason_Array)


# @@protoc_insertion_point(module_scope)