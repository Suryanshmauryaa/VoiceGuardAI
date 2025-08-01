import io
import librosa
import numpy as np
from tensorflow.keras.models import load_model

emotion_model = load_model("models/emotion_model.h5")
EMOTIONS = ['Neutral', 'Calm', 'Happy', 'Sad', 'Angry', 'Fearful', 'Disgust', 'Surprised']

def extract_features(audio_bytes):
    y, sr = librosa.load(io.BytesIO(audio_bytes), sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=100)
    return np.mean(mfcc.T, axis=0)

def detect_emotion(audio_bytes):
    features = extract_features(audio_bytes)
    features = np.expand_dims(features, axis=0)
    prediction = emotion_model.predict(features)
    return EMOTIONS[np.argmax(prediction)]
