import torch.nn as nn

class DummyModel(nn.Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.fc = nn.Linear(100, 5)

    def forward(self, x):
        return self.fc(x)
