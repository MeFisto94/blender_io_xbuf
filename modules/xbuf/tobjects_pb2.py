# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xbuf/tobjects.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import xbuf.primitives_pb2

from xbuf.primitives_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='xbuf/tobjects.proto',
  package='xbuf',
  serialized_pb=_b('\n\x13xbuf/tobjects.proto\x12\x04xbuf\x1a\x15xbuf/primitives.proto\"G\n\x07TObject\x12\n\n\x02id\x18\x01 \x02(\t\x12\"\n\ttransform\x18\x02 \x02(\x0b\x32\x0f.xbuf.Transform\x12\x0c\n\x04name\x18\x04 \x01(\tP\x00')
  ,
  dependencies=[xbuf.primitives_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TOBJECT = _descriptor.Descriptor(
  name='TObject',
  full_name='xbuf.TObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xbuf.TObject.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transform', full_name='xbuf.TObject.transform', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='xbuf.TObject.name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=123,
)

_TOBJECT.fields_by_name['transform'].message_type = xbuf.primitives_pb2._TRANSFORM
DESCRIPTOR.message_types_by_name['TObject'] = _TOBJECT

TObject = _reflection.GeneratedProtocolMessageType('TObject', (_message.Message,), dict(
  DESCRIPTOR = _TOBJECT,
  __module__ = 'xbuf.tobjects_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.TObject)
  ))
_sym_db.RegisterMessage(TObject)


# @@protoc_insertion_point(module_scope)
