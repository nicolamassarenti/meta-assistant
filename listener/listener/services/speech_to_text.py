from typing import List
from pydantic import BaseModel, Field


from google.cloud import speech


class SpeechToText(BaseModel):
    rate: int = Field(default=16000, description="Audio recording rate")
    language_code: str = Field(default="en-US", description="Language code")
    encoding: speech.RecognitionConfig.AudioEncoding = Field(
        default=speech.RecognitionConfig.AudioEncoding.LINEAR16, description="Encoding"
    )
    client: speech.SpeechClient = Field(
        default=speech.SpeechClient(), description="Speech client"
    )
    config: speech.RecognitionConfig = Field(
        default=None, description="Recognition config"
    )
    streaming_config: speech.StreamingRecognitionConfig = Field(
        default=None, description="Streaming recognition config"
    )

    class Config:
        arbitrary_types_allowed = True

    def __init__(
        self,
        rate: int,
        language_code: str,
        encoding: speech.RecognitionConfig.AudioEncoding,
    ):
        super().__init__()
        self.rate = rate
        self.language_code = language_code
        self.encoding = encoding

        self.config = speech.RecognitionConfig(
            encoding=self.encoding,
            sample_rate_hertz=self.rate,
            language_code=self.language_code,
        )

        self.streaming_config = speech.StreamingRecognitionConfig(
            config=self.config, interim_results=True
        )

    def _generate_requests(
        self, audio_generator
    ) -> List[speech.StreamingRecognizeRequest]:
        return [
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        ]

    def _generate_transcription(
        self, requests: List[speech.StreamingRecognizeRequest]
    ) -> List[str]:
        return self.client.streaming_recognize(self.streaming_config, requests)

    def get_stt_result(self, audio_generator) -> speech.StreamingRecognizeResponse:
        # Generating requests
        requests = self._generate_requests(audio_generator=audio_generator)

        # Generating responses
        responses = self._generate_transcription(requests=requests)

        return responses
