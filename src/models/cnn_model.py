import torch
import torch.nn as nn


class CNNBaseline(nn.Module):
    def __init__(self, input_channels=1):
        super(CNNBaseline, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2d(input_channels, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )

        # We compute flatten size dynamically (this fixes your error)
        self.flatten = nn.Flatten()

        # dummy pass to determine feature size
        with torch.no_grad():
            dummy = torch.zeros(1, input_channels, 32, 32)
            dummy_out = self.features(dummy)
            n_features = dummy_out.view(1, -1).shape[1]

        self.classifier = nn.Sequential(
            nn.Linear(n_features, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.flatten(x)
        x = self.classifier(x)
        return x