import numpy as np
import torch
from torch import nn
from typing import List

# Dummy local model
class SimpleLSTM(nn.Module):
    def __init__(self, input_size=1, hidden_size=16):
        super(SimpleLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

# Simulate training on a single client
def train_local_model(client_id):
    model = SimpleLSTM()
    # Dummy data
    data = torch.randn(32, 10, 1)
    target = torch.randn(32, 1)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    for _ in range(5):  # 5 epochs
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    print(f"Client {client_id} training complete.")
    return model.state_dict()

# Simulate federated learning round
def federated_round(num_clients=5):
    local_weights = [train_local_model(i) for i in range(num_clients)]
    print("Aggregating model updates...")

if __name__ == "__main__":
    federated_round()
