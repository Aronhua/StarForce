# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_matchroboteloscore.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_matchroboteloscore.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"xls_beans_matchroboteloscore.proto\x12\nD11.Pbeans\"2\n\x12MatchRobotEloScore\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08MatchElo\x18\x02 \x01(\r\"I\n\x18MatchRobotEloScore_Array\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.D11.Pbeans.MatchRobotEloScoreb\x06proto3')
)




_MATCHROBOTELOSCORE = _descriptor.Descriptor(
  name='MatchRobotEloScore',
  full_name='D11.Pbeans.MatchRobotEloScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.MatchRobotEloScore.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MatchElo', full_name='D11.Pbeans.MatchRobotEloScore.MatchElo', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=50,
  serialized_end=100,
)


_MATCHROBOTELOSCORE_ARRAY = _descriptor.Descriptor(
  name='MatchRobotEloScore_Array',
  full_name='D11.Pbeans.MatchRobotEloScore_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.MatchRobotEloScore_Array.items', index=0,
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
  serialized_start=102,
  serialized_end=175,
)

_MATCHROBOTELOSCORE_ARRAY.fields_by_name['items'].message_type = _MATCHROBOTELOSCORE
DESCRIPTOR.message_types_by_name['MatchRobotEloScore'] = _MATCHROBOTELOSCORE
DESCRIPTOR.message_types_by_name['MatchRobotEloScore_Array'] = _MATCHROBOTELOSCORE_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchRobotEloScore = _reflection.GeneratedProtocolMessageType('MatchRobotEloScore', (_message.Message,), {
  'DESCRIPTOR' : _MATCHROBOTELOSCORE,
  '__module__' : 'xls_beans_matchroboteloscore_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRobotEloScore)
  })
_sym_db.RegisterMessage(MatchRobotEloScore)

MatchRobotEloScore_Array = _reflection.GeneratedProtocolMessageType('MatchRobotEloScore_Array', (_message.Message,), {
  'DESCRIPTOR' : _MATCHROBOTELOSCORE_ARRAY,
  '__module__' : 'xls_beans_matchroboteloscore_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRobotEloScore_Array)
  })
_sym_db.RegisterMessage(MatchRobotEloScore_Array)


# @@protoc_insertion_point(module_scope)