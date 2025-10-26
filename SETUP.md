# ICS344 Project Setup Guide

## Prerequisites
Make sure you have Python 3.8+ installed.

## Installation Steps

### 1. Install python3-venv (if not already installed)
```bash
sudo apt install python3.13-venv
```

### 2. Create a Virtual Environment
```bash
cd /home/srlemon/Documents/KFUPM/ICS344/Project/ics344_project
python3 -m venv venv
```

### 3. Activate the Virtual Environment
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the AES Encryption Module

### Test the AES encryption:
```bash
python aes_encryption.py
```

### Use in your code:
```python
from aes_encryption import AESEncryption

# Create encryption instance
aes = AESEncryption()

# Encrypt a message
encrypted = aes.encrypt("Your secret message")

# Decrypt the message
decrypted = aes.decrypt(encrypted)
```

## Project Structure
```
ics344_project/
├── GUI/
│   ├── gui.py          # PyQt5 GUI
│   └── main_test.py    # Main application
├── aes_encryption.py   # AES encryption module
├── requirements.txt    # Python dependencies
└── SETUP.md           # This file
```
