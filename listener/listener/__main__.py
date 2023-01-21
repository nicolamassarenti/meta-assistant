import typer

from listener.services import SpeechToText, TranscriptorFormatter
from listener.domain import MicrophoneStream


app = typer.Typer(name="data-generator")

RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


@app.command()
def stt_from_stream(
    rate: int = typer.Option(
        default=16000,
        help="The rate of the audio stream",
        envvar="RATE",
        show_envvar=True,
    ),
    chunk: int = typer.Option(
        default=1600,
        help="The chunk of the audio stream",
        envvar="CHUNK",
        show_envvar=True,
    ),
    language_code: str = typer.Option(
        default="en-US",
        help="The language code of the audio stream",
        envvar="LANGUAGE_CODE",
        show_envvar=True,
    ),
):
    """
    Opens a microphone stream and sends the audio to the SpeechToText service, which returns a transcription.
    :param rate: the rate of the audio stream
    :param chunk: the chunk of the audio stream
    :return:
    """

    stt = SpeechToText(rate=rate, language_code=language_code)

    with MicrophoneStream(rate=rate, chunk=chunk) as stream:
        audio_generator = stream.generator()

        # Generating transciption with SpeechToText service
        transcription = stt.get_stt_result(audio_generator=audio_generator)

        # Now, put the transcription responses to use.
        TranscriptorFormatter.transcribe(responses=transcription)
