# models/pytorch_models.py
import torch
import torch.nn as nn
import torch.optim as optim
from .base_model.py import BaseModel

class PyTorchModel(BaseModel):
    def build_model(self):
        self.model = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 1),
            nn.Sigmoid()
        )

    def compile_model(self):
        self.criterion
