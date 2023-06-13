# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_caseconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_caseconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1axls_beans_caseconfig.proto\x12\nD11.Pbeans\"\x84\x02\n\nCaseConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12+\n\x05limit\x18\x02 \x03(\x0b\x32\x1c.D11.Pbeans.CaseConfig_limit\x12)\n\x04\x63ost\x18\x03 \x03(\x0b\x32\x1b.D11.Pbeans.CaseConfig_cost\x12\x10\n\x08\x64ropRule\x18\x04 \x01(\r\x12\x10\n\x08\x64ropType\x18\x05 \x01(\r\x12\x0e\n\x06\x64ropID\x18\x06 \x01(\r\x12\x31\n\x08\x63ontrols\x18\x07 \x03(\x0b\x32\x1f.D11.Pbeans.CaseConfig_controls\x12+\n\x05rules\x18\x08 \x03(\x0b\x32\x1c.D11.Pbeans.CaseConfig_rules\"-\n\x10\x43\x61seConfig_limit\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r\",\n\x0f\x43\x61seConfig_cost\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r\"I\n\x13\x43\x61seConfig_controls\x12\x10\n\x08minCount\x18\x01 \x01(\r\x12\x10\n\x08maxCount\x18\x02 \x01(\r\x12\x0e\n\x06\x64ropID\x18\x03 \x01(\r\"R\n\x10\x43\x61seConfig_rules\x12\x10\n\x08priority\x18\x01 \x01(\r\x12\r\n\x05level\x18\x02 \x01(\r\x12\r\n\x05\x63ount\x18\x03 \x01(\r\x12\x0e\n\x06\x64ropID\x18\x04 \x01(\r\"9\n\x10\x43\x61seConfig_Array\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x16.D11.Pbeans.CaseConfigb\x06proto3')
)




_CASECONFIG = _descriptor.Descriptor(
  name='CaseConfig',
  full_name='D11.Pbeans.CaseConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.CaseConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='D11.Pbeans.CaseConfig.limit', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='D11.Pbeans.CaseConfig.cost', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropRule', full_name='D11.Pbeans.CaseConfig.dropRule', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropType', full_name='D11.Pbeans.CaseConfig.dropType', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropID', full_name='D11.Pbeans.CaseConfig.dropID', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controls', full_name='D11.Pbeans.CaseConfig.controls', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='D11.Pbeans.CaseConfig.rules', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=43,
  serialized_end=303,
)


_CASECONFIG_LIMIT = _descriptor.Descriptor(
  name='CaseConfig_limit',
  full_name='D11.Pbeans.CaseConfig_limit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.CaseConfig_limit.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='D11.Pbeans.CaseConfig_limit.value', index=1,
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
  serialized_start=305,
  serialized_end=350,
)


_CASECONFIG_COST = _descriptor.Descriptor(
  name='CaseConfig_cost',
  full_name='D11.Pbeans.CaseConfig_cost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.CaseConfig_cost.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='D11.Pbeans.CaseConfig_cost.value', index=1,
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
  serialized_start=352,
  serialized_end=396,
)


_CASECONFIG_CONTROLS = _descriptor.Descriptor(
  name='CaseConfig_controls',
  full_name='D11.Pbeans.CaseConfig_controls',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minCount', full_name='D11.Pbeans.CaseConfig_controls.minCount', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxCount', full_name='D11.Pbeans.CaseConfig_controls.maxCount', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropID', full_name='D11.Pbeans.CaseConfig_controls.dropID', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=398,
  serialized_end=471,
)


_CASECONFIG_RULES = _descriptor.Descriptor(
  name='CaseConfig_rules',
  full_name='D11.Pbeans.CaseConfig_rules',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='D11.Pbeans.CaseConfig_rules.priority', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='D11.Pbeans.CaseConfig_rules.level', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='D11.Pbeans.CaseConfig_rules.count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropID', full_name='D11.Pbeans.CaseConfig_rules.dropID', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=473,
  serialized_end=555,
)


_CASECONFIG_ARRAY = _descriptor.Descriptor(
  name='CaseConfig_Array',
  full_name='D11.Pbeans.CaseConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.CaseConfig_Array.items', index=0,
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
  serialized_start=557,
  serialized_end=614,
)

_CASECONFIG.fields_by_name['limit'].message_type = _CASECONFIG_LIMIT
_CASECONFIG.fields_by_name['cost'].message_type = _CASECONFIG_COST
_CASECONFIG.fields_by_name['controls'].message_type = _CASECONFIG_CONTROLS
_CASECONFIG.fields_by_name['rules'].message_type = _CASECONFIG_RULES
_CASECONFIG_ARRAY.fields_by_name['items'].message_type = _CASECONFIG
DESCRIPTOR.message_types_by_name['CaseConfig'] = _CASECONFIG
DESCRIPTOR.message_types_by_name['CaseConfig_limit'] = _CASECONFIG_LIMIT
DESCRIPTOR.message_types_by_name['CaseConfig_cost'] = _CASECONFIG_COST
DESCRIPTOR.message_types_by_name['CaseConfig_controls'] = _CASECONFIG_CONTROLS
DESCRIPTOR.message_types_by_name['CaseConfig_rules'] = _CASECONFIG_RULES
DESCRIPTOR.message_types_by_name['CaseConfig_Array'] = _CASECONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CaseConfig = _reflection.GeneratedProtocolMessageType('CaseConfig', (_message.Message,), {
  'DESCRIPTOR' : _CASECONFIG,
  '__module__' : 'xls_beans_caseconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseConfig)
  })
_sym_db.RegisterMessage(CaseConfig)

CaseConfig_limit = _reflection.GeneratedProtocolMessageType('CaseConfig_limit', (_message.Message,), {
  'DESCRIPTOR' : _CASECONFIG_LIMIT,
  '__module__' : 'xls_beans_caseconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseConfig_limit)
  })
_sym_db.RegisterMessage(CaseConfig_limit)

CaseConfig_cost = _reflection.GeneratedProtocolMessageType('CaseConfig_cost', (_message.Message,), {
  'DESCRIPTOR' : _CASECONFIG_COST,
  '__module__' : 'xls_beans_caseconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseConfig_cost)
  })
_sym_db.RegisterMessage(CaseConfig_cost)

CaseConfig_controls = _reflection.GeneratedProtocolMessageType('CaseConfig_controls', (_message.Message,), {
  'DESCRIPTOR' : _CASECONFIG_CONTROLS,
  '__module__' : 'xls_beans_caseconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseConfig_controls)
  })
_sym_db.RegisterMessage(CaseConfig_controls)

CaseConfig_rules = _reflection.GeneratedProtocolMessageType('CaseConfig_rules', (_message.Message,), {
  'DESCRIPTOR' : _CASECONFIG_RULES,
  '__module__' : 'xls_beans_caseconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseConfig_rules)
  })
_sym_db.RegisterMessage(CaseConfig_rules)

CaseConfig_Array = _reflection.GeneratedProtocolMessageType('CaseConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _CASECONFIG_ARRAY,
  '__module__' : 'xls_beans_caseconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.CaseConfig_Array)
  })
_sym_db.RegisterMessage(CaseConfig_Array)


# @@protoc_insertion_point(module_scope)