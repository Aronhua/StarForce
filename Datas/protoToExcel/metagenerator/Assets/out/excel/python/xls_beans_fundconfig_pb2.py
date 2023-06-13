# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_fundconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_fundconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1axls_beans_fundconfig.proto\x12\nD11.Pbeans\"\xa2\x02\n\nFundConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x13\n\x0bstopBuyTime\x18\x02 \x01(\x03\x12\x10\n\x08\x66undType\x18\x03 \x01(\r\x12\x0e\n\x06period\x18\x04 \x01(\r\x12\x0f\n\x07\x62uyType\x18\x05 \x01(\r\x12\x16\n\x0e\x63urrencySymbol\x18\x06 \x01(\t\x12\x14\n\x0c\x63urrencyType\x18\x07 \x01(\r\x12\x15\n\rcurrencyCount\x18\x08 \x01(\r\x12\x15\n\roriginalCount\x18\t \x01(\r\x12\x0f\n\x07panelId\x18\n \x01(\r\x12\x14\n\x0c\x62\x61\x63kgroundId\x18\x0b \x01(\r\x12\x15\n\rfundMailTitle\x18\x0c \x01(\t\x12\x17\n\x0f\x66undMailContent\x18\r \x01(\t\x12\r\n\x05tasks\x18\x0e \x03(\r\"9\n\x10\x46undConfig_Array\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x16.D11.Pbeans.FundConfigb\x06proto3')
)




_FUNDCONFIG = _descriptor.Descriptor(
  name='FundConfig',
  full_name='D11.Pbeans.FundConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.FundConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stopBuyTime', full_name='D11.Pbeans.FundConfig.stopBuyTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fundType', full_name='D11.Pbeans.FundConfig.fundType', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='D11.Pbeans.FundConfig.period', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buyType', full_name='D11.Pbeans.FundConfig.buyType', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currencySymbol', full_name='D11.Pbeans.FundConfig.currencySymbol', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currencyType', full_name='D11.Pbeans.FundConfig.currencyType', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currencyCount', full_name='D11.Pbeans.FundConfig.currencyCount', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='originalCount', full_name='D11.Pbeans.FundConfig.originalCount', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='panelId', full_name='D11.Pbeans.FundConfig.panelId', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backgroundId', full_name='D11.Pbeans.FundConfig.backgroundId', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fundMailTitle', full_name='D11.Pbeans.FundConfig.fundMailTitle', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fundMailContent', full_name='D11.Pbeans.FundConfig.fundMailContent', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='D11.Pbeans.FundConfig.tasks', index=13,
      number=14, type=13, cpp_type=3, label=3,
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
  serialized_end=333,
)


_FUNDCONFIG_ARRAY = _descriptor.Descriptor(
  name='FundConfig_Array',
  full_name='D11.Pbeans.FundConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.FundConfig_Array.items', index=0,
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
  serialized_start=335,
  serialized_end=392,
)

_FUNDCONFIG_ARRAY.fields_by_name['items'].message_type = _FUNDCONFIG
DESCRIPTOR.message_types_by_name['FundConfig'] = _FUNDCONFIG
DESCRIPTOR.message_types_by_name['FundConfig_Array'] = _FUNDCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FundConfig = _reflection.GeneratedProtocolMessageType('FundConfig', (_message.Message,), {
  'DESCRIPTOR' : _FUNDCONFIG,
  '__module__' : 'xls_beans_fundconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.FundConfig)
  })
_sym_db.RegisterMessage(FundConfig)

FundConfig_Array = _reflection.GeneratedProtocolMessageType('FundConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _FUNDCONFIG_ARRAY,
  '__module__' : 'xls_beans_fundconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.FundConfig_Array)
  })
_sym_db.RegisterMessage(FundConfig_Array)


# @@protoc_insertion_point(module_scope)