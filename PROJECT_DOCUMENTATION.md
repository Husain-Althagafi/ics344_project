# ICS344 Project - Secure Communication System

## Overview
This project implements a secure communication system using:
- **Diffie-Hellman (DH)** for key exchange
- **AES-256-CBC** with PKCS#7 padding for encryption
- **PyQt5** GUI for demonstration

## Architecture

### 1. Diffie-Hellman Key Exchange
**File:** `diffie_hellman.py`

- Uses RFC 3526 2048-bit MODP Group (Group 14) - industry standard
- Prime (p): 2048-bit safe prime
- Generator (g): 2
- Derives a 32-byte AES key using SHA-256

**Process:**
```
Client A:
  - Generates private key: a (random)
  - Computes public key: A = g^a mod p
  
Client B:
  - Generates private key: b (random)
  - Computes public key: B = g^b mod p

Exchange:
  - Client A sends A to Client B
  - Client B sends B to Client A

Shared Secret:
  - Client A computes: s = B^a mod p
  - Client B computes: s = A^b mod p
  - Both get the same s! (because B^a = A^b = g^(ab) mod p)
  
AES Key:
  - shared_key = SHA256(s) → 32 bytes for AES-256
```

### 2. AES Encryption
**File:** `aes_encryption.py`

- **Algorithm:** AES-256
- **Mode:** CBC (Cipher Block Chaining)
- **Padding:** PKCS#7
- **IV:** Random 16-byte IV for each message
- **Output:** Base64-encoded (IV + ciphertext)

**Encryption Flow:**
```
Plaintext → UTF-8 bytes → PKCS#7 padding → AES-CBC encrypt → IV + Ciphertext → Base64
```

**Decryption Flow:**
```
Base64 → Decode → Extract IV + Ciphertext → AES-CBC decrypt → Remove padding → UTF-8 string
```

### 3. GUI Application
**Files:** 
- `GUI/main_gui.ui` - Qt Designer UI file
- `GUI/gui.py` - Auto-generated UI code
- `GUI/main_window.py` - Application logic

**Features:**
- Two-client communication simulation
- Real-time encryption/decryption
- Attack simulation
- System logs

## Security Features

### ✅ What's Secure:

1. **Key Exchange:** 
   - DH ensures keys are never transmitted
   - 2048-bit DH provides strong security
   - Resistant to passive eavesdropping

2. **Encryption:**
   - AES-256 is industry standard
   - CBC mode prevents pattern analysis
   - Random IV for each message prevents replay attacks
   - PKCS#7 padding prevents padding oracle attacks

3. **Key Derivation:**
   - SHA-256 hashing ensures uniform key distribution

### ⚠️ What's Missing (for production):

1. **Authentication:** No verification of public keys (vulnerable to MITM)
   - Solution: Use certificates or HMAC
   
2. **Perfect Forward Secrecy:** Keys are static during session
   - Solution: Re-negotiate keys periodically
   
3. **Message Authentication:** No MAC/HMAC to verify integrity
   - Solution: Use AES-GCM or add HMAC

4. **Replay Protection:** No sequence numbers
   - Solution: Add message counters/timestamps

## How to Run

### Setup:
```bash
# Install dependencies
cd ics344_project
source ../.venv/bin/activate  # or create new venv
pip install -r requirements.txt

# Run application
python GUI/main_window.py
```

### Usage:

1. **Start Application:**
   - Automatic DH key exchange occurs
   - Check logs for public keys and shared key

2. **Send Message (Client A → Client B):**
   - Type message in Client A's text box
   - Click "Encrypt & Send"
   - Encrypted message appears in Client B's box
   - Client B clicks "Decrypt & Verify" to read

3. **Reply (Client B → Client A):**
   - Type response in Client B's text box
   - Click "Encrypt & Send"
   - Client A clicks "Decrypt & Verify"

4. **Simulate Attacks:**
   - Select attack type from dropdown
   - Click "Simulate" button
   - Observe logs for attack simulation

## Project Structure

```
ics344_project/
├── diffie_hellman.py       # DH key exchange implementation
├── aes_encryption.py       # AES-CBC encryption/decryption
├── requirements.txt        # Python dependencies
├── SETUP.md               # Setup instructions
├── PROJECT_DOCUMENTATION.md # This file
└── GUI/
    ├── main_gui.ui        # Qt Designer UI file
    ├── gui.py             # Auto-generated UI code
    └── main_window.py     # Application logic
```

## Technical Details

### Diffie-Hellman Parameters:
- **Prime (p):** 2048-bit safe prime from RFC 3526
- **Generator (g):** 2
- **Private keys:** Random integers in range [2, p-2]
- **Public keys:** Computed as g^private mod p
- **Shared secret:** SHA-256 hash of computed secret

### AES Parameters:
- **Key size:** 256 bits (32 bytes)
- **Block size:** 128 bits (16 bytes)
- **Mode:** CBC with random IV per message
- **Padding:** PKCS#7 (automatic via pycryptodome)
- **Encoding:** Base64 for transmission

## Testing

### Test DH Module:
```bash
python diffie_hellman.py
```

### Test AES Module:
```bash
python aes_encryption.py
```

### Test GUI:
```bash
python GUI/main_window.py
```

## Dependencies

- Python 3.8+
- PyQt5 5.15.11
- pycryptodome 3.20.0
- pyqt5-tools (development only)

## Future Enhancements

1. Add HMAC for message authentication
2. Implement certificate-based key verification
3. Add session rekeying (Perfect Forward Secrecy)
4. Network socket implementation for real communication
5. Add digital signatures for non-repudiation
6. Implement key derivation function (KDF) for multiple keys

## References

- RFC 3526: DH MODP Groups
- NIST SP 800-38A: AES Modes of Operation
- RFC 5246: TLS Protocol (for best practices)

## Authors

ICS344 Project Team
KFUPM - Information and Computer Science Department
