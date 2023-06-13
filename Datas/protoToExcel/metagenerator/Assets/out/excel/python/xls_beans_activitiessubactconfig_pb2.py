# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_activitiessubactconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_activitiessubactconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&xls_beans_activitiessubactconfig.proto\x12\nD11.Pbeans\"\xe3\x02\n\x16\x41\x63tivitiesSubActConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tstartTime\x18\x03 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x03\x12\x10\n\x08startDay\x18\x05 \x01(\r\x12\x0e\n\x06\x65ndDay\x18\x06 \x01(\r\x12\x11\n\tcycleType\x18\x07 \x01(\t\x12\x16\n\x0e\x63ycleStartDate\x18\x08 \x01(\r\x12\x14\n\x0c\x63ycleEndDate\x18\t \x01(\r\x12\x11\n\tcatalogId\x18\n \x01(\r\x12=\n\x08showCond\x18\x0b \x03(\x0b\x32+.D11.Pbeans.ActivitiesSubActConfig_showCond\x12\x15\n\rbackgroundImg\x18\x0c \x01(\r\x12\x18\n\x10navigateFuncName\x18\r \x01(\t\x12\x15\n\rnavigateParam\x18\x0e \x01(\r\x12\x0e\n\x06webURL\x18\x0f \x01(\t\"D\n\x1f\x41\x63tivitiesSubActConfig_showCond\x12\x0e\n\x06\x63ondId\x18\x01 \x01(\t\x12\x11\n\tcondValue\x18\x02 \x01(\r\"Q\n\x1c\x41\x63tivitiesSubActConfig_Array\x12\x31\n\x05items\x18\x01 \x03(\x0b\x32\".D11.Pbeans.ActivitiesSubActConfigb\x06proto3')
)




_ACTIVITIESSUBACTCONFIG = _descriptor.Descriptor(
  name='ActivitiesSubActConfig',
  full_name='D11.Pbeans.ActivitiesSubActConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.ActivitiesSubActConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.ActivitiesSubActConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='D11.Pbeans.ActivitiesSubActConfig.startTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='D11.Pbeans.ActivitiesSubActConfig.endTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startDay', full_name='D11.Pbeans.ActivitiesSubActConfig.startDay', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endDay', full_name='D11.Pbeans.ActivitiesSubActConfig.endDay', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cycleType', full_name='D11.Pbeans.ActivitiesSubActConfig.cycleType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cycleStartDate', full_name='D11.Pbeans.ActivitiesSubActConfig.cycleStartDate', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cycleEndDate', full_name='D11.Pbeans.ActivitiesSubActConfig.cycleEndDate', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='catalogId', full_name='D11.Pbeans.ActivitiesSubActConfig.catalogId', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showCond', full_name='D11.Pbeans.ActivitiesSubActConfig.showCond', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backgroundImg', full_name='D11.Pbeans.ActivitiesSubActConfig.backgroundImg', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigateFuncName', full_name='D11.Pbeans.ActivitiesSubActConfig.navigateFuncName', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigateParam', full_name='D11.Pbeans.ActivitiesSubActConfig.navigateParam', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='webURL', full_name='D11.Pbeans.ActivitiesSubActConfig.webURL', index=14,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=55,
  serialized_end=410,
)


_ACTIVITIESSUBACTCONFIG_SHOWCOND = _descriptor.Descriptor(
  name='ActivitiesSubActConfig_showCond',
  full_name='D11.Pbeans.ActivitiesSubActConfig_showCond',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condId', full_name='D11.Pbeans.ActivitiesSubActConfig_showCond.condId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condValue', full_name='D11.Pbeans.ActivitiesSubActConfig_showCond.condValue', index=1,
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
  serialized_start=412,
  serialized_end=480,
)


_ACTIVITIESSUBACTCONFIG_ARRAY = _descriptor.Descriptor(
  name='ActivitiesSubActConfig_Array',
  full_name='D11.Pbeans.ActivitiesSubActConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.ActivitiesSubActConfig_Array.items', index=0,
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
  serialized_start=482,
  serialized_end=563,
)

_ACTIVITIESSUBACTCONFIG.fields_by_name['showCond'].message_type = _ACTIVITIESSUBACTCONFIG_SHOWCOND
_ACTIVITIESSUBACTCONFIG_ARRAY.fields_by_name['items'].message_type = _ACTIVITIESSUBACTCONFIG
DESCRIPTOR.message_types_by_name['ActivitiesSubActConfig'] = _ACTIVITIESSUBACTCONFIG
DESCRIPTOR.message_types_by_name['ActivitiesSubActConfig_showCond'] = _ACTIVITIESSUBACTCONFIG_SHOWCOND
DESCRIPTOR.message_types_by_name['ActivitiesSubActConfig_Array'] = _ACTIVITIESSUBACTCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActivitiesSubActConfig = _reflection.GeneratedProtocolMessageType('ActivitiesSubActConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITIESSUBACTCONFIG,
  '__module__' : 'xls_beans_activitiessubactconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ActivitiesSubActConfig)
  })
_sym_db.RegisterMessage(ActivitiesSubActConfig)

ActivitiesSubActConfig_showCond = _reflection.GeneratedProtocolMessageType('ActivitiesSubActConfig_showCond', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITIESSUBACTCONFIG_SHOWCOND,
  '__module__' : 'xls_beans_activitiessubactconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ActivitiesSubActConfig_showCond)
  })
_sym_db.RegisterMessage(ActivitiesSubActConfig_showCond)

ActivitiesSubActConfig_Array = _reflection.GeneratedProtocolMessageType('ActivitiesSubActConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITIESSUBACTCONFIG_ARRAY,
  '__module__' : 'xls_beans_activitiessubactconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ActivitiesSubActConfig_Array)
  })
_sym_db.RegisterMessage(ActivitiesSubActConfig_Array)


# @@protoc_insertion_point(module_scope)