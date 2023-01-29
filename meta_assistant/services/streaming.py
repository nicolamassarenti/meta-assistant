import time
import numpy as np
import grpc

from typing import List

from grpc_streaming import logger
from grpc_streaming.services.grpc import audio2face_pb2, audio2face_pb2_grpc


class StreamingService:
    @staticmethod
    def stream_chunk(
        sample_rate: int, chunks: List[np.ndarray], endpoint: str, instance_name: str
    ):
        """
        Stream a chunk of bytes to the gRPC server
        :return:
        """
        block_until_playback_is_finished = True  # ADJUST

        with grpc.insecure_channel(endpoint) as channel:
            logger.info("Channel created")
            stub = audio2face_pb2_grpc.Audio2FaceStub(channel)

            def make_generator():
                start_marker = audio2face_pb2.PushAudioRequestStart(
                    samplerate=sample_rate,
                    instance_name=instance_name,
                    block_until_playback_is_finished=block_until_playback_is_finished,
                )
                # At first, we send a message with start_marker
                yield audio2face_pb2.PushAudioStreamRequest(start_marker=start_marker)
                # Then we send messages with audio_data
                for _, chunk in enumerate(chunks):
                    yield audio2face_pb2.PushAudioStreamRequest(
                        audio_data=chunk.astype(np.float32).tobytes()
                    )

            request_generator = make_generator()
            logger.debug("Sending audio data...")
            response = stub.PushAudioStream(request_generator)
            if response.success:
                logger.debug("SUCCESS")
            else:
                logger.error(f"{response.message}")
        logger.info("Channel closed")

    @staticmethod
    def stream_zero_padding(
            length: int, endpoint: str, instance_name: str,
    ):
        """
        Stream a chunk of bytes to the gRPC server
        :return:
        """
        block_until_playback_is_finished = True  # ADJUST

        with grpc.insecure_channel(endpoint) as channel:
            logger.info("Channel created")
            stub = audio2face_pb2_grpc.Audio2FaceStub(channel)

            def make_generator():
                start_marker = audio2face_pb2.PushAudioRequestStart(
                    samplerate=44100,
                    instance_name=instance_name,
                    block_until_playback_is_finished=block_until_playback_is_finished,
                )
                # At first, we send a message with start_marker
                yield audio2face_pb2.PushAudioStreamRequest(start_marker=start_marker)
                # Then we send the zero padding
                zero_padding = np.zeros(length)
                yield audio2face_pb2.PushAudioStreamRequest(
                    audio_data=zero_padding.astype(np.float32).tobytes()
                )

            request_generator = make_generator()
            logger.debug("Sending audio data...")
            response = stub.PushAudioStream(request_generator)
            if response.success:
                logger.debug("SUCCESS")
            else:
                logger.error(f"{response.message}")
        logger.info("Channel closed")
