# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: internal_nodes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import public_input_pb2 as public__input__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14internal_nodes.proto\x1a\x12public_input.proto\"\xb4\x02\n\tEtlOutput\x12$\n\x07request\x18\x01 \x01(\x0b\x32\x13.entrypoint.Request\x12*\n\x0bmodel_input\x18\x02 \x01(\x0b\x32\x15.EtlOutput.ModelInput\x1a\xd4\x01\n\nModelInput\x12\x11\n\troom_type\x18\x01 \x01(\x05\x12\x10\n\x08\x62\x65\x64rooms\x18\x02 \x01(\x05\x12\x11\n\tbathrooms\x18\x03 \x01(\x02\x12\x14\n\x0c\x61\x63\x63ommodates\x18\x04 \x01(\x05\x12\x0c\n\x04\x62\x65\x64s\x18\x05 \x01(\x05\x12\x15\n\rneighbourhood\x18\x06 \x01(\x05\x12\x10\n\x08latitude\x18\x07 \x01(\x02\x12\x11\n\tlongitude\x18\x08 \x01(\x02\x12\n\n\x02tv\x18\t \x01(\x08\x12\x10\n\x08\x65levator\x18\n \x01(\x08\x12\x10\n\x08internet\x18\x0b \x01(\x08\"K\n\x0bModelOutput\x12$\n\x07request\x18\x01 \x01(\x0b\x32\x13.entrypoint.Request\x12\x16\n\x0eprice_category\x18\x02 \x01(\x05\x62\x06proto3')



_ETLOUTPUT = DESCRIPTOR.message_types_by_name['EtlOutput']
_ETLOUTPUT_MODELINPUT = _ETLOUTPUT.nested_types_by_name['ModelInput']
_MODELOUTPUT = DESCRIPTOR.message_types_by_name['ModelOutput']
EtlOutput = _reflection.GeneratedProtocolMessageType('EtlOutput', (_message.Message,), {

  'ModelInput' : _reflection.GeneratedProtocolMessageType('ModelInput', (_message.Message,), {
    'DESCRIPTOR' : _ETLOUTPUT_MODELINPUT,
    '__module__' : 'internal_nodes_pb2'
    # @@protoc_insertion_point(class_scope:EtlOutput.ModelInput)
    })
  ,
  'DESCRIPTOR' : _ETLOUTPUT,
  '__module__' : 'internal_nodes_pb2'
  # @@protoc_insertion_point(class_scope:EtlOutput)
  })
_sym_db.RegisterMessage(EtlOutput)
_sym_db.RegisterMessage(EtlOutput.ModelInput)

ModelOutput = _reflection.GeneratedProtocolMessageType('ModelOutput', (_message.Message,), {
  'DESCRIPTOR' : _MODELOUTPUT,
  '__module__' : 'internal_nodes_pb2'
  # @@protoc_insertion_point(class_scope:ModelOutput)
  })
_sym_db.RegisterMessage(ModelOutput)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ETLOUTPUT._serialized_start=45
  _ETLOUTPUT._serialized_end=353
  _ETLOUTPUT_MODELINPUT._serialized_start=141
  _ETLOUTPUT_MODELINPUT._serialized_end=353
  _MODELOUTPUT._serialized_start=355
  _MODELOUTPUT._serialized_end=430
# @@protoc_insertion_point(module_scope)
