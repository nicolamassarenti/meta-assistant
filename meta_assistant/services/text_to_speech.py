from google.cloud import texttospeech


class TextToSpeech:
    @staticmethod
    def synthesize(text: str, language_code: str = "en-US") -> bytes:
        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Save audio content to file using a temporary file
        import tempfile
        # with tempfile.NamedTemporaryFile(suffix=".mp3") as f:
        #     f.write(response.audio_content)
        #     f.seek(0)
        #     mp3_file = f.name

        # Save audio content to file
        mp3_file = "/home/nicola/Music/output.mp3"
        with open(mp3_file, "wb") as out:
            out.write(response.audio_content)

        # Convert the mp3 file to a wav file

        # Convert MP3 to WAV
        import subprocess

        wav_file="/home/nicola/Music/output.wav"
        subprocess.call(["rm", wav_file])
        subprocess.call(["ffmpeg", "-i",mp3_file, wav_file])

        return wav_file
        # Convert the mp3 file to a wav file
        import soundfile
        data, sample_rate = soundfile.read(mp3_file)
        # import tempfile
        # with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        #     soundfile.write(f, data, sample_rate)
        #     f.seek(0)
        #     wav_file = f.name

        return wav_file

