# speaker_identifier.py

import torch
from models.speaker_model import DummyModel

model = DummyModel()

# 👇 Comment this line out since you don't have a real model
# model.load_state_dict(torch.load("models/speaker_model.pt"))

model.eval()

def identify_speaker(audio_bytes):
    # Dummy audio processing
    dummy_input = torch.randn(1, 100)  # 100 input features
    output = model(dummy_input)
    predicted_speaker = torch.argmax(output).item()
    return f"Speaker {predicted_speaker + 1}"
