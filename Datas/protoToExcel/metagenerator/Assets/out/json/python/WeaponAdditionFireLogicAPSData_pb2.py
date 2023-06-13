# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WeaponAdditionFireLogicAPSData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WeaponAdditionFireLogicAPSData.proto',
  package='D11.Pjson',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$WeaponAdditionFireLogicAPSData.proto\x12\tD11.Pjson\"\x91\x02\n\x1eWeaponAdditionFireLogicAPSData\x12\n\n\x02Hp\x18\x01 \x01(\x02\x12\x1b\n\x13LimitDetectionCount\x18\x02 \x01(\x02\x12\x17\n\x0f\x44\x65tectionRadius\x18\x03 \x01(\x02\x12\x1a\n\x12\x44\x65tectionAllEnable\x18\x04 \x01(\x08\x12\x12\n\nPlantRange\x18\x05 \x01(\x02\x12\x1c\n\x14\x41ttackSoundEventName\x18\x06 \x01(\t\x12\x1b\n\x13PlantSoundEventName\x18\x07 \x01(\t\x12 \n\x18PlaySearchSoundEventName\x18\x08 \x01(\t\x12 \n\x18StopSearchSoundEventName\x18\t \x01(\tb\x06proto3')
)




_WEAPONADDITIONFIRELOGICAPSDATA = _descriptor.Descriptor(
  name='WeaponAdditionFireLogicAPSData',
  full_name='D11.Pjson.WeaponAdditionFireLogicAPSData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Hp', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.Hp', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LimitDetectionCount', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.LimitDetectionCount', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DetectionRadius', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.DetectionRadius', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DetectionAllEnable', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.DetectionAllEnable', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PlantRange', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.PlantRange', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AttackSoundEventName', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.AttackSoundEventName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PlantSoundEventName', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.PlantSoundEventName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PlaySearchSoundEventName', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.PlaySearchSoundEventName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StopSearchSoundEventName', full_name='D11.Pjson.WeaponAdditionFireLogicAPSData.StopSearchSoundEventName', index=8,
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
  serialized_start=52,
  serialized_end=325,
)

DESCRIPTOR.message_types_by_name['WeaponAdditionFireLogicAPSData'] = _WEAPONADDITIONFIRELOGICAPSDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WeaponAdditionFireLogicAPSData = _reflection.GeneratedProtocolMessageType('WeaponAdditionFireLogicAPSData', (_message.Message,), {
  'DESCRIPTOR' : _WEAPONADDITIONFIRELOGICAPSDATA,
  '__module__' : 'WeaponAdditionFireLogicAPSData_pb2'
  # @@protoc_insertion_point(class_scope:D11.Pjson.WeaponAdditionFireLogicAPSData)
  })
_sym_db.RegisterMessage(WeaponAdditionFireLogicAPSData)


# @@protoc_insertion_point(module_scope)