import torch
from torch.utils.data import Dataset

class DummyLandslideDataset(Dataset):
    def __init__(self, size=100):
        self.size = size

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        # fake terrain "image"
        x = torch.randn(1, 32, 32)

        # fake label (0 or 1 landslide)
        y = torch.randint(0, 2, (1,)).float()

        return x, y