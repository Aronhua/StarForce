# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xls_beans_taskevent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xls_beans_taskevent.proto',
  package='D11.Pbeans',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19xls_beans_taskevent.proto\x12\nD11.Pbeans\"\xe6\x01\n\tTaskEvent\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\ttriggerId\x18\x02 \x01(\t\x12\x10\n\x08gameMode\x18\x03 \x01(\t\x12\x0f\n\x07gameMap\x18\x04 \x01(\t\x12\x12\n\nmainCondId\x18\x05 \x01(\t\x12\x15\n\rmainCondValue\x18\x06 \x01(\t\x12\x36\n\x0btaskSubCond\x18\x07 \x03(\x0b\x32!.D11.Pbeans.TaskEvent_taskSubCond\x12\x34\n\nfinishCond\x18\x08 \x03(\x0b\x32 .D11.Pbeans.TaskEvent_finishCond\":\n\x15TaskEvent_taskSubCond\x12\x0e\n\x06\x63ondId\x18\x01 \x01(\t\x12\x11\n\tcondValue\x18\x02 \x01(\t\"%\n\x14TaskEvent_finishCond\x12\r\n\x05\x63ount\x18\x01 \x01(\r\"7\n\x0fTaskEvent_Array\x12$\n\x05items\x18\x01 \x03(\x0b\x32\x15.D11.Pbeans.TaskEventb\x06proto3')
)




_TASKEVENT = _descriptor.Descriptor(
  name='TaskEvent',
  full_name='D11.Pbeans.TaskEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='D11.Pbeans.TaskEvent.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggerId', full_name='D11.Pbeans.TaskEvent.triggerId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameMode', full_name='D11.Pbeans.TaskEvent.gameMode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameMap', full_name='D11.Pbeans.TaskEvent.gameMap', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mainCondId', full_name='D11.Pbeans.TaskEvent.mainCondId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mainCondValue', full_name='D11.Pbeans.TaskEvent.mainCondValue', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskSubCond', full_name='D11.Pbeans.TaskEvent.taskSubCond', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finishCond', full_name='D11.Pbeans.TaskEvent.finishCond', index=7,
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
  serialized_start=42,
  serialized_end=272,
)


_TASKEVENT_TASKSUBCOND = _descriptor.Descriptor(
  name='TaskEvent_taskSubCond',
  full_name='D11.Pbeans.TaskEvent_taskSubCond',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condId', full_name='D11.Pbeans.TaskEvent_taskSubCond.condId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condValue', full_name='D11.Pbeans.TaskEvent_taskSubCond.condValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=274,
  serialized_end=332,
)


_TASKEVENT_FINISHCOND = _descriptor.Descriptor(
  name='TaskEvent_finishCond',
  full_name='D11.Pbeans.TaskEvent_finishCond',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='D11.Pbeans.TaskEvent_finishCond.count', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=334,
  serialized_end=371,
)


_TASKEVENT_ARRAY = _descriptor.Descriptor(
  name='TaskEvent_Array',
  full_name='D11.Pbeans.TaskEvent_Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='D11.Pbeans.TaskEvent_Array.items', index=0,
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
  serialized_start=373,
  serialized_end=428,
)

_TASKEVENT.fields_by_name['taskSubCond'].message_type = _TASKEVENT_TASKSUBCOND
_TASKEVENT.fields_by_name['finishCond'].message_type = _TASKEVENT_FINISHCOND
_TASKEVENT_ARRAY.fields_by_name['items'].message_type = _TASKEVENT
DESCRIPTOR.message_types_by_name['TaskEvent'] = _TASKEVENT
DESCRIPTOR.message_types_by_name['TaskEvent_taskSubCond'] = _TASKEVENT_TASKSUBCOND
DESCRIPTOR.message_types_by_name['TaskEvent_finishCond'] = _TASKEVENT_FINISHCOND
DESCRIPTOR.message_types_by_name['TaskEvent_Array'] = _TASKEVENT_ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskEvent = _reflection.GeneratedProtocolMessageType('TaskEvent', (_message.Message,), {
  'DESCRIPTOR' : _TASKEVENT,
  '__module__' : 'xls_beans_taskevent_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.TaskEvent)
  })
_sym_db.RegisterMessage(TaskEvent)

TaskEvent_taskSubCond = _reflection.GeneratedProtocolMessageType('TaskEvent_taskSubCond', (_message.Message,), {
  'DESCRIPTOR' : _TASKEVENT_TASKSUBCOND,
  '__module__' : 'xls_beans_taskevent_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.TaskEvent_taskSubCond)
  })
_sym_db.RegisterMessage(TaskEvent_taskSubCond)

TaskEvent_finishCond = _reflection.GeneratedProtocolMessageType('TaskEvent_finishCond', (_message.Message,), {
  'DESCRIPTOR' : _TASKEVENT_FINISHCOND,
  '__module__' : 'xls_beans_taskevent_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.TaskEvent_finishCond)
  })
_sym_db.RegisterMessage(TaskEvent_finishCond)

TaskEvent_Array = _reflection.GeneratedProtocolMessageType('TaskEvent_Array', (_message.Message,), {
  'DESCRIPTOR' : _TASKEVENT_ARRAY,
  '__module__' : 'xls_beans_taskevent_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pbeans.TaskEvent_Array)
  })
_sym_db.RegisterMessage(TaskEvent_Array)


# @@protoc_insertion_point(module_scope)