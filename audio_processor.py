# audio_processor.py

# For file upload (used in Streamlit Cloud)
import soundfile as sf
import numpy as np

def load_audio_file(file):
    audio, sample_rate = sf.read(file)
    return audio, sample_rate


# --- Local microphone-based capture (commented for Streamlit) ---
# import sounddevice as sd
# import numpy as np

# def capture_audio(duration=5, fs=16000):
#     print("🎤 Recording started...")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
#     sd.wait()
#     print("✅ Recording finished.")
#     return np.squeeze(audio), fs
