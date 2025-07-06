# PIDS: Predictive Infrastructure Degradation System

This repository presents an early-stage prototype of the federated learning pipeline used in **PIDS**, a privacy-preserving AI system for predicting infrastructure failures across UK assets.

## 🔍 Overview

PIDS is built to operate in decentralized environments—public housing, NHS-linked estates, transport hubs—where data sensitivity and network constraints prevent central training. This repo contains:

- A simplified federated training loop
- Simulated infrastructure sensor data
- Scripts for anomaly detection model training (LSTM + GNN variants)
- Documentation outlining synthetic failure injection methods

## 🧪 Components

- `federated_training.py`: Simulates local model updates from multiple clients and secure aggregation
- `synthetic_data_generator.py`: Generates failure patterns from heating/cooling systems
- `models/`: Includes basic LSTM and GNN architectures for sequence and graph learning
- `config.yaml`: Contains adjustable parameters for federation, node count, update frequency

## 📦 Installation

```bash
git clone https://github.com/nuvaleoai/pids-federated
cd pids-federated
pip install -r requirements.txt
```

## 🚀 How to Run

```bash
python federated_training.py --clients 10 --rounds 50 --model lstm
```

## 🔐 Privacy Considerations

This prototype uses only synthetic data. The system is designed to support:
- Federated averaging with encryption-ready update stubs
- Local-only training, no raw data transfer
- Drop-in support for homomorphic encryption modules (future)

## 📄 License

MIT License

## 🔗 More Information

Visit https://www.nuvaleoai.co.uk/pids for project background or contact marius.nicorescu@nuvaleoai.co.uk for access to preprint documentation.
