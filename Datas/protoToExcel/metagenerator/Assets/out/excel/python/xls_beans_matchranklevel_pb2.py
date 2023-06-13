# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_matchranklevel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_matchranklevel.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1exls_beans_matchranklevel.proto\x12\nD11.Pbeans\"\xb5\x04\n\x0eMatchRankLevel\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05grade\x18\x03 \x01(\r\x12\x11\n\tgradeStar\x18\x04 \x01(\r\x12\x17\n\x0fgradeStarAmount\x18\x05 \x01(\r\x12\x16\n\x0egradeStarScore\x18\x06 \x01(\r\x12\x0f\n\x07levelId\x18\x07 \x01(\r\x12\x0c\n\x04mode\x18\x08 \x01(\r\x12\x11\n\trankScore\x18\t \x01(\r\x12\x13\n\x0brankPercent\x18\n \x01(\x02\x12\x13\n\x0bsmallIconId\x18\x0b \x01(\r\x12\x13\n\x0blargeIconId\x18\x0c \x01(\r\x12\x16\n\x0emodelAssetName\x18\r \x01(\t\x12 \n\x18levelUpTimelineAssetPath\x18\x0e \x01(\t\x12\x18\n\x10gradeStarProtect\x18\x0f \x01(\r\x12\x18\n\x10rankScoreProtect\x18\x10 \x01(\r\x12\x10\n\x08succCond\x18\x11 \x01(\r\x12\x1a\n\x12promotionBattleCnt\x18\x12 \x01(\r\x12\x45\n\x10loseCompensation\x18\x13 \x03(\x0b\x32+.D11.Pbeans.MatchRankLevel_loseCompensation\x12\x18\n\x10newRankBaseScore\x18\x14 \x01(\r\x12\x14\n\x0c\x63onvertParam\x18\x15 \x01(\x02\x12\x18\n\x10joinMinRankLevel\x18\x16 \x01(\r\x12\x18\n\x10joinMaxRankLevel\x18\x17 \x01(\r\">\n\x1fMatchRankLevel_loseCompensation\x12\x0c\n\x04\x63ond\x18\x01 \x01(\r\x12\r\n\x05\x61ward\x18\x02 \x01(\r\"A\n\x14MatchRankLevel_Array\x12)\n\x05items\x18\x01 \x03(\x0b\x32\x1a.D11.Pbeans.MatchRankLevelb\x06proto3')
)




_MATCHRANKLEVEL = _descriptor.Descriptor(
  name='MatchRankLevel',
  full_name='D11.Pbeans.MatchRankLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.MatchRankLevel.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.MatchRankLevel.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grade', full_name='D11.Pbeans.MatchRankLevel.grade', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeStar', full_name='D11.Pbeans.MatchRankLevel.gradeStar', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeStarAmount', full_name='D11.Pbeans.MatchRankLevel.gradeStarAmount', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeStarScore', full_name='D11.Pbeans.MatchRankLevel.gradeStarScore', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='levelId', full_name='D11.Pbeans.MatchRankLevel.levelId', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='D11.Pbeans.MatchRankLevel.mode', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rankScore', full_name='D11.Pbeans.MatchRankLevel.rankScore', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rankPercent', full_name='D11.Pbeans.MatchRankLevel.rankPercent', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='smallIconId', full_name='D11.Pbeans.MatchRankLevel.smallIconId', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='largeIconId', full_name='D11.Pbeans.MatchRankLevel.largeIconId', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modelAssetName', full_name='D11.Pbeans.MatchRankLevel.modelAssetName', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='levelUpTimelineAssetPath', full_name='D11.Pbeans.MatchRankLevel.levelUpTimelineAssetPath', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeStarProtect', full_name='D11.Pbeans.MatchRankLevel.gradeStarProtect', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rankScoreProtect', full_name='D11.Pbeans.MatchRankLevel.rankScoreProtect', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='succCond', full_name='D11.Pbeans.MatchRankLevel.succCond', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='promotionBattleCnt', full_name='D11.Pbeans.MatchRankLevel.promotionBattleCnt', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loseCompensation', full_name='D11.Pbeans.MatchRankLevel.loseCompensation', index=18,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='newRankBaseScore', full_name='D11.Pbeans.MatchRankLevel.newRankBaseScore', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convertParam', full_name='D11.Pbeans.MatchRankLevel.convertParam', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='joinMinRankLevel', full_name='D11.Pbeans.MatchRankLevel.joinMinRankLevel', index=21,
      number=22, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='joinMaxRankLevel', full_name='D11.Pbeans.MatchRankLevel.joinMaxRankLevel', index=22,
      number=23, type=13, cpp_type=3, label=1,
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
  serialized_start=47,
  serialized_end=612,
)


_MATCHRANKLEVEL_LOSECOMPENSATION = _descriptor.Descriptor(
  name='MatchRankLevel_loseCompensation',
  full_name='D11.Pbeans.MatchRankLevel_loseCompensation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cond', full_name='D11.Pbeans.MatchRankLevel_loseCompensation.cond', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='award', full_name='D11.Pbeans.MatchRankLevel_loseCompensation.award', index=1,
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
  serialized_start=614,
  serialized_end=676,
)


_MATCHRANKLEVEL_ARRAY = _descriptor.Descriptor(
  name='MatchRankLevel_Array',
  full_name='D11.Pbeans.MatchRankLevel_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.MatchRankLevel_Array.items', index=0,
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
  serialized_start=678,
  serialized_end=743,
)

_MATCHRANKLEVEL.fields_by_name['loseCompensation'].message_type = _MATCHRANKLEVEL_LOSECOMPENSATION
_MATCHRANKLEVEL_ARRAY.fields_by_name['items'].message_type = _MATCHRANKLEVEL
DESCRIPTOR.message_types_by_name['MatchRankLevel'] = _MATCHRANKLEVEL
DESCRIPTOR.message_types_by_name['MatchRankLevel_loseCompensation'] = _MATCHRANKLEVEL_LOSECOMPENSATION
DESCRIPTOR.message_types_by_name['MatchRankLevel_Array'] = _MATCHRANKLEVEL_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchRankLevel = _reflection.GeneratedProtocolMessageType('MatchRankLevel', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRANKLEVEL,
  '__module__' : 'xls_beans_matchranklevel_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRankLevel)
  })
_sym_db.RegisterMessage(MatchRankLevel)

MatchRankLevel_loseCompensation = _reflection.GeneratedProtocolMessageType('MatchRankLevel_loseCompensation', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRANKLEVEL_LOSECOMPENSATION,
  '__module__' : 'xls_beans_matchranklevel_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRankLevel_loseCompensation)
  })
_sym_db.RegisterMessage(MatchRankLevel_loseCompensation)

MatchRankLevel_Array = _reflection.GeneratedProtocolMessageType('MatchRankLevel_Array', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRANKLEVEL_ARRAY,
  '__module__' : 'xls_beans_matchranklevel_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.MatchRankLevel_Array)
  })
_sym_db.RegisterMessage(MatchRankLevel_Array)


# @@protoc_insertion_point(module_scope)