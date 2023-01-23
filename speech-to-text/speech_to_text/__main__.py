import typer

from speech_to_text import logger
from speech_to_text.domain import MicrophoneStream
from speech_to_text.services import SpeechToText, TranscriptorFormatter


app = typer.Typer(name="data-generator")


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
    :param language_code: the language code of the audio stream
    :return:
    """
    logger.debug("Received parameters: rate={}, chunk={}, language_code={}".format(rate, chunk, language_code))
    stt = SpeechToText(rate=rate, language_code=language_code)

    logger.info("Opening microphone stream...")
    with MicrophoneStream(rate=rate, chunk=chunk) as stream:
        audio_generator = stream.generator()

        # Generating transcription with SpeechToText service
        transcription = stt.get_stt_result(audio_generator=audio_generator)

        # Now, put the transcription responses to use.
        TranscriptorFormatter.transcribe(responses=transcription)


if __name__ == "__main__":
    app()
