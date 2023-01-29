import typer

from text_to_speech.services import TextToSpeech

app = typer.Typer(name="text-to-speech")

@app.command()
def tts_from_text(
    text: str = typer.Option(
        default="Hello World!",
        help="The text to be converted to speech"
    ),
    language_code: str = typer.Option(
        default="en-US",
        help="The language code of the text",
        envvar="LANGUAGE_CODE",
        show_envvar=True,
    ),
):
    """
    Converts a text to speech
    :param text: the text to be converted to speech
    :param language_code: the language code of the text
    :return:
    """
    print("Received parameters: text={}, language_code={}".format(text, language_code))

    tts_audio = TextToSpeech.get_tts_audio(language_code=language_code, text=text)



    # Saving the audio file
    with open("/home/nicola/Music/output.mp3", "wb") as f:
        f.write(tts_audio)

    # Convert MP3 to WAV
    import subprocess
    subprocess.call(["ffmpeg", "-i", "/home/nicola/Music/output.mp3", "/home/nicola/Music/output.wav"])



if __name__ == "__main__":
    app()
