import queue
import pyaudio
import time

from meta_assistant import logger


class MicrophoneStream:
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't overflow
            # while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    @staticmethod
    def get_audio(sample_rate: int, duration: int):
        """Get audio from the microphone"""
        import keyboard

        start_time = time.time()
        logger.info("Opening microphone stream...")
        with MicrophoneStream(sample_rate, chunk=1024) as stream:
            audio_generator = stream.generator()
            frames = []
            for _ in range(int(sample_rate / 1024 * duration)):
                elapsed_time = time.time() - start_time
                if elapsed_time > duration:
                    frames.append(next(audio_generator))
                    break
                if input() == "q":  # if key 'q' is pressed
                    logger.debug("You Pressed A Key!")
                    frames.append(next(audio_generator))
                    break  # finishing the loop
                frames.append(next(audio_generator))
            audio = b"".join(frames)
        logger.info("Closing microphone stream...")
        return audio

    @staticmethod
    def get_audio_recording(sample_rate: int, duration: int):
        """Get audio recording from the microphone"""
        start_time = time.time()
        with MicrophoneStream(sample_rate, chunk=1024) as stream:
            audio_generator = stream.generator()
            frames = []
            for _ in range(int(sample_rate / 1024 * duration)):
                elapsed_time = time.time() - start_time
                if elapsed_time > duration:
                    break
                # if keyboard.read_key('q'):  # if key 'q' is pressed
                #     print('You Pressed A Key!')
                #     break  # finishing the loop
                frames.append(next(audio_generator))
            audio_recording = b"".join(frames)
        return audio_recording
