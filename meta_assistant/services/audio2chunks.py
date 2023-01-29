import soundfile
import uuid
import subprocess
import os

from typing import List, Tuple


class Audio2Chunks:
    @staticmethod
    def split_audio_to_chunks(audio: bytes) -> Tuple[List[bytes], int]:
        """
        Split the audio into chunks
        :param audio: the audio to be split
        :param chunk_size: the size of each chunk
        :return: a list of chunks and the sample rate
        """
        # Generate an id for the audio files
        audio_id = uuid.uuid4().hex
        mp3_file = "{name}.mp3".format(name=audio_id)
        wav_file = "{name}.wav".format(name=audio_id)

        # Save audio content to an mp3 file
        with open(mp3_file, "wb") as out:
            out.write(audio)

        # Convert MP3 to WAV
        subprocess.call(["ffmpeg", "-i", mp3_file, wav_file])

        # Extract the audio data and the sample rate
        data, sample_rate = soundfile.read(wav_file)

        # Split the audio into chunks
        chunk_size = sample_rate // 10
        data = [
            data[i * chunk_size : i * chunk_size + chunk_size]
            for i in range(len(data) // chunk_size + 1)
        ]

        # Clean up the files
        os.remove(mp3_file)
        os.remove(wav_file)

        # Return the chunks and the sample rate
        return data, sample_rate
