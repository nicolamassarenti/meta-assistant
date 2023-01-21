from typing import List, Any, Generator

from google.cloud.speech_v1 import StreamingRecognizeRequest
from pydantic import BaseModel, Field


from google.cloud import speech


class SpeechToText:
    class Config:
        arbitrary_types_allowed = True

    def __init__(
        self,
        rate: int = 16000,
        language_code: str = "en-US",
    ):
        self.client = speech.SpeechClient()
        self.rate = rate
        self.language_code = language_code

        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.rate,
            language_code=self.language_code,
        )

        self.streaming_config = speech.StreamingRecognitionConfig(
            config=self.config, interim_results=True
        )

    def _generate_requests(
        self, audio_generator
    ) -> Generator[StreamingRecognizeRequest, Any, None]:
        return (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

    def _generate_transcription(
        self, requests: Generator[StreamingRecognizeRequest, Any, None]
    ) -> List[str]:
        return self.client.streaming_recognize(self.streaming_config, requests)

    def get_stt_result(self, audio_generator) -> speech.StreamingRecognizeResponse:
        # Generating requests
        requests = self._generate_requests(audio_generator=audio_generator)

        # Generating responses
        responses = self._generate_transcription(requests=requests)

        return responses
