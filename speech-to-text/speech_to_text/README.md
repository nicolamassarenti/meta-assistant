# Listener

The listener is a simple CLI that opens an audio streaming with the microphone, and sends the audio to the server for
the Speech-to-Text conversion. The output is then printed to the console.

## Technologies and Frameworks
- Typer (CLI) https://typer.tiangolo.com/
- PyAudio (Audio streaming) https://people.csail.mit.edu/hubert/pyaudio/
- Google Speech-to-Text (STT) https://cloud.google.com/speech-to-text
- Poetry (Dependency management) https://python-poetry.org/
- Docker (Containerization) https://www.docker.com/

## Usage
You can use the listener in two ways:
- Using the CLI
- Using Docker

### CLI
To use the CLI, you need to install the dependencies using poetry:
```bash
poetry install
```

Then, you can run the CLI using:
```bash
poetry run python -m speech_to_text
```
Or, as an alternative, if you activated the virtual environment, you can run:
```bash
python -m speech_to_text
```

### Docker
To use the Docker image, you need to build the image using:
```bash
./docker/build.sh
```

Then, you can run the image using:
```bash
# Create the environment variable with the path to the credentials file
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
./docker/run.sh
```
