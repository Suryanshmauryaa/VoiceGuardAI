import streamlit as st
from audio_processor import capture_audio
from speaker_identifier import identify_speaker
from emotion_detector import detect_emotion
from threat_detector import detect_threat
from alerts import trigger_alerts
import speech_recognition as sr
import tempfile
import wave

st.set_page_config(page_title="VoiceGuard AI+", layout="wide")

st.title("🔐 VoiceGuard AI+ – Advanced Voice & Emotion Security System")

option = st.radio("Choose Input Mode", ["🎙️ Use Microphone", "📂 Upload Audio File"])

# Capture audio
if option == "🎙️ Use Microphone":
    st.info("Recording from microphone. Please speak...")
    audio = capture_audio()
else:
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    if uploaded_file:
        audio = uploaded_file.read()
    else:
        audio = None

# Proceed if audio is available
if audio:
    st.success("✅ Audio captured successfully!")

    # Save audio temporarily for recognition
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio)
        temp_audio_path = temp_audio.name

    # Speech-to-text transcript
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(temp_audio_path) as source:
            audio_data = recognizer.record(source)
            transcript = recognizer.recognize_google(audio_data)
            st.subheader("📝 Transcript")
            st.code(transcript)
            print("🎙 TRANSCRIPT:", transcript)  # ✅ Print in terminal for debugging
    except sr.UnknownValueError:
        transcript = ""
        st.warning("🤷 Speech not recognized. Please try again.")
        print("❌ Could not understand audio.")

    # Run AI modules
    speaker = identify_speaker(audio)
    emotion = detect_emotion(audio)
    threat = detect_threat(transcript)

    st.write(f"👤 Speaker: **{speaker}**")
    st.write(f"😡 Emotion: **{emotion}**")
    st.write(f"🚨 Threat: **{threat}**")

    # Trigger alert if threat detected
    if threat != "No Threat":
        trigger_alerts(speaker, emotion, threat)
        st.error("🔴 ALERT TRIGGERED!")
