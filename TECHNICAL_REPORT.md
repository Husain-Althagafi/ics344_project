# ICS344 Secure Communication System - Technical Report

**Course:** ICS 344 – Information Security  
**Project:** Cryptography in Action – Secure Messaging Application  
**Bucket Assignment:** P01 (Python | AES-CBC PKCS#7 | Diffie-Hellman | Desktop)  
**Institution:** King Fahd University of Petroleum & Minerals  
**Department:** Information and Computer Science  
**Date:** November 2025

---

## Abstract

This report presents the design, implementation, and evaluation of a secure communication system developed as part of the ICS344 Information Security course project. The system demonstrates fundamental cryptographic principles including symmetric encryption, key exchange protocols, and security attack simulations. Built as a desktop application using Python and PyQt5, the system implements AES-256 encryption in CBC mode with PKCS#7 padding, utilizes the classic Diffie-Hellman protocol for secure key exchange, and provides interactive simulations of four common security attacks: dictionary attacks, message injection, session hijacking, and message flooding. This report details the cryptographic design decisions, implementation architecture, user interface design, attack simulation methodologies, and provides a comprehensive security evaluation including identified limitations and potential improvements.

**Keywords:** Cryptography, AES-CBC, Diffie-Hellman, Secure Communication, Attack Simulation, Desktop Security Application

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Objectives](#2-project-objectives)
3. [Cryptographic Design](#3-cryptographic-design)
4. [System Architecture](#4-system-architecture)
5. [GUI Design and Workflow](#5-gui-design-and-workflow)
6. [Attack Simulations](#6-attack-simulations)
7. [Security Evaluation](#7-security-evaluation)
8. [Limitations and Future Work](#8-limitations-and-future-work)
9. [Conclusion](#9-conclusion)
10. [References](#10-references)

---

## 1. Introduction

### 1.1 Background

In modern digital communications, ensuring the confidentiality, integrity, and authenticity of transmitted data is paramount. Cryptographic protocols form the foundation of secure communication systems, from messaging applications to financial transactions. Understanding how these protocols work, their strengths, and their vulnerabilities is essential for computer science students and security professionals.

This project implements a functional secure messaging system that demonstrates core cryptographic concepts in an accessible, interactive manner. Unlike theoretical discussions of cryptography, this application allows users to observe encryption and decryption in real-time, witness key exchange protocols in action, and understand how various security attacks can threaten or fail against properly implemented cryptographic systems.

### 1.2 Project Scope

The Secure Communication System is a desktop-based application developed according to the P01 bucket specifications, which mandates:
- Implementation language: Python
- Encryption algorithm: AES in CBC mode with PKCS#7 padding
- Key exchange protocol: Classic Diffie-Hellman
- Platform: Desktop application
- Required attack simulations: Dictionary, Message Injection, Session Hijacking, and Flooding

The application simulates a two-client communication scenario within a single window, allowing users to observe the complete workflow of secure message exchange from key establishment to encrypted transmission and decryption.

### 1.3 Motivation

Several factors motivated the development of this project:

**Educational Value:** Cryptography courses often focus on mathematical foundations without providing hands-on experience with real implementations. This project bridges that gap by offering an interactive learning tool.

**Practical Understanding:** By implementing cryptographic algorithms and protocols from scratch (using industry-standard libraries), students gain insight into the challenges and considerations that arise in real-world security applications.

**Security Awareness:** The attack simulation component demonstrates that even strong cryptographic primitives can be vulnerable to implementation flaws or protocol-level attacks, emphasizing the importance of holistic security design.

**Portfolio Development:** This project serves as a demonstration of competency in security programming, suitable for academic assessment and professional portfolios.

### 1.4 Document Organization

The remainder of this report is organized as follows: Section 2 outlines the specific objectives and requirements of the project. Section 3 provides detailed explanation of the cryptographic design, including algorithm selection, mode of operation, and key sizes. Section 4 describes the overall system architecture and component interactions. Section 5 presents the GUI design with workflow diagrams. Section 6 details each attack simulation and its defense mechanisms. Section 7 evaluates the security of the implementation, and Section 8 discusses limitations and potential improvements. Finally, Section 9 concludes the report.

---

## 2. Project Objectives

### 2.1 Primary Objectives

The primary objectives of this project were established based on the ICS344 course requirements and the P01 bucket specifications:

**Objective 1: Implement Symmetric Encryption**  
Develop a working implementation of AES-256 encryption using Cipher Block Chaining (CBC) mode with PKCS#7 padding. The implementation must correctly encrypt plaintext messages and decrypt ciphertext back to the original plaintext, demonstrating understanding of block cipher modes and padding schemes.

**Objective 2: Implement Secure Key Exchange**  
Implement the classic Diffie-Hellman key exchange protocol to enable two parties to establish a shared secret key over an insecure channel. The implementation must use cryptographically secure parameters and properly derive encryption keys from the shared secret.

**Objective 3: Create Interactive User Interface**  
Design and implement a graphical user interface that allows users to interact with the cryptographic functions intuitively, providing clear feedback through logging and visual indicators.

**Objective 4: Simulate Security Attacks**  
Implement four distinct attack simulations as specified in the P01 bucket:
- Dictionary attacks against encryption keys
- Message injection attacks
- Session hijacking via man-in-the-middle
- Message flooding for denial-of-service

**Objective 5: Demonstrate Security Principles**  
Through the combined functionality of encryption, key exchange, and attack simulations, demonstrate fundamental security principles including confidentiality, the importance of key management, and the distinction between encryption and authentication.

### 2.2 Technical Requirements

Beyond the high-level objectives, specific technical requirements guided the implementation:

- Use Python 3.8 or higher as the implementation language
- Utilize the pycryptodome library for cryptographic primitives
- Implement a desktop GUI using PyQt5 framework
- Support cross-platform operation (Windows, macOS, Linux)
- Provide comprehensive logging of all security-relevant events
- Ensure proper error handling and input validation
- Follow secure coding practices and avoid common vulnerabilities

### 2.3 Learning Outcomes

Upon completion of this project, the development team achieved the following learning outcomes:

1. Practical experience implementing cryptographic algorithms using industry-standard libraries
2. Understanding of the differences between cryptographic modes (specifically CBC mode operation)
3. Hands-on knowledge of key exchange protocols and their security properties
4. Appreciation for the complexity of building secure systems beyond just using encryption
5. Familiarity with common attack vectors and defensive strategies
6. Experience with GUI programming for security applications
7. Understanding of the limitations of individual security mechanisms and the need for defense-in-depth

---

## 3. Cryptographic Design

This section details the cryptographic components of the system, explaining the rationale behind algorithm selection, parameter choices, and implementation decisions.

### 3.1 Symmetric Encryption: AES-CBC

#### 3.1.1 Algorithm Selection

The Advanced Encryption Standard (AES) was selected as the symmetric encryption algorithm for this project. AES is a widely adopted encryption standard established by the U.S. National Institute of Standards and Technology (NIST) in 2001. Several factors justified this choice:

**Security:** AES has withstood over two decades of cryptanalysis and is considered secure against all known practical attacks when used with appropriate key sizes and modes of operation.

**Performance:** AES benefits from hardware acceleration in modern processors (AES-NI instruction set), making it efficient even for resource-constrained applications.

**Standardization:** AES is mandated or recommended by numerous security standards and regulations, including FIPS 197, making it a practical choice for real-world applications.

**Availability:** High-quality, well-tested implementations of AES are readily available in cryptographic libraries, reducing the risk of implementation flaws.

#### 3.1.2 Mode of Operation: CBC

The Cipher Block Chaining (CBC) mode was selected as specified in the P01 bucket requirements. CBC is a block cipher mode that provides several important security properties:

**Plaintext Pattern Hiding:** In CBC mode, each plaintext block is XORed with the previous ciphertext block before encryption. This ensures that identical plaintext blocks produce different ciphertext blocks, hiding patterns in the plaintext.

**Initialization Vector (IV):** CBC requires a random initialization vector for the first block. Our implementation generates a cryptographically secure random IV for each message, ensuring that encrypting the same message twice produces different ciphertexts.

**Error Propagation:** In CBC mode, a single bit error in the ciphertext affects the decryption of two blocks, which can be useful for detecting tampering (though dedicated integrity mechanisms are preferred).

The encryption process in CBC mode follows this formula for each block *i*:

```
C[0] = IV
C[i] = E(K, P[i] ⊕ C[i-1])
```

Where:
- C[i] = ciphertext block i
- E = encryption function
- K = encryption key
- P[i] = plaintext block i
- ⊕ = XOR operation
- IV = initialization vector

**PLACEHOLDER FOR DIAGRAM: CBC mode encryption illustration showing IV, plaintext blocks, XOR operations, and ciphertext blocks**

#### 3.1.3 Padding Scheme: PKCS#7

Block ciphers like AES operate on fixed-size blocks (128 bits for AES). Messages that are not multiples of the block size must be padded. This implementation uses PKCS#7 padding as specified in the bucket requirements.

PKCS#7 padding works as follows:
- If N bytes of padding are needed, append N bytes each with value N
- For example, if 5 bytes of padding are needed, append: 0x05 0x05 0x05 0x05 0x05
- If the message is already a multiple of the block size, append a full block of padding

This padding scheme is unambiguous and allows for reliable detection of padding during decryption.

#### 3.1.4 Key Size: 256 bits

This implementation uses AES-256, meaning a 256-bit (32-byte) encryption key. This key size provides a security level of 256 bits, which is more than sufficient for current and foreseeable future threat models.

To put this in perspective, attempting to brute-force a 256-bit key would require checking 2^256 possible keys. Even if an attacker could check one trillion (10^12) keys per second, it would take approximately 10^57 years to try all possibilities—many orders of magnitude longer than the age of the universe.

#### 3.1.5 Implementation Details

The AES-CBC implementation is provided by the pycryptodome library, a well-maintained fork of PyCrypto. The implementation follows this workflow:

**Encryption:**
```python
1. Generate random 16-byte IV
2. Convert plaintext string to UTF-8 bytes
3. Apply PKCS#7 padding to plaintext bytes
4. Create AES cipher object in CBC mode with key and IV
5. Encrypt padded plaintext
6. Concatenate IV + ciphertext
7. Encode result as Base64 for transmission/display
```

**Decryption:**
```python
1. Decode Base64 to get IV + ciphertext bytes
2. Extract IV (first 16 bytes)
3. Extract ciphertext (remaining bytes)
4. Create AES cipher object in CBC mode with key and IV
5. Decrypt ciphertext
6. Remove PKCS#7 padding
7. Convert bytes to UTF-8 string
```

**PLACEHOLDER FOR CODE SNIPPET: Key sections of AES encryption/decryption implementation**

### 3.2 Key Exchange: Diffie-Hellman

#### 3.2.1 Protocol Overview

The Diffie-Hellman (DH) key exchange protocol, invented by Whitfield Diffie and Martin Hellman in 1976, enables two parties to establish a shared secret over an insecure channel. The security of DH relies on the computational difficulty of the discrete logarithm problem.

The classic DH protocol operates as follows:

**Setup (Public Parameters):**
- Large prime number p (modulus)
- Generator g (primitive root modulo p)

**Key Exchange:**
1. Alice generates random private key a, computes public key A = g^a mod p
2. Bob generates random private key b, computes public key B = g^b mod p
3. Alice and Bob exchange public keys (A and B) over insecure channel
4. Alice computes shared secret: s = B^a mod p
5. Bob computes shared secret: s = A^b mod p
6. Both parties now share secret s = g^(ab) mod p

An eavesdropper observing the exchange sees only g, p, A, and B. Computing the shared secret from these values requires solving the discrete logarithm problem, which is computationally infeasible for properly chosen parameters.

**PLACEHOLDER FOR DIAGRAM: Diffie-Hellman key exchange sequence diagram showing Alice, Bob, and eavesdropper**

#### 3.2.2 Parameter Selection

This implementation uses the 2048-bit MODP Group 14 from RFC 3526, a standardized set of Diffie-Hellman parameters. The specific parameters are:

**Prime (p):** A 2048-bit safe prime (a prime of the form p = 2q + 1 where q is also prime)

**Generator (g):** 2

These parameters are considered secure for current applications and are widely used in protocols like TLS and IPsec. The 2048-bit key size provides approximately 112 bits of security, which is sufficient protection against modern attacks.

#### 3.2.3 Key Derivation

The raw shared secret computed by Diffie-Hellman is a large integer. To use this as an AES key, we must derive a fixed-length key material. This implementation uses SHA-256 hashing for key derivation:

```
shared_secret_int = g^(ab) mod p
shared_secret_bytes = int_to_bytes(shared_secret_int, 256 bytes)
aes_key = SHA256(shared_secret_bytes)  # Produces 32 bytes for AES-256
```

This approach ensures:
- Fixed output length (256 bits) suitable for AES-256
- Uniform distribution of key bits
- One-way transformation (computing shared_secret from aes_key is infeasible)

#### 3.2.4 Security Properties

The Diffie-Hellman implementation provides the following security properties:

**Passive Eavesdropping Resistance:** An attacker who observes the public key exchange cannot compute the shared secret without solving the discrete logarithm problem.

**Forward Secrecy (Session Level):** Each session uses freshly generated DH parameters. If the session keys are later compromised, past sessions remain secure (though this implementation reuses the same DH keys for the application lifetime).

**No Pre-Shared Secrets Required:** Unlike symmetric key exchange, DH allows two parties to establish a shared secret without any prior secret communication.

However, it's important to note that classic DH alone does not provide:
- Authentication (vulnerable to active man-in-the-middle attacks)
- Non-repudiation
- Message integrity

These limitations are discussed further in Section 7.

### 3.3 Random Number Generation

Cryptographic security depends critically on the quality of random numbers used for keys, IVs, and other secrets. This implementation uses Python's `secrets` module and pycryptodome's `get_random_bytes()` function, both of which utilize the operating system's cryptographically secure random number generator:

- On Linux: /dev/urandom
- On Windows: CryptGenRandom
- On macOS: /dev/urandom

These sources provide high-quality randomness suitable for cryptographic applications.

### 3.4 Base64 Encoding

Encrypted data is binary, which can cause issues when transmitted or displayed. This implementation encodes all ciphertext using Base64 encoding, which:
- Converts binary data to ASCII text
- Allows safe transmission through text-based channels
- Enables easy copying and pasting in the GUI
- Increases size by approximately 33% (acceptable overhead)

---

## 4. System Architecture

This section describes the overall architecture of the secure communication system, including component organization, data flow, and design patterns employed.

### 4.1 Component Overview

The system is organized into three primary components:

**Cryptographic Layer** (`aes_encryption.py`, `diffie_hellman.py`)  
Provides core cryptographic functionality including encryption, decryption, and key exchange. This layer is independent of the GUI and could be reused in other applications.

**User Interface Layer** (`GUI/gui.py`, `GUI/main_window.py`)  
Handles all user interactions, displays, and event processing. The GUI is generated from Qt Designer files and extended with custom logic.

**Application Logic Layer** (`GUI/main_window.py`)  
Coordinates between the cryptographic and UI layers, implements attack simulations, and manages application state.

**PLACEHOLDER FOR DIAGRAM: System architecture diagram showing three layers and their interactions**

### 4.2 Module Descriptions

#### 4.2.1 AES Encryption Module

**File:** `aes_encryption.py`

This module encapsulates all AES-CBC encryption and decryption functionality. It exposes a simple class-based interface:

```python
class AESEncryption:
    def __init__(self, key=None)
    def encrypt(self, plaintext) -> str
    def decrypt(self, encrypted_data) -> str
    def get_key_hex(self) -> str
```

**Key Design Decisions:**
- Automatic IV generation and inclusion in ciphertext
- Automatic padding handling
- String-based interface (accepts and returns strings, not bytes)
- Base64 encoding for ciphertext output

#### 4.2.2 Diffie-Hellman Module

**File:** `diffie_hellman.py`

This module implements the classic DH protocol using standardized parameters:

```python
class DiffieHellman:
    def __init__(self)
    def get_public_key(self) -> int
    def compute_shared_secret(self, other_public_key: int)
    def get_shared_key(self) -> bytes
```

**Key Design Decisions:**
- Uses RFC 3526 Group 14 parameters (2048-bit)
- SHA-256 key derivation for AES compatibility
- Separate methods for key generation and secret computation

#### 4.2.3 GUI Module

**File:** `GUI/gui.py` (auto-generated)

This file contains the PyQt5 GUI code generated from the Qt Designer `.ui` file. It should not be edited manually as it will be overwritten when the UI design is modified.

**File:** `GUI/main_window.py` (custom logic)

This file extends the auto-generated GUI with application-specific logic:
- Button click handlers
- Message encryption/decryption logic
- Attack simulation implementations
- Log management
- State tracking for replay detection

This separation allows the GUI design to be modified independently of the application logic.

### 4.3 Data Flow

#### 4.3.1 Application Startup Flow

```
1. Application starts
   ↓
2. Initialize PyQt5 application
   ↓
3. Create DH instances for Client A and Client B
   ↓
4. Perform DH key exchange
   ├→ Client A generates private/public key pair
   ├→ Client B generates private/public key pair
   ├→ Exchange public keys
   ├→ Both compute shared secret
   └→ Derive AES key via SHA-256
   ↓
5. Initialize AES encryption with shared key
   ↓
6. Display GUI window
   ↓
7. Log key exchange completion
```

**PLACEHOLDER FOR SCREENSHOT: Application startup showing DH key exchange logs**

#### 4.3.2 Message Encryption Flow

```
User types message in Client A
   ↓
User clicks "Encrypt & Send"
   ↓
main_window.py: client_a_encrypt_send()
   ↓
Call aes_encryption.encrypt(plaintext)
   ├→ Generate random IV
   ├→ Pad plaintext
   ├→ Encrypt with AES-CBC
   ├→ Concatenate IV + ciphertext
   └→ Base64 encode
   ↓
Display ciphertext in Client B text area
   ↓
Log encryption event
```

#### 4.3.3 Message Decryption Flow

```
Ciphertext present in Client B text area
   ↓
User clicks "Decrypt & Verify"
   ↓
main_window.py: client_b_decrypt_verify()
   ↓
Call aes_encryption.decrypt(ciphertext)
   ├→ Base64 decode
   ├→ Extract IV and ciphertext
   ├→ Decrypt with AES-CBC
   └→ Remove padding
   ↓
Display plaintext in Client B text area
   ↓
Log successful decryption
```

### 4.4 Design Patterns

Several software design patterns were employed to ensure maintainability and extensibility:

**Model-View-Controller (MVC):** The separation of GUI (View), cryptographic modules (Model), and main_window.py (Controller) follows MVC principles.

**Singleton Pattern:** Only one instance of the main window exists, managing application state centrally.

**Facade Pattern:** The AESEncryption and DiffieHellman classes provide simple interfaces hiding complex cryptographic operations.

**Observer Pattern:** The logging system acts as an observer, receiving notifications of security events.

---

## 5. GUI Design and Workflow

This section presents the graphical user interface design, explains the workflow for typical operations, and provides visual diagrams of the user interaction patterns.

### 5.1 Interface Layout

The application window is divided into several functional areas:

**Client A Panel (Left Side):**
- Large text area for composing/viewing messages
- "Encrypt & Send" button
- "Decrypt & Verify" button

**Client B Panel (Right Side):**
- Large text area for composing/viewing messages  
- "Encrypt & Send" button
- "Decrypt & Verify" button

**Central Divider:**
- Visual separator between the two clients

**Attack Simulation Controls (Bottom Center):**
- Dropdown menu for attack selection
- "Simulate" button to trigger the selected attack

**System Log Panel (Bottom):**
- Scrollable text area displaying security events
- Auto-scrolling to latest messages
- Shows key exchange, encryption, decryption, and attack events

**Menu Bar (Top):**
- File menu with options for printing logs

**PLACEHOLDER FOR SCREENSHOT: Main application window with all components labeled**

### 5.2 Design Rationale

The interface was designed with several principles in mind:

**Clarity:** The two-panel design makes it immediately obvious that this is a two-party communication system. Users can clearly see the message flow from one client to another.

**Simplicity:** Each client has only two buttons, reducing cognitive load. The attack simulation uses a simple dropdown + button pattern.

**Feedback:** The log panel provides continuous feedback about what the system is doing, which is essential for educational purposes.

**Visibility:** Both plaintext and ciphertext are visible simultaneously, allowing users to observe the transformation that encryption provides.

**Consistency:** Both clients have identical interfaces, emphasizing the symmetric nature of the communication.

### 5.3 Workflow Diagrams

#### 5.3.1 Standard Message Exchange Workflow

```
┌─────────────────────────────────────────────────────────────┐
│ Standard Secure Message Exchange                            │
└─────────────────────────────────────────────────────────────┘

[User] ──┐
         │
         ├─→ Types message in Client A text area
         │
         ├─→ Clicks "Encrypt & Send" button
         │
[System]──┤
         ├─→ Encrypts message with AES-CBC
         │
         ├─→ Displays ciphertext in Client B text area
         │
         ├─→ Logs encryption event
         │
[User] ──┤
         ├─→ Observes encrypted message in Client B
         │
         ├─→ Clicks "Decrypt & Verify" button
         │
[System]──┤
         ├─→ Decrypts ciphertext
         │
         ├─→ Displays plaintext in Client B text area
         │
         └─→ Logs successful decryption

```

**PLACEHOLDER FOR SCREENSHOT: Sequence showing message encryption and decryption steps**

#### 5.3.2 Attack Simulation Workflow

```
┌─────────────────────────────────────────────────────────────┐
│ Attack Simulation Workflow                                   │
└─────────────────────────────────────────────────────────────┘

[User] ──┐
         │
         ├─→ Selects attack type from dropdown
         │
         ├─→ Clicks "Simulate" button
         │
[System]──┤
         ├─→ Executes selected attack simulation
         │
         ├─→ Updates GUI with attack results
         │
         ├─→ Logs attack steps and outcomes
         │
         └─→ Displays defense effectiveness

```

**PLACEHOLDER FOR SCREENSHOT: Attack simulation interface with dropdown menu and simulate button**

### 5.4 User Interaction Flow

The typical user session follows this pattern:

**Phase 1: Startup and Observation**
1. User launches application
2. Observes automatic DH key exchange in logs
3. Notes the public keys and shared AES key displayed

**Phase 2: Message Encryption**
4. User types a plaintext message in Client A
5. Clicks "Encrypt & Send"
6. Observes the Base64-encoded ciphertext appear in Client B
7. Notes the encryption logged with key information

**Phase 3: Message Decryption**
8. User clicks "Decrypt & Verify" in Client B
9. Observes the original plaintext reappear
10. Notes successful decryption logged

**Phase 4: Reverse Communication**
11. User types a response in Client B
12. Encrypts and sends to Client A
13. Decrypts in Client A

**Phase 5: Attack Exploration**
14. User selects different attacks from dropdown
15. Observes each attack's behavior and the system's response
16. Reads detailed logs explaining attack outcomes

### 5.5 Accessibility Considerations

While not the primary focus of this educational project, several accessibility features were considered:

- Clear, readable fonts at appropriate sizes
- High contrast between text and background
- Logical tab order for keyboard navigation
- Descriptive button labels
- Comprehensive text-based logging (screen reader compatible)

### 5.6 Qt Designer Integration

The GUI was designed using Qt Designer, a visual tool for creating Qt interfaces. The workflow is:

1. Design interface visually in `main_gui.ui`
2. Generate Python code with `pyuic5` tool
3. Extend generated code in `main_window.py`

This approach provides:
- Visual design iteration without coding
- Automatic code generation
- Separation of design and logic
- Professional appearance with minimal effort

**PLACEHOLDER FOR SCREENSHOT: Qt Designer showing the interface layout**

---

## 6. Attack Simulations

This section details the four attack simulations implemented in the system, explaining the attack methodology, the system's response, and the security lessons demonstrated by each simulation.

### 6.1 Dictionary Attack

#### 6.1.1 Attack Description

A dictionary attack is a brute-force method where an attacker attempts to guess a cryptographic key by trying many possibilities from a precomputed list (dictionary) of likely values. In the context of password-based encryption, attackers might try common passwords, variations, and combinations.

However, this simulation demonstrates why dictionary attacks fail against properly generated cryptographic keys like those used in AES-256.

#### 6.1.2 Implementation

The dictionary attack simulation follows these steps:

```
1. Define a list of common passwords/keys:
   ["password", "123456", "admin", "qwerty", "secret"]

2. For each candidate in the list:
   a. Log the attempt
   b. Compare against the actual AES-256 key
   c. Mark as FAILED

3. After all attempts:
   a. Log total failures
   b. Explain why attack failed
   c. Display computational infeasibility
```

**PLACEHOLDER FOR SCREENSHOT: Dictionary attack simulation showing multiple failed attempts in logs**

#### 6.1.3 Security Analysis

The simulation demonstrates several important concepts:

**Key Space Size:** AES-256 has a key space of 2^256 possible keys. Even attempting one trillion keys per second would require approximately 10^57 years to try all possibilities.

**Random Key Generation:** Unlike user-chosen passwords, cryptographic keys should be generated using secure random number generators, making them immune to dictionary attacks.

**Quality of Secrets:** The simulation emphasizes that the strength of encryption depends not just on the algorithm but on the quality of the key material.

The logs explicitly state:
```
"Dictionary Attack: Failed - AES-256 key space is 2^256"
"Would take billions of years"
```

This educational message helps users understand that computational infeasibility is a core security property.

#### 6.1.4 Real-World Context

While this simulation shows dictionary attacks failing against AES keys, such attacks are effective against:
- User-chosen passwords (which should be hashed, not used directly as keys)
- Weak key derivation functions
- Systems with insufficient entropy in key generation

The lesson is that cryptographic systems must ensure proper key generation and management to resist dictionary attacks.

### 6.2 Message Injection Attack

#### 6.2.1 Attack Description

Message injection demonstrates that encryption alone provides confidentiality but not necessarily integrity or authenticity. In this attack, an adversary who has obtained the encryption key can create arbitrary encrypted messages that appear valid to the receiver.

This attack succeeds because AES-CBC provides no built-in authentication mechanism.

#### 6.2.2 Implementation

The message injection attack proceeds as follows:

```
1. Attacker obtains the shared encryption key (simulated)

2. Attacker creates malicious plaintext:
   "HACKED MESSAGE"

3. Attacker encrypts the malicious message with the shared key:
   encrypted = aes.encrypt("HACKED MESSAGE")

4. Attacker injects the encrypted message into Client A's text area

5. System logs the injection with key information
```

**PLACEHOLDER FOR SCREENSHOT: Message injection attack showing forged encrypted message in Client A**

#### 6.2.3 Security Analysis

This simulation illustrates critical security principles:

**Encryption ≠ Authentication:** AES-CBC encrypts data but doesn't verify who created it. An attacker with the key can impersonate any party.

**Need for Message Authentication Codes (MACs):** To prevent message injection, systems should use authenticated encryption modes (like AES-GCM) or add separate MAC/HMAC verification.

**Confidentiality vs. Integrity:** This attack succeeds even though confidentiality is maintained (the attacker encrypted a valid message). The problem is lack of integrity protection.

The logs explain:
```
"Message Injection: Demonstrates encryption alone isn't enough"
"Need for message authentication (HMAC/signatures)"
```

#### 6.2.4 Real-World Context

Message injection attacks are relevant in scenarios like:
- Compromised keys in long-lived sessions
- Insider threats (legitimate participants sending malicious content)
- Systems relying solely on encryption for security

The defense is to add authentication layers:
- HMAC (Hash-based Message Authentication Code)
- Digital signatures
- Authenticated encryption modes (AES-GCM, ChaCha20-Poly1305)

### 6.3 Session Hijacking (Man-in-the-Middle)

#### 6.3.1 Attack Description

Session hijacking through man-in-the-middle (MITM) attacks involves an adversary intercepting communications between two parties and potentially impersonating one or both. In the context of Diffie-Hellman, an active MITM attacker could perform separate DH exchanges with each party, decrypting and re-encrypting all traffic.

However, this simulation demonstrates that even a passive eavesdropper who intercepts the DH public key exchange cannot compute the shared secret.

#### 6.3.2 Implementation

The session hijacking simulation models a passive eavesdropper:

```
1. Attacker observes Client A's public key exchange

2. Attacker generates their own DH key pair

3. Attacker attempts to compute shared secret:
   attacker_secret = client_a_public_key ^ attacker_private_key mod p

4. System compares:
   - Real shared secret (from both clients)
   - Attacker's computed "secret"

5. Demonstrate that keys don't match

6. Log security analysis:
   - MITM failed due to DH security
   - Note: Active MITM (not simulated) would require additional defenses
```

**PLACEHOLDER FOR SCREENSHOT: Session hijacking simulation showing key comparison and MITM failure**

#### 6.3.3 Security Analysis

This simulation teaches several lessons about key exchange security:

**Passive Eavesdropping Resistance:** Classic DH ensures that observing the public key exchange doesn't reveal the shared secret. This relies on the computational difficulty of the discrete logarithm problem.

**Mathematical Foundation:** The attacker cannot compute g^(ab) from knowing only g^a and g^b without knowing either private exponent.

**Active MITM Vulnerability:** While passive eavesdropping fails, the simulation notes that an active attacker who intercepts and modifies the exchange could succeed. This requires authentication mechanisms like:
  - Digital certificates
  - Pre-shared authentication keys
  - Digital signatures on public keys

The logs explain:
```
"Attacker only has Client A's public key"
"Attacker cannot compute correct shared secret"
"Keys don't match! ✓"
"MITM Attack: FAILED - DH is secure against passive eavesdropping ✓"
"Note: Would need digital signatures to prevent active MITM"
```

#### 6.3.4 Real-World Context

DH security properties are fundamental to protocols like:
- TLS (Transport Layer Security) - uses authenticated DH
- IPsec - combines DH with authentication
- Signal Protocol - uses DH with identity verification

The key lesson is that DH must be combined with authentication mechanisms for complete security against MITM attacks.

### 6.4 Flooding Messages Attack

#### 6.4.1 Attack Description

A flooding attack is a type of Denial-of-Service (DoS) attack where an adversary overwhelms a system with a large volume of messages, consuming resources and potentially making the service unavailable to legitimate users.

This simulation demonstrates the impact of rapid, uncontrolled message transmission and the need for rate limiting defenses.

#### 6.4.2 Implementation

The flooding attack simulation creates rapid message traffic:

```
1. Loop 10 times (reduced from thousands to prevent actual GUI freezing):
   a. Generate flood message: "FLOOD MESSAGE {i}"
   b. Encrypt the message
   c. Log the transmission

2. After flooding sequence:
   a. Log attack completion
   b. Display defense recommendations:
      - Rate limiting
      - Connection throttling
```

**PLACEHOLDER FOR SCREENSHOT: Flooding attack showing multiple rapid messages in system logs**

#### 6.4.3 Security Analysis

The flooding simulation illustrates:

**Resource Exhaustion:** Even with efficient encryption, processing thousands or millions of messages consumes CPU, memory, and bandwidth.

**Availability Impact:** If the GUI processed all messages synchronously, the interface would freeze, demonstrating unavailability.

**Defense Mechanisms:** The simulation recommends:
  - **Rate Limiting:** Restrict the number of messages per time period
  - **Connection Throttling:** Slow down or temporarily block suspicious sources
  - **Resource Quotas:** Limit memory/CPU usage per client

The logs state:
```
"Flooding Attack: Simulating rapid message sending..."
"Flood message 1/10 sent"
...
"Flooding Attack: Completed"
"Defense: Rate limiting should be implemented"
"Defense: Connection throttling recommended ✓"
```

#### 6.4.4 Real-World Context

Flooding attacks are common in:
- Chat applications (spam)
- Email systems (email bombs)
- Network protocols (SYN floods, UDP floods)
- Web services (HTTP request floods)

Real-world defenses include:
- Application-level rate limiting
- Network-level throttling (firewalls, IDS/IPS)
- CAPTCHA for suspicious activity
- Distributed systems with load balancing
- Traffic analysis and anomaly detection

### 6.5 Attack Simulation Summary

The four attack simulations collectively demonstrate:

1. **Dictionary Attack:** Strong cryptographic keys resist brute-force
2. **Message Injection:** Encryption alone doesn't guarantee authenticity
3. **Session Hijacking:** DH resists passive eavesdropping but needs authentication
4. **Flooding:** Availability requires resource management beyond encryption

These simulations provide hands-on understanding of security principles that complement theoretical knowledge.

**PLACEHOLDER FOR TABLE: Summary table of attacks, outcomes, and lessons learned**

---

## 7. Security Evaluation

This section provides a critical evaluation of the security properties of the implemented system, analyzing both strengths and areas requiring additional mechanisms.

### 7.1 Cryptographic Strength Assessment

#### 7.1.1 AES-256-CBC Evaluation

**Strengths:**
- AES-256 is a proven encryption algorithm with no known practical attacks
- CBC mode properly conceals patterns in plaintext
- Random IV generation prevents deterministic encryption
- PKCS#7 padding is correctly implemented through pycryptodome
- Key size (256 bits) provides long-term security

**Limitations:**
- CBC mode is vulnerable to padding oracle attacks if decryption errors are revealed to attackers (mitigated by not exposing detailed error information)
- No built-in integrity protection (ciphertext can be modified)
- Vulnerable to bit-flipping attacks (modifying ciphertext affects plaintext predictably)

**Recommended Improvements:**
- Consider AES-GCM (Galois/Counter Mode) for authenticated encryption
- Add HMAC for explicit integrity verification
- Implement encrypt-then-MAC pattern

#### 7.1.2 Diffie-Hellman Evaluation

**Strengths:**
- Uses standardized 2048-bit parameters (RFC 3526 Group 14)
- Resistant to passive eavesdropping (discrete logarithm problem)
- No pre-shared secrets required
- Proper key derivation using SHA-256

**Limitations:**
- Vulnerable to active MITM attacks without authentication
- Ephemeral DH not implemented (same keys used throughout session)
- No perfect forward secrecy across sessions
- No identity verification of communication parties

**Recommended Improvements:**
- Add certificate-based authentication
- Implement ephemeral DH with periodic rekeying
- Use authenticated DH variants (like in TLS)
- Add digital signatures to verify public keys

### 7.2 Implementation Security

#### 7.2.1 Secure Coding Practices

**Positive Aspects:**
- Uses well-tested cryptographic libraries (pycryptodome) instead of custom implementations
- Proper random number generation through OS-provided sources
- No hardcoded keys or secrets
- Clear separation between cryptographic and application logic

**Areas for Improvement:**
- Key material stored in memory could be read by debuggers or memory dumps
- No secure deletion of sensitive data (Python garbage collection handles this, but not securely)
- Error messages could potentially leak information about decryption failures

#### 7.2.2 Input Validation

**Current State:**
- Basic checks for empty messages
- Exception handling for encryption/decryption failures

**Improvements Needed:**
- Validate ciphertext format before decryption attempts
- Implement maximum message length limits
- Sanitize input before logging (prevent log injection)

### 7.3 Protocol Security

#### 7.3.1 Security Properties Achieved

✅ **Confidentiality:** Messages are encrypted with AES-256, preventing unauthorized reading

✅ **Key Agreement:** DH enables secure key establishment without pre-shared secrets

✅ **Computational Security:** Both AES and DH rely on computationally hard problems

#### 7.3.2 Security Properties NOT Achieved

❌ **Authentication:** No verification of participant identities

❌ **Integrity:** No protection against message modification

❌ **Non-repudiation:** No proof of message origin

❌ **Perfect Forward Secrecy:** Key compromise reveals all session messages

❌ **Replay Protection:** No timestamps or sequence numbers (partially implemented in code but not in protocol)

### 7.4 Threat Model Analysis

#### 7.4.1 Threats Defended Against

**Passive Eavesdropping:** ✅ Protected by DH + AES encryption

**Dictionary Attacks on Keys:** ✅ Cryptographically random 256-bit keys

**Pattern Analysis:** ✅ CBC mode with random IVs prevents pattern detection

#### 7.4.2 Threats NOT Defended Against

**Active Man-in-the-Middle:** ❌ DH vulnerable without authentication

**Message Tampering:** ❌ No integrity verification

**Replay Attacks:** ❌ No protocol-level protection (code has partial implementation)

**Key Compromise:** ❌ No forward secrecy if keys leaked

**Denial of Service:** ⚠️ Limited rate limiting in simulation only

### 7.5 Comparison with Production Systems

To contextualize the security evaluation, it's useful to compare this educational implementation with production secure messaging systems:

**Signal Protocol:**
- Uses authenticated encryption (AES-GCM or ChaCha20-Poly1305)
- Implements Double Ratchet for perfect forward secrecy
- Includes message authentication codes
- Verifies identity through key fingerprints

**TLS 1.3:**
- Uses authenticated encryption exclusively
- Ephemeral DH with forward secrecy
- Certificate-based authentication
- Extensive security analysis and formal verification

**Our Implementation:**
- Educational focus on core concepts
- Demonstrates fundamental mechanisms
- Deliberately simplified to highlight specific security properties
- Suitable for learning, not production use

### 7.6 Security Grading

If we were to grade the security of this implementation:

**Cryptographic Algorithms:** A (uses strong, standard algorithms correctly)

**Key Management:** B+ (good DH implementation, but lacks authentication)

**Protocol Design:** B- (covers confidentiality well, weak on integrity/authentication)

**Implementation Quality:** B+ (uses secure libraries, good practices)

**Production Readiness:** D (educational tool, not suitable for real secrets)

**Overall Security Assessment:** B (solid educational implementation with known limitations)

---

## 8. Limitations and Future Work

This section honestly discusses the limitations of the current implementation and proposes concrete improvements for future iterations.

### 8.1 Current Limitations

#### 8.1.1 Cryptographic Limitations

**No Message Authentication:**  
The most significant limitation is the absence of message authentication codes (MACs) or digital signatures. This means:
- An attacker who obtains the key can forge messages
- Message tampering goes undetected
- No proof of message origin

**Future Work:** Implement HMAC-SHA256 for message authentication or upgrade to AES-GCM which provides built-in authentication.

**Static Key Exchange:**  
DH keys are generated once at startup and reused for the entire session:
- If keys are compromised, all messages can be decrypted
- No perfect forward secrecy between messages

**Future Work:** Implement ephemeral DH with periodic rekeying (e.g., new DH exchange every N messages or every M minutes).

**No Identity Verification:**  
The system cannot verify who it's communicating with:
- Vulnerable to active MITM attacks
- No way to ensure you're talking to the intended party

**Future Work:** Add certificate-based authentication using X.509 certificates or implement a trust-on-first-use (TOFU) model with key fingerprint verification.

#### 8.1.2 Protocol Limitations

**Single-Instance Simulation:**  
Both "clients" run in the same application:
- Not a true network protocol implementation
- Cannot demonstrate network-level attacks
- Limited realism for understanding distributed systems

**Future Work:** Implement actual network sockets (TCP/UDP) with client-server architecture to enable true multi-machine communication.

**No Session Management:**  
The application has no concept of sessions:
- Cannot handle reconnections
- No state persistence
- No session timeout or key rotation

**Future Work:** Implement session identifiers, timeouts, and renegotiation triggers.

**Limited Replay Protection:**  
While the code includes message hash tracking, it's not part of the core protocol:
- No timestamps embedded in messages
- Hash-based protection is easily bypassed
- No sequence numbers

**Future Work:** Add protocol-level sequence numbers and timestamps, implement a proper nonce-based replay protection mechanism.

#### 8.1.3 Implementation Limitations

**GUI Thread Blocking:**  
Heavy cryptographic operations run on the main GUI thread:
- Could cause UI freezing with large messages
- Flooding attack demonstration limited to prevent freezing

**Future Work:** Move cryptographic operations to background threads using PyQt's QThread or Python's threading/asyncio.

**No Secure Memory:**  
Sensitive data (keys, plaintext) stored in regular Python strings:
- Vulnerable to memory dumps
- Cannot securely erase from memory
- Swap space could contain secrets

**Future Work:** Investigate Python libraries for secure memory handling (though Python's architecture makes this challenging).

**Limited Error Handling:**  
Error messages could leak information:
- Decryption failures reveal padding errors
- Could enable padding oracle attacks in theory

**Future Work:** Implement constant-time comparison and uniform error messages.

### 8.2 Missing Security Features

**Digital Signatures:**  
No implementation of RSA, ECDSA, or other signature schemes:
- Cannot prove message origin
- No non-repudiation

**Future Work:** Add RSA signature generation and verification to complement encryption.

**Certificate Infrastructure:**  
No PKI (Public Key Infrastructure):
- Cannot verify public keys
- No trust chain

**Future Work:** Implement a simple certificate system or integrate with existing PKI.

**Key Storage:**  
Keys exist only in memory:
- Lost when application closes
- Cannot save session for later

**Future Work:** Implement secure key storage (encrypted keystore file) with master password protection.

### 8.3 Usability Limitations

**No Multi-User Support:**  
Only simulates two clients:
- Cannot demonstrate group communication
- No contact management

**Future Work:** Extend to support multiple clients with roster management.

**No Message History:**  
Messages disappear when overwritten:
- Cannot review conversation
- No persistent storage

**Future Work:** Implement message database with encryption at rest.

**Limited File Support:**  
Text messages only:
- Cannot send files
- Cannot send images

**Future Work:** Add file transfer capability with progress indicators.

### 8.4 Proposed Enhancements

#### 8.4.1 Short-Term Improvements (1-2 weeks)

1. **Add HMAC:** Implement message authentication using HMAC-SHA256
2. **Improve Logging:** Add timestamps to all log entries
3. **Input Validation:** Implement maximum message length and format validation
4. **Better Error Handling:** Uniform error messages, no information leakage

#### 8.4.2 Medium-Term Improvements (1 month)

1. **Network Implementation:** Convert to client-server architecture with sockets
2. **Key Fingerprints:** Display SHA-256 fingerprints of public keys for manual verification
3. **Session Management:** Implement session IDs and timeout mechanisms
4. **Threading:** Move crypto operations off GUI thread

#### 8.4.3 Long-Term Improvements (2-3 months)

1. **Upgrade to AES-GCM:** Replace CBC+HMAC with authenticated encryption
2. **Perfect Forward Secrecy:** Implement Double Ratchet or Signal Protocol
3. **Certificate Support:** Add X.509 certificate generation and verification
4. **Message Persistence:** Encrypted database for message history
5. **Group Messaging:** Support for multi-party conversations
6. **File Transfer:** Binary file support with chunking and progress tracking

### 8.5 Educational Value vs. Production Use

It's important to emphasize that this project was designed primarily for educational purposes. The limitations discussed are deliberate simplifications to focus on core concepts:

**Educational Strengths:**
- Clear demonstration of fundamental cryptographic principles
- Interactive visualization of abstract concepts
- Hands-on experience with security tradeoffs
- Exposes students to real cryptographic libraries

**Why Not Production-Ready:**
- Missing critical security features (authentication, integrity)
- Single-instance simulation
- No formal security analysis or penetration testing
- Not designed for adversarial environments

Students and reviewers should understand that building production secure messaging requires:
- Formal security protocol design
- Extensive testing and auditing
- Defense-in-depth approach
- Ongoing maintenance and updates
- Compliance with standards and regulations

This project succeeds as a learning tool while acknowledging that real-world security demands significantly more comprehensive implementation.

---

## 9. Conclusion

### 9.1 Summary of Achievements

This project successfully demonstrates the implementation of a secure communication system according to the P01 bucket specifications. The key achievements include:

**Cryptographic Implementation:**  
We implemented AES-256 encryption in CBC mode with PKCS#7 padding, providing strong confidentiality for messages. The use of random initialization vectors for each message ensures that identical plaintexts produce different ciphertexts, preventing pattern analysis.

**Key Exchange Protocol:**  
The classic Diffie-Hellman implementation using RFC 3526 standardized parameters enables two parties to establish a shared secret key without any prior secure communication channel. The key derivation using SHA-256 ensures compatibility with AES-256.

**User Interface:**  
The PyQt5-based desktop application provides an intuitive interface for observing cryptographic operations in real-time. The clear separation between the two clients and comprehensive logging helps users understand the message flow and security events.

**Attack Simulations:**  
Four distinct attacks were implemented and demonstrated:
- Dictionary attacks showing the computational infeasibility of brute-forcing strong keys
- Message injection illustrating the difference between confidentiality and authentication
- Session hijacking demonstrating DH's resistance to passive eavesdropping
- Message flooding highlighting the need for availability protections

**Educational Impact:**  
The project successfully bridges the gap between theoretical cryptography and practical implementation, providing hands-on experience with security concepts that are often presented only abstractly.

### 9.2 Lessons Learned

Through the development and analysis of this project, several important lessons emerged:

**Cryptography is Complex:**  
Even implementing "simple" encryption requires careful attention to details like padding, IV generation, and key derivation. Using well-tested libraries is essential to avoid implementation vulnerabilities.

**Encryption Alone is Insufficient:**  
The message injection attack clearly demonstrates that confidentiality does not imply integrity or authentication. Secure systems require multiple complementary mechanisms.

**Security is a Spectrum:**  
There is no absolute security, only security appropriate to the threat model. This educational implementation makes different tradeoffs than a production system would.

**Usability Matters:**  
Security features that are difficult to use correctly will be misused or avoided. The GUI design aimed to make cryptographic operations understandable and accessible.

**Limitations Must Be Acknowledged:**  
Understanding what a system does NOT protect against is as important as understanding what it does protect. Honest assessment of limitations enables better security decisions.

### 9.3 Meeting Project Objectives

Reviewing the objectives stated in Section 2:

✅ **Objective 1 (Symmetric Encryption):** Successfully implemented AES-256-CBC with PKCS#7 padding

✅ **Objective 2 (Key Exchange):** Successfully implemented classic Diffie-Hellman with proper parameter selection

✅ **Objective 3 (User Interface):** Created intuitive desktop GUI with clear feedback

✅ **Objective 4 (Attack Simulations):** Implemented all four required attacks (Dictionary, Message Injection, Session Hijacking, Flooding)

✅ **Objective 5 (Security Principles):** Demonstrated confidentiality, key management challenges, and the distinction between encryption and authentication

All primary objectives were met according to the P01 bucket specifications.

### 9.4 Contribution to Information Security Education

This project contributes to information security education in several ways:

**Practical Experience:** Students gain hands-on experience with cryptographic libraries and protocols, complementing theoretical coursework.

**Visual Learning:** The GUI provides immediate visual feedback on encryption transformations, making abstract concepts concrete.

**Attack Understanding:** The simulations help students develop an adversarial mindset, understanding both how attacks work and how defenses function.

**Code Review Opportunity:** The source code serves as a reference implementation that students can study, modify, and extend.

**Portfolio Piece:** The project demonstrates competency in security programming suitable for academic or professional portfolios.

### 9.5 Final Thoughts

Secure communication is fundamental to modern computing, from messaging apps to financial transactions to military communications. Understanding the building blocks—encryption algorithms, key exchange protocols, and security attacks—is essential for anyone working in information technology.

This project provides a foundation for that understanding. While the implementation is intentionally simplified for educational purposes, the core concepts demonstrated here—AES encryption, Diffie-Hellman key exchange, and security attack patterns—are the same principles underlying production systems used by billions of people daily.

The limitations and missing features discussed in Section 8 are not failures but rather opportunities for future learning. Understanding what makes a truly secure system requires first understanding the basics, then gradually adding layers of sophistication: authentication, forward secrecy, secure channels, and defense-in-depth.

We hope this project serves not as an endpoint but as a starting point for deeper exploration of cryptography and information security. The field is vast, constantly evolving, and critically important. Every student who gains practical understanding of these concepts becomes better equipped to build the secure systems our digital society depends upon.

### 9.6 Recommendations for Users

For students and instructors using this project:

**Students:**
- Experiment with the code—modify parameters, add features, break things
- Read the source code carefully to understand implementation details
- Try to exploit the limitations discussed in Section 8
- Research how production systems address these limitations
- Consider this a starting point for further study, not a complete solution

**Instructors:**
- Use this as a demonstration tool in cryptography lectures
- Assign extensions as homework (add HMAC, implement RSA signatures, etc.)
- Have students conduct security reviews and propose improvements
- Encourage students to implement the future work items
- Emphasize both what works and what's missing

**Security Professionals:**
- Recognize this as an educational tool, not production code
- Use it to explain concepts to non-technical stakeholders
- Consider it a template for more sophisticated implementations
- Appreciate the value of simple demonstrations in security education

---

## 10. References

### 10.1 Cryptographic Standards

[1] National Institute of Standards and Technology (NIST). "Advanced Encryption Standard (AES)." FIPS PUB 197, November 2001.  
https://csrc.nist.gov/publications/detail/fips/197/final

[2] National Institute of Standards and Technology (NIST). "Recommendation for Block Cipher Modes of Operation." SP 800-38A, December 2001.  
https://csrc.nist.gov/publications/detail/sp/800-38a/final

[3] Krawczyk, H., Bellare, M., and R. Canetti. "HMAC: Keyed-Hashing for Message Authentication." RFC 2104, February 1997.  
https://www.rfc-editor.org/rfc/rfc2104

[4] Kivinen, T. and M. Kojo. "More Modular Exponential (MODP) Diffie-Hellman groups for Internet Key Exchange (IKE)." RFC 3526, May 2003.  
https://www.rfc-editor.org/rfc/rfc3526

### 10.2 Cryptographic Algorithms

[5] Daemen, J. and V. Rijmen. "The Design of Rijndael: AES - The Advanced Encryption Standard." Springer-Verlag, 2002.

[6] Diffie, W. and M. Hellman. "New Directions in Cryptography." IEEE Transactions on Information Theory, vol. IT-22, no. 6, pp. 644-654, November 1976.

[7] Kaliski, B. "PKCS #7: Cryptographic Message Syntax Version 1.5." RFC 2315, March 1998.  
https://www.rfc-editor.org/rfc/rfc2315

### 10.3 Security Analysis

[8] Ferguson, N., Schneier, B., and T. Kohno. "Cryptography Engineering: Design Principles and Practical Applications." Wiley, 2010.

[9] Menezes, A., van Oorschot, P., and S. Vanstone. "Handbook of Applied Cryptography." CRC Press, 1996.  
http://cacr.uwaterloo.ca/hac/

[10] Katz, J. and Y. Lindell. "Introduction to Modern Cryptography." 2nd Edition, CRC Press, 2014.

### 10.4 Implementation Resources

[11] Python Software Foundation. "secrets — Generate secure random numbers for managing secrets." Python Documentation.  
https://docs.python.org/3/library/secrets.html

[12] Pycryptodome Contributors. "PyCryptodome Documentation." Version 3.20.0.  
https://pycryptodome.readthedocs.io/

[13] Riverbank Computing Limited. "PyQt5 Reference Guide." 2023.  
https://www.riverbankcomputing.com/static/Docs/PyQt5/

### 10.5 Attack Methodologies

[14] Vaudenay, S. "Security Flaws Induced by CBC Padding." Advances in Cryptology - EUROCRYPT 2002, pp. 534-545, 2002.

[15] Bleichenbacher, D. "Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS #1." Advances in Cryptology - CRYPTO '98, pp. 1-12, 1998.

[16] Joux, A., Vitse, V. "Elliptic Curve Discrete Logarithm Problem over Small Degree Extension Fields." Journal of Cryptology, vol. 26, no. 1, pp. 119-143, 2013.

### 10.6 Related Projects and Protocols

[17] Signal. "Signal Protocol." Technical Documentation.  
https://signal.org/docs/

[18] Rescorla, E. "The Transport Layer Security (TLS) Protocol Version 1.3." RFC 8446, August 2018.  
https://www.rfc-editor.org/rfc/rfc8446

[19] OpenSSL Project. "OpenSSL Cryptography and SSL/TLS Toolkit."  
https://www.openssl.org/

### 10.7 Educational Resources

[20] Boneh, D. and V. Shoup. "A Graduate Course in Applied Cryptography." Stanford University, 2020.  
https://toc.cryptobook.us/

[21] Stallings, W. "Cryptography and Network Security: Principles and Practice." 8th Edition, Pearson, 2020.

---

## Appendix A: Installation Instructions

Detailed installation instructions are provided in the USER_GUIDE.md document. For quick reference:

```bash
# Install virtual environment support
sudo apt install python3-venv  # Debian/Ubuntu

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run application
python GUI/main_window.py
```

---

## Appendix B: Code Structure

```
ics344_project/
├── README.md                   # Project overview and documentation
├── USER_GUIDE.md              # User manual
├── TECHNICAL_REPORT.md        # This document
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git exclusions
│
├── diffie_hellman.py          # Diffie-Hellman implementation
├── aes_encryption.py          # AES-CBC encryption/decryption
│
└── GUI/
    ├── main_gui.ui            # Qt Designer UI definition
    ├── gui.py                 # Auto-generated PyQt5 code
    └── main_window.py         # Application logic and attacks
```

---

## Appendix C: Glossary

**AES (Advanced Encryption Standard):** Symmetric encryption algorithm using 128-bit blocks

**CBC (Cipher Block Chaining):** Block cipher mode where each block is XORed with previous ciphertext

**DH (Diffie-Hellman):** Key exchange protocol based on discrete logarithm problem

**HMAC:** Hash-based Message Authentication Code for verifying integrity and authenticity

**IV (Initialization Vector):** Random value used to initialize CBC mode encryption

**MAC (Message Authentication Code):** Cryptographic checksum to verify message integrity

**MITM (Man-in-the-Middle):** Attack where adversary intercepts communication

**PKCS#7:** Padding scheme for block ciphers

**SHA-256:** Cryptographic hash function producing 256-bit output

---

**End of Technical Report**

**Document Information:**
- Version: 1.0
- Date: November 2025
- Pages: ~15 pages (formatted)
- Project: ICS344 Secure Communication System
- Bucket: P01
