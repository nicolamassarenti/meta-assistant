import numpy as np
import grpc

import soundfile

from meta_assistant import logger
from meta_assistant.services.grpc import audio2face_pb2, audio2face_pb2_grpc


class Audio2Face:
    @staticmethod
    def send_audio(
        sample_rate: int, audio_data: bytes, endpoint: str, instance_name: str
    ):
        """
        Stream a chunk of bytes to the gRPC server
        :return:
        """

        samplerate = sample_rate
        url = endpoint
        import time

        chunk_size = samplerate // 10  # ADJUST
        sleep_between_chunks = 0.04  # ADJUST
        block_until_playback_is_finished = True  # ADJUST

        with grpc.insecure_channel(url) as channel:
            print("Channel creadted")
            stub = audio2face_pb2_grpc.Audio2FaceStub(channel)

            def make_generator():
                start_marker = audio2face_pb2.PushAudioRequestStart(
                    samplerate=samplerate,
                    instance_name=instance_name,
                    block_until_playback_is_finished=block_until_playback_is_finished,
                )
                # At first, we send a message with start_marker
                yield audio2face_pb2.PushAudioStreamRequest(start_marker=start_marker)
                # Then we send messages with audio_data
                for i in range(len(audio_data) // chunk_size + 1):
                    time.sleep(sleep_between_chunks)
                    chunk = audio_data[i * chunk_size: i * chunk_size + chunk_size]
                    yield audio2face_pb2.PushAudioStreamRequest(audio_data=chunk.astype(np.float32).tobytes())

            request_generator = make_generator()
            print("Sending audio data...")
            response = stub.PushAudioStream(request_generator)
            if response.success:
                print("SUCCESS")
            else:
                print(f"ERROR: {response.message}")
        print("Channel closed")

    @staticmethod
    def send_empty(
        length: int,
        endpoint: str,
        instance_name: str,
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
