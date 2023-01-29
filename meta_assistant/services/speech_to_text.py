from google.cloud import speech


class SpeechToText:
    @staticmethod
    def transcribe(
        audio: bytes,
        language_code: str = "en-US",
    ) -> str:
        """
        Transcribe audio stream.
        :param audio_generator: Audio generator.
        :param rate: Sample rate of the audio stream.
        :param language_code: Language code of the audio stream.
        :return: Transcribed text.
        """
        # Instantiates a client
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(content=audio)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=language_code,
        )

        response = client.recognize(config=config, audio=audio)

        for result in response.results:
            return result.alternatives[0].transcript

