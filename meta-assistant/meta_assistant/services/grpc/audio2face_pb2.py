# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio2face.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61udio2face.proto\x12\x1cmeta_assistant.services.grpc\"{\n\x10PushAudioRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x12\n\nsamplerate\x18\x02 \x01(\x05\x12\x12\n\naudio_data\x18\x03 \x01(\x0c\x12(\n block_until_playback_is_finished\x18\x04 \x01(\x08\"5\n\x11PushAudioResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x90\x01\n\x16PushAudioStreamRequest\x12K\n\x0cstart_marker\x18\x01 \x01(\x0b\x32\x33.meta_assistant.services.grpc.PushAudioRequestStartH\x00\x12\x14\n\naudio_data\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11streaming_request\"l\n\x15PushAudioRequestStart\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x12\n\nsamplerate\x18\x02 \x01(\x05\x12(\n block_until_playback_is_finished\x18\x03 \x01(\x08\";\n\x17PushAudioStreamResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\x81\x02\n\nAudio2Face\x12n\n\tPushAudio\x12..meta_assistant.services.grpc.PushAudioRequest\x1a/.meta_assistant.services.grpc.PushAudioResponse\"\x00\x12\x82\x01\n\x0fPushAudioStream\x12\x34.meta_assistant.services.grpc.PushAudioStreamRequest\x1a\x35.meta_assistant.services.grpc.PushAudioStreamResponse\"\x00(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audio2face_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PUSHAUDIOREQUEST._serialized_start=50
  _PUSHAUDIOREQUEST._serialized_end=173
  _PUSHAUDIORESPONSE._serialized_start=175
  _PUSHAUDIORESPONSE._serialized_end=228
  _PUSHAUDIOSTREAMREQUEST._serialized_start=231
  _PUSHAUDIOSTREAMREQUEST._serialized_end=375
  _PUSHAUDIOREQUESTSTART._serialized_start=377
  _PUSHAUDIOREQUESTSTART._serialized_end=485
  _PUSHAUDIOSTREAMRESPONSE._serialized_start=487
  _PUSHAUDIOSTREAMRESPONSE._serialized_end=546
  _AUDIO2FACE._serialized_start=549
  _AUDIO2FACE._serialized_end=806
# @@protoc_insertion_point(module_scope)
