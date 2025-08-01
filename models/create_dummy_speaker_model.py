import torch
import torch.nn as nn

class SpeakerModel(nn.Module):
    def __init__(self):
        super(SpeakerModel, self).__init__()
        self.fc = nn.Linear(100, 5)  # 5 speaker classes

    def forward(self, x):
        return self.fc(x)

# Instantiate and save the model
model = SpeakerModel()
torch.save(model.state_dict(), "models/speaker_recognition_model.pt")

print("✅ Dummy speaker_recognition_model.pt saved in 'models/' folder.")
