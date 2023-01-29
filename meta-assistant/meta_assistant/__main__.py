import time
import typer
import queue
import threading

from meta_assistant import logger
from meta_assistant.domain import MicrophoneStream
from meta_assistant.services import (
    VoiceActivityDetection,
    SpeechToText,
    TextGenerator,
    TextToSpeech,
    Audio2Face
)

app = typer.Typer()

# Define a global FIFO queue to store the audio chunks
audio_chunks = queue.Queue()
locked = False


def microphone_audio_stream(sample_rate: int = 16000, chunk_size: int = 1024):
    """
    Open a new thread to start recording the audio and to put the audio chunks into the queue a speaker is detected.
    :return:
    """
    logger.info("Opening microphone stream...")





@app.command()
def run_meta_assistant(
    microphone_rate: int = typer.Option(
        default=16000, help="The sample rate of the microphone"
    ),
    openai_key: str = typer.Option(
        ...,
        help="The OpenAI API key",
        envvar="OPENAI_KEY",
        show_envvar=True,
    ),
    openai_model: str = typer.Option(
        default="davinci",
        help="The OpenAI model to be used",
        envvar="OPENAI_MODEL",
        show_envvar=True,
    ),
    openai_instruction: str = typer.Option(
        default="",
        help="The instruction to be used by the OpenAI model",
    ),
    grpc_server: str = typer.Option(..., help="The endpoint of the gRPC server"),
):
    """
    Run the meta-assistant
    :return:
    """
    logger.info("Received arguments:")
    logger.info("microphone_rate: {}".format(microphone_rate))
    logger.info("openai_key: {}".format(openai_key))
    logger.info("openai_model: {}".format(openai_model))
    logger.info("openai_instruction: {}".format(openai_instruction))
    logger.info("grpc_server: {}".format(grpc_server))

    # Open a new thread to start recording the audio and to put the audio chunks into the queue a speaker is detected.
    # threading.Thread(target=microphone_audio_stream, args=(microphone_rate,)).start()
    speech_audio = None
    while True:

        # # Get 10 seconds of audio
        # audio_recording = MicrophoneStream.get_audio_recording(
        #     sample_rate=microphone_rate, duration=5
        # )
        #
        # # Process the audio recording
        # text = SpeechToText.transcribe(audio=audio_recording)
        # logger.info("Transcribed text: {}".format(text))
        #
        # # Generate the response
        # response = TextGenerator.generate(
        #     key=openai_key,
        #     model=openai_model,
        #     input=text,
        #     instruction=openai_instruction,
        # )
        # logger.info("Response: {}".format(response))

        # Generate the speech audio from the response
        if speech_audio is None:
            speech_audio = TextToSpeech.synthesize(text="Hello, I'm happy to know you")

        # Send gRPC request to the audio2face plugin
        Audio2Face.send_audio(sample_rate=16000, chunks=speech_audio, endpoint=grpc_server, instance_name="/World/audio2face/PlayerStreaming")

if __name__ == "__main__":
    app()
