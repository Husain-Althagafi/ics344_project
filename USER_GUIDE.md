# ICS344 Secure Communication System - User Guide

**Project:** Cryptography in Action – Secure Messaging Application  
**Bucket:** P01 (Python | AES-CBC PKCS#7 | Diffie-Hellman | Desktop)  
**Team:** ICS344 Project Team  
**Institution:** King Fahd University of Petroleum & Minerals

---

## Table of Contents
1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation Guide](#installation-guide)
4. [Getting Started](#getting-started)
5. [Using the Application](#using-the-application)
6. [Attack Simulations](#attack-simulations)
7. [Troubleshooting](#troubleshooting)

---

## 1. Introduction

Welcome to the Secure Communication System, a desktop application designed to demonstrate cryptographic principles including encryption, key exchange, and security attack simulations. This application provides an interactive environment for understanding how modern secure communication works.

**Key Features:**
- AES-256-CBC encryption with PKCS#7 padding
- Diffie-Hellman key exchange
- Two-client communication simulation
- Four different attack simulations
- Real-time security event logging

---

## 2. System Requirements

### Minimum Requirements
- **Operating System:** Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python Version:** Python 3.8 or higher
- **RAM:** 512 MB minimum
- **Disk Space:** 100 MB free space
- **Display:** 1024x768 resolution minimum

### Software Dependencies
- PyQt5 5.15.11
- pycryptodome 3.20.0
- Python virtual environment support

---

## 3. Installation Guide

### Step 1: Install Python
Ensure Python 3.8 or higher is installed on your system. Verify installation by opening a terminal and typing:
```bash
python3 --version
```

### Step 2: Install Virtual Environment Support
On Linux/macOS:
```bash
sudo apt install python3-venv  # Debian/Ubuntu
```

On Windows, this is typically included with Python installation.

### Step 3: Set Up Project
Navigate to the project directory and create a virtual environment:
```bash
cd ics344_project
python3 -m venv venv
```

### Step 4: Activate Virtual Environment
On Linux/macOS:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

**PLACEHOLDER FOR SCREENSHOT: Installation process showing successful dependency installation**

---

## 4. Getting Started

### Launching the Application

Once installation is complete, launch the application by running:
```bash
python GUI/main_window.py
```

The application window will appear with the following components:
- **Client A Text Area** (left panel)
- **Client B Text Area** (right panel)
- **Control Buttons** for encryption and decryption
- **Attack Simulation Controls** at the bottom
- **System Log Panel** showing security events

**PLACEHOLDER FOR SCREENSHOT: Main application window with labeled components**

### Initial Key Exchange

Upon startup, the application automatically performs a Diffie-Hellman key exchange between Client A and Client B. The system log will display:
- Client A's public key
- Client B's public key
- The derived shared AES encryption key

This process happens instantly and requires no user intervention.

**PLACEHOLDER FOR SCREENSHOT: System logs showing DH key exchange completion**

---

## 5. Using the Application

### Sending an Encrypted Message (Client A to Client B)

**Step 1:** Type your message in the Client A text area (left panel).

**PLACEHOLDER FOR SCREENSHOT: User typing message in Client A text area**

**Step 2:** Click the **"Encrypt & Send"** button under Client A's panel.

**Step 3:** The encrypted message (Base64-encoded ciphertext) will appear in Client B's text area (right panel).

**PLACEHOLDER FOR SCREENSHOT: Encrypted message appearing in Client B's text area**

**Step 4:** Observe the system log panel, which will show:
- "Client A: Encrypted and sent message"
- The encryption key used (first 32 characters)

### Decrypting a Received Message (Client B)

**Step 1:** With the encrypted message visible in Client B's text area, click the **"Decrypt & Verify"** button under Client B's panel.

**Step 2:** The original plaintext message will replace the ciphertext in Client B's text area.

**PLACEHOLDER FOR SCREENSHOT: Decrypted plaintext message in Client B's text area**

**Step 3:** The system log confirms successful decryption with the message:
- "Client B: Message decrypted successfully ✓"

### Sending Messages in Reverse (Client B to Client A)

The process works identically in the opposite direction:
1. Type message in Client B's text area
2. Click Client B's **"Encrypt & Send"**
3. Encrypted message appears in Client A's text area
4. Client A clicks **"Decrypt & Verify"** to read the message

---

## 6. Attack Simulations

The application includes four security attack simulations as specified in the project requirements. These demonstrate common threats to cryptographic systems and how they are defended against.

### Dictionary Attack

**Purpose:** Demonstrates the computational infeasibility of brute-forcing AES-256 encryption keys.

**Steps to Simulate:**
1. Select "Dictionary" from the attack type dropdown menu
2. Click the **"Simulate"** button
3. Watch the system log as it attempts common passwords
4. Observe that all attempts fail due to the massive AES-256 key space (2^256 possibilities)

**PLACEHOLDER FOR SCREENSHOT: Dictionary attack simulation in progress with failed attempts in logs**

**What You'll See:**
- Multiple password attempts logged
- Each attempt marked as "FAILED"
- Final message: "Dictionary Attack: Failed - AES-256 key space is 2^256"
- Explanation: "Would take billions of years"

### Message Injection Attack

**Purpose:** Shows that encryption provides confidentiality but not necessarily integrity or authenticity.

**Steps to Simulate:**
1. Select "Message Injection" from the dropdown menu
2. Click **"Simulate"**
3. A forged encrypted message ("HACKED MESSAGE") is injected into Client A's text area
4. The attacker successfully encrypts the message using the captured shared key

**PLACEHOLDER FOR SCREENSHOT: Message injection attack showing forged message**

**What You'll See:**
- Log message: "Simulate message attack: sending a hijacked message to client A"
- The forged encrypted message appears in the text area
- Logs show the key used for encryption
- This demonstrates why message authentication (HMAC/signatures) is necessary

### Session Hijacking (MITM Attack)

**Purpose:** Demonstrates that Diffie-Hellman is secure against passive eavesdropping but explains the need for authentication.

**Steps to Simulate:**
1. Select "Session Hijack" from the dropdown menu
2. Click **"Simulate"**
3. The simulation shows an attacker attempting to intercept the key exchange

**PLACEHOLDER FOR SCREENSHOT: Session hijacking simulation showing attacker's failed key computation**

**What You'll See:**
- "MITM Attack: Attacker intercepts communication..."
- Attacker's forged public key displayed
- Comparison between attacker's forged key and the real shared key
- "Keys don't match! ✓"
- "MITM Attack: FAILED - DH is secure against passive eavesdropping ✓"
- Note about needing digital signatures for active MITM prevention

### Flooding Messages Attack

**Purpose:** Simulates a Denial of Service (DoS) attack through rapid message transmission.

**Steps to Simulate:**
1. Select "Flooding Messages" from the dropdown menu
2. Click **"Simulate"**
3. Watch as multiple messages are rapidly encrypted and logged

**PLACEHOLDER FOR SCREENSHOT: Flooding attack showing multiple rapid messages in logs**

**What You'll See:**
- "Flooding Attack: Simulating rapid message sending..."
- Ten flood messages logged in quick succession
- "Flooding Attack: Completed"
- Defense recommendations: "Rate limiting should be implemented" and "Connection throttling recommended ✓"

---

## 7. Troubleshooting

### Application Won't Start

**Problem:** Error message when running `python GUI/main_window.py`

**Solutions:**
1. Ensure virtual environment is activated (you should see `(venv)` in your terminal prompt)
2. Verify all dependencies are installed: `pip list | grep PyQt5`
3. Check Python version: `python3 --version` (must be 3.8+)
4. Reinstall dependencies: `pip install --force-reinstall -r requirements.txt`

### Import Errors

**Problem:** "ModuleNotFoundError: No module named 'PyQt5'" or similar

**Solution:** 
```bash
source venv/bin/activate  # Activate virtual environment first
pip install PyQt5 pycryptodome
```

### Decryption Fails

**Problem:** "Padding is incorrect" error when decrypting

**Causes:**
- Message was tampered with (this is actually correct behavior!)
- Ciphertext was modified or corrupted
- Wrong key being used

**Solution:** This is expected behavior when demonstrating tampering attacks. For normal operation, ensure messages are not modified between encryption and decryption.

### GUI Display Issues

**Problem:** Text or buttons appear cut off or overlapping

**Solution:**
1. Ensure minimum screen resolution (1024x768)
2. Adjust system DPI settings if on high-resolution displays
3. Restart the application

### Log Panel Not Scrolling

**Problem:** Cannot see latest log entries

**Solution:** The log panel auto-scrolls when you're at the bottom. If you've scrolled up to read old logs, scroll to the bottom manually or let new messages arrive to trigger auto-scroll.

---

## Getting Help

For additional support or questions:
- Review the README.md file in the project directory
- Check the technical documentation for implementation details
- Consult the project source code comments
- Contact the development team

---

## Conclusion

This user guide has covered the essential operations of the Secure Communication System. You should now be able to:
- Install and launch the application
- Send and receive encrypted messages
- Simulate various security attacks
- Understand the security features and limitations

For deeper technical understanding of the cryptographic implementations, please refer to the Technical Report document.

**PLACEHOLDER FOR SCREENSHOT: Application in use showing all components working together**

---

**Document Version:** 1.0  
**Last Updated:** November 2025  
**Project Bucket:** P01
