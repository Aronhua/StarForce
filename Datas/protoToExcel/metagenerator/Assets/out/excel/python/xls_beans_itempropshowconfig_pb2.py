# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_itempropshowconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_itempropshowconfig.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"xls_beans_itempropshowconfig.proto\x12\nD11.Pbeans\"\xf3\x01\n\x12ItemPropShowConfig\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x19\n\x11\x64\x65scriptionValues\x18\x04 \x03(\t\x12\x0e\n\x06iconID\x18\x05 \x01(\r\x12\x11\n\tbigIconID\x18\x06 \x01(\r\x12\x14\n\x0citemRoleName\x18\x07 \x01(\t\x12\x11\n\tthemeIcon\x18\x08 \x01(\r\x12\x0f\n\x07themeBg\x18\t \x01(\r\x12\x0f\n\x07shareBg\x18\n \x01(\r\x12\x10\n\x08\x66\x65\x61tures\x18\x0b \x03(\r\x12\x13\n\x0biconDirName\x18\x0c \x01(\t\"I\n\x18ItemPropShowConfig_Array\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.D11.Pbeans.ItemPropShowConfigb\x06proto3')
)




_ITEMPROPSHOWCONFIG = _descriptor.Descriptor(
  name='ItemPropShowConfig',
  full_name='D11.Pbeans.ItemPropShowConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.ItemPropShowConfig.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='D11.Pbeans.ItemPropShowConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='D11.Pbeans.ItemPropShowConfig.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descriptionValues', full_name='D11.Pbeans.ItemPropShowConfig.descriptionValues', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iconID', full_name='D11.Pbeans.ItemPropShowConfig.iconID', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bigIconID', full_name='D11.Pbeans.ItemPropShowConfig.bigIconID', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='itemRoleName', full_name='D11.Pbeans.ItemPropShowConfig.itemRoleName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='themeIcon', full_name='D11.Pbeans.ItemPropShowConfig.themeIcon', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='themeBg', full_name='D11.Pbeans.ItemPropShowConfig.themeBg', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shareBg', full_name='D11.Pbeans.ItemPropShowConfig.shareBg', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='D11.Pbeans.ItemPropShowConfig.features', index=10,
      number=11, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iconDirName', full_name='D11.Pbeans.ItemPropShowConfig.iconDirName', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=51,
  serialized_end=294,
)


_ITEMPROPSHOWCONFIG_ARRAY = _descriptor.Descriptor(
  name='ItemPropShowConfig_Array',
  full_name='D11.Pbeans.ItemPropShowConfig_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.ItemPropShowConfig_Array.items', index=0,
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
  serialized_start=296,
  serialized_end=369,
)

_ITEMPROPSHOWCONFIG_ARRAY.fields_by_name['items'].message_type = _ITEMPROPSHOWCONFIG
DESCRIPTOR.message_types_by_name['ItemPropShowConfig'] = _ITEMPROPSHOWCONFIG
DESCRIPTOR.message_types_by_name['ItemPropShowConfig_Array'] = _ITEMPROPSHOWCONFIG_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ItemPropShowConfig = _reflection.GeneratedProtocolMessageType('ItemPropShowConfig', (_message.Message,), {
  'DESCRIPTOR' : _ITEMPROPSHOWCONFIG,
  '__module__' : 'xls_beans_itempropshowconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ItemPropShowConfig)
  })
_sym_db.RegisterMessage(ItemPropShowConfig)

ItemPropShowConfig_Array = _reflection.GeneratedProtocolMessageType('ItemPropShowConfig_Array', (_message.Message,), {
  'DESCRIPTOR' : _ITEMPROPSHOWCONFIG_ARRAY,
  '__module__' : 'xls_beans_itempropshowconfig_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.ItemPropShowConfig_Array)
  })
_sym_db.RegisterMessage(ItemPropShowConfig_Array)


# @@protoc_insertion_point(module_scope)