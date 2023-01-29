import webrtcvad


class VoiceActivityDetection:
    """Voice activity detection service."""

    @staticmethod
    def is_speech(
        audio: bytes, sample_rate: int = 16000, aggressiveness: int = 3
    ) -> bool:
        """
        Check if the audio chunk is speech or not.
        :param audio: Audio chunk to check.
        :param sample_rate: Sample rate of the audio chunk.
        :param aggressiveness: Aggressiveness of the voice activity detection.
        :return:
        """
        # vad = webrtcvad.Vad(aggressiveness)
        # return vad.is_speech(audio_chunk, sample_rate)
        import numpy as np

        frame_duration = 1
        threshold = 6000000
        """
        Perform voice activity detection on the given audio signal.
        :param audio: The audio signal as a 1D numpy array.
        :param sample_rate: The sample rate of the audio signal.
        :param frame_duration: The duration of each frame in seconds.
        :param threshold: The energy threshold for determining speech.
        :return: A list of tuples representing the start and end times of speech segments in seconds.
        """
        audio = np.frombuffer(audio, dtype=np.int16)
        frame_size = int(frame_duration * sample_rate)
        frames = np.array([audio[i:i + frame_size] for i in range(0, len(audio), frame_size)])
        energies = np.array([np.sum(frame ** 2) for frame in frames])
        speech_detected = False
        for energy in energies:
            if energy > threshold:
                speech_detected = True
                break
        return speech_detected