import typer
import time

from pathlib import Path


from grpc_streaming.services.file_reader import FileReader
from grpc_streaming.services.streaming import StreamingService

app = typer.Typer(name="grpc-streaming")


@app.command()
def send_audio(
    folder: Path = typer.Option(
        ...,
        help="The folder where there could be the audio files",
        file_okay=False,
        dir_okay=True,
        exists=True,
        resolve_path=True,
    ),
    endpoint: str = typer.Option(..., help="The endpoint of the gRPC server"),
):

    instance_name = "/World/audio2face/PlayerStreaming"
    file_path = None
    while True:
        # Check if a new file exists in the specified folder
        for file in folder.glob("*.wav"):
            if file_path is None or file != file_path:
                file_path = file
                break

        # If a new file exists
        if file_path:

            chunks, sample_rate = FileReader.get_chunks(path=file_path)
            StreamingService.stream_chunk(
                chunks=chunks, endpoint=endpoint, sample_rate=sample_rate, instance_name=instance_name
            )
            time.sleep(0.04)

            StreamingService.stream_zero_padding(endpoint=endpoint, length=100, instance_name=instance_name)
            time.sleep(0.01)

            # Delete file
            file_path.unlink()
            file_path = None
        else:
            StreamingService.stream_zero_padding(endpoint=endpoint, length=100, instance_name=instance_name)
            time.sleep(0.01)


if __name__ == "__main__":
    app()
