# VoiceGuard AI+ 🔐

**VoiceGuard AI+** is a real-time voice and emotion-based security system. It identifies the speaker, detects emotional tone, spots threat keywords in speech, and sends real-time alerts via email and SMS.

### 🔧 Features
- ✅ Real-time voice capture
- 🗣️ Speaker identification
- 😡 Emotion recognition
- 🔍 Keyword-based threat detection
- 📩 Email + SMS alerts (Twilio/Gmail)
- 🌐 REST API & Streamlit frontend

### 🚀 Run Locally
```bash
git clone https://github.com/suryanshmauryaa/VoiceGuardAI
cd VoiceGuardAI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
