import soundfile

from typing import List, Tuple
from pathlib import Path


class FileReader:
    @staticmethod
    def get_chunks(path: Path, chunk_size: int = 1024) -> Tuple[List[bytes], int]:
        """
        Read a file and return a list of chunks with the sample rate
        :param path: the path of the file
        :param chunk_size: the size of the chunk
        :return: list of bytes
        """
        audio_data, sample_rate = soundfile.read(path)
        return (
            [
                audio_data[i * chunk_size : i * chunk_size + chunk_size]
                for i in range(len(audio_data) // chunk_size + 1)
            ],
            sample_rate,
        )
