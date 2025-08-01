# app.py

import streamlit as st
from audio_processor import load_audio_file
from emotion_detector import predict_emotion
from speaker_identifier import identify_speaker
from threat_detector import detect_threat

st.set_page_config(page_title="VoiceGuard AI+", layout="centered")
st.title("🎙️ VoiceGuard AI+ – Voice & Emotion Security System")

uploaded_file = st.file_uploader("Upload an audio file (.wav)", type=["wav"])

if uploaded_file is not None:
    audio, fs = load_audio_file(uploaded_file)
    st.audio(uploaded_file, format='audio/wav')

    st.subheader("🔐 Analysis Results")

    # Run models
    speaker = identify_speaker(audio, fs)
    emotion = predict_emotion(audio, fs)
    threat = detect_threat(audio, fs)

    st.write(f"👤 **Speaker**: {speaker}")
    st.write(f"😊 **Emotion**: {emotion}")
    st.write(f"🚨 **Threat Status**: {'Threat Detected' if threat else 'No Threat'}")

# --- Local mic version (commented for Streamlit Cloud) ---
# audio, fs = capture_audio()
# Uncomment the line below to run local mic version
# st.audio(audio, format="audio/wav")
