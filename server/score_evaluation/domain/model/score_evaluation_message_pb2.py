# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: score_evaluation_message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1escore_evaluation_message.proto\x12\x08tutorial\"\xa6\x02\n\x16ScoreEvaluationMessage\x12\x16\n\x0erepository_url\x18\x01 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x02 \x01(\t\x12\x15\n\rdrop_interval\x18\x03 \x01(\x05\x12\x39\n\x05level\x18\x04 \x01(\x0e\x32*.tutorial.ScoreEvaluationMessage.GameLevel\x12\x11\n\tgame_mode\x18\x05 \x01(\t\x12\x11\n\tgame_time\x18\x06 \x01(\x05\x12\x0f\n\x07timeout\x18\x07 \x01(\x05\x12\x1b\n\x13predict_weight_path\x18\x08 \x01(\t\x12\x11\n\ttrial_num\x18\t \x01(\x05\"+\n\tGameLevel\x12\x08\n\x04\x45\x41SY\x10\x00\x12\n\n\x06MIDIUM\x10\x01\x12\x08\n\x04HARD\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'score_evaluation_message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCOREEVALUATIONMESSAGE._serialized_start=45
  _SCOREEVALUATIONMESSAGE._serialized_end=339
  _SCOREEVALUATIONMESSAGE_GAMELEVEL._serialized_start=296
  _SCOREEVALUATIONMESSAGE_GAMELEVEL._serialized_end=339
# @@protoc_insertion_point(module_scope)