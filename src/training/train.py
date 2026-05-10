import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from src.models.cnn_model import CNNBaseline
from src.training.dataset import DummyLandslideDataset

def train():
    dataset = DummyLandslideDataset()
    loader = DataLoader(dataset, batch_size=8, shuffle=True)

    model = CNNBaseline()
    criterion = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(3):  # keep small for now
        total_loss = 0

        for x, y in loader:
            optimizer.zero_grad()

            preds = model(x)
            loss = criterion(preds.squeeze(), y.squeeze())

            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

if __name__ == "__main__":
    train()