import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile

def capture_audio(duration=5, fs=44100):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        wav.write(f.name, fs, recording)
        with open(f.name, 'rb') as audio_file:
            audio_bytes = audio_file.read()
    return audio_bytes
