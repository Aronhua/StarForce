# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_luckystrikecosts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_luckystrikecosts.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n xls_beans_luckystrikecosts.proto\x12\nD11.Pbeans\"\x8c\x01\n\x10LuckyStrikeCosts\x12\n\n\x02id\x18\x01 \x01(\r\x12\x39\n\tdiscounts\x18\x02 \x03(\x0b\x32&.D11.Pbeans.LuckyStrikeCosts_discounts\x12\x31\n\x05\x63osts\x18\x03 \x03(\x0b\x32\".D11.Pbeans.LuckyStrikeCosts_costs\"R\n\x1aLuckyStrikeCosts_discounts\x12\x11\n\tstartTime\x18\x01 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\x03\x12\x10\n\x08\x64iscount\x18\x03 \x01(\r\"B\n\x16LuckyStrikeCosts_costs\x12\r\n\x05\x63ount\x18\x01 \x01(\r\x12\n\n\x02id\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\r\"E\n\x16LuckyStrikeCosts_Array\x12+\n\x05items\x18\x01 \x03(\x0b\x32\x1c.D11.Pbeans.LuckyStrikeCostsb\x06proto3')
)




_LUCKYSTRIKECOSTS = _descriptor.Descriptor(
  name='LuckyStrikeCosts',
  full_name='D11.Pbeans.LuckyStrikeCosts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.LuckyStrikeCosts.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discounts', full_name='D11.Pbeans.LuckyStrikeCosts.discounts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='costs', full_name='D11.Pbeans.LuckyStrikeCosts.costs', index=2,
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
  serialized_start=49,
  serialized_end=189,
)


_LUCKYSTRIKECOSTS_DISCOUNTS = _descriptor.Descriptor(
  name='LuckyStrikeCosts_discounts',
  full_name='D11.Pbeans.LuckyStrikeCosts_discounts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startTime', full_name='D11.Pbeans.LuckyStrikeCosts_discounts.startTime', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='D11.Pbeans.LuckyStrikeCosts_discounts.endTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discount', full_name='D11.Pbeans.LuckyStrikeCosts_discounts.discount', index=2,
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
  serialized_start=191,
  serialized_end=273,
)


_LUCKYSTRIKECOSTS_COSTS = _descriptor.Descriptor(
  name='LuckyStrikeCosts_costs',
  full_name='D11.Pbeans.LuckyStrikeCosts_costs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='D11.Pbeans.LuckyStrikeCosts_costs.count', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.LuckyStrikeCosts_costs.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='D11.Pbeans.LuckyStrikeCosts_costs.value', index=2,
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
  serialized_start=275,
  serialized_end=341,
)


_LUCKYSTRIKECOSTS_ARRAY = _descriptor.Descriptor(
  name='LuckyStrikeCosts_Array',
  full_name='D11.Pbeans.LuckyStrikeCosts_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.LuckyStrikeCosts_Array.items', index=0,
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
  serialized_start=343,
  serialized_end=412,
)

_LUCKYSTRIKECOSTS.fields_by_name['discounts'].message_type = _LUCKYSTRIKECOSTS_DISCOUNTS
_LUCKYSTRIKECOSTS.fields_by_name['costs'].message_type = _LUCKYSTRIKECOSTS_COSTS
_LUCKYSTRIKECOSTS_ARRAY.fields_by_name['items'].message_type = _LUCKYSTRIKECOSTS
DESCRIPTOR.message_types_by_name['LuckyStrikeCosts'] = _LUCKYSTRIKECOSTS
DESCRIPTOR.message_types_by_name['LuckyStrikeCosts_discounts'] = _LUCKYSTRIKECOSTS_DISCOUNTS
DESCRIPTOR.message_types_by_name['LuckyStrikeCosts_costs'] = _LUCKYSTRIKECOSTS_COSTS
DESCRIPTOR.message_types_by_name['LuckyStrikeCosts_Array'] = _LUCKYSTRIKECOSTS_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LuckyStrikeCosts = _reflection.GeneratedProtocolMessageType('LuckyStrikeCosts', (_message.Message,), {
  'DESCRIPTOR' : _LUCKYSTRIKECOSTS,
  '__module__' : 'xls_beans_luckystrikecosts_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.LuckyStrikeCosts)
  })
_sym_db.RegisterMessage(LuckyStrikeCosts)

LuckyStrikeCosts_discounts = _reflection.GeneratedProtocolMessageType('LuckyStrikeCosts_discounts', (_message.Message,), {
  'DESCRIPTOR' : _LUCKYSTRIKECOSTS_DISCOUNTS,
  '__module__' : 'xls_beans_luckystrikecosts_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.LuckyStrikeCosts_discounts)
  })
_sym_db.RegisterMessage(LuckyStrikeCosts_discounts)

LuckyStrikeCosts_costs = _reflection.GeneratedProtocolMessageType('LuckyStrikeCosts_costs', (_message.Message,), {
  'DESCRIPTOR' : _LUCKYSTRIKECOSTS_COSTS,
  '__module__' : 'xls_beans_luckystrikecosts_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.LuckyStrikeCosts_costs)
  })
_sym_db.RegisterMessage(LuckyStrikeCosts_costs)

LuckyStrikeCosts_Array = _reflection.GeneratedProtocolMessageType('LuckyStrikeCosts_Array', (_message.Message,), {
  'DESCRIPTOR' : _LUCKYSTRIKECOSTS_ARRAY,
  '__module__' : 'xls_beans_luckystrikecosts_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.LuckyStrikeCosts_Array)
  })
_sym_db.RegisterMessage(LuckyStrikeCosts_Array)


# @@protoc_insertion_point(module_scope)