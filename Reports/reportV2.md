# ICS344 Secure Communication System - Technical Report

**Course:** ICS 344 – Information Security  
**Project:** Cryptography in Action – Secure Messaging Application  
**Bucket:** P01 (Python | AES-CBC PKCS#7 | Diffie-Hellman | Desktop)  
**Institution:** King Fahd University of Petroleum & Minerals  
**Date:** November 2025

---

## Abstract

This report presents a secure communication system developed for the ICS344 course, demonstrating fundamental cryptographic principles through an interactive desktop application. Built with Python and PyQt5, the system implements AES-256-CBC encryption with PKCS#7 padding and classic Diffie-Hellman key exchange, while providing simulations of four security attacks: dictionary attacks, message injection, session hijacking, and message flooding. The report details cryptographic design, system architecture, GUI workflow, attack methodologies, and security evaluation with identified limitations.

**Keywords:** Cryptography, AES-CBC, Diffie-Hellman, Attack Simulation, Desktop Security Application

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

### 1.1 Background and Scope

In modern digital communications, cryptographic protocols form the foundation of secure systems. This project implements a functional secure messaging system demonstrating core cryptographic concepts in an interactive manner, allowing users to observe encryption/decryption in real-time and understand how security attacks operate.

The Secure Communication System is a desktop application developed per P01 specifications: Python implementation, AES-CBC with PKCS#7 padding, classic Diffie-Hellman key exchange, and simulations of Dictionary, Message Injection, Session Hijacking, and Flooding attacks. The application simulates two-client communication within a single window, showing the complete workflow from key establishment to encrypted message exchange.

### 1.2 Motivation

This project bridges the gap between theoretical cryptography and practical implementation, providing hands-on experience with real security challenges. It demonstrates that strong cryptographic primitives can still be vulnerable to implementation flaws or protocol-level attacks, emphasizing holistic security design. The project serves as both an educational tool and a portfolio demonstration of security programming competency.

---

## 2. Project Objectives

### 2.1 Primary Objectives

**Objective 1: Implement Symmetric Encryption**  
Develop AES-256 encryption using CBC mode with PKCS#7 padding, demonstrating understanding of block cipher modes and padding schemes.

**Objective 2: Implement Secure Key Exchange**  
Implement classic Diffie-Hellman protocol using cryptographically secure parameters, properly deriving encryption keys from the shared secret.

**Objective 3: Create Interactive User Interface**  
Design a graphical interface allowing intuitive interaction with cryptographic functions through clear logging and visual feedback.

**Objective 4: Simulate Security Attacks**  
Implement four distinct attacks: dictionary attacks on keys, message injection, session hijacking via MITM, and message flooding DoS.

**Objective 5: Demonstrate Security Principles**  
Show fundamental concepts including confidentiality, key management importance, and the distinction between encryption and authentication.

### 2.2 Technical Requirements

- Python 3.8+ with pycryptodome library for cryptographic primitives
- PyQt5 framework for desktop GUI
- Cross-platform support (Windows, macOS, Linux)
- Comprehensive security event logging
- Proper error handling and secure coding practices

---

## 3. Cryptographic Design

### 3.1 Symmetric Encryption: AES-CBC

**Algorithm Selection:** AES-256 was chosen for its proven security (20+ years of cryptanalysis), hardware acceleration support (AES-NI), standardization (FIPS 197), and availability of well-tested implementations.

**CBC Mode:** Cipher Block Chaining provides plaintext pattern hiding through XOR operations with previous ciphertext blocks. Each message uses a cryptographically random initialization vector (IV), ensuring identical plaintexts produce different ciphertexts. The encryption follows:

```
C[i] = E(K, P[i] ⊕ C[i-1])
```

Where:
- C = ciphertext
- P = plaintext
- K = key
- E = encryption function

**PLACEHOLDER FOR DIAGRAM: CBC mode encryption illustration**

**PKCS#7 Padding:** Block ciphers require fixed-size inputs (128 bits for AES). PKCS#7 padding appends N bytes of value N when N bytes are needed, providing unambiguous padding removal during decryption.

**Implementation:** Uses pycryptodome library following this workflow:

*Encryption:*
1. Generate random 16-byte IV
2. UTF-8 encode plaintext
3. Apply PKCS#7 padding
4. Encrypt with AES-CBC
5. Concatenate IV+ciphertext
6. Base64 encode

*Decryption:*
1. Base64 decode
2. Extract IV and ciphertext
3. Decrypt
4. Remove padding
5. UTF-8 decode

**PLACEHOLDER FOR CODE SNIPPET: AES encryption/decryption implementation**

### 3.2 Key Exchange: Diffie-Hellman

**Protocol Overview:** The Diffie-Hellman protocol enables shared secret establishment over insecure channels. Alice and Bob each generate private keys (a, b), compute public keys (A=g^a mod p, B=g^b mod p), exchange public values, then independently compute the same shared secret s=g^(ab) mod p. Security relies on the discrete logarithm problem's computational difficulty.

**PLACEHOLDER FOR DIAGRAM: Diffie-Hellman exchange sequence**

**Parameters:** Uses RFC 3526 Group 14 (2048-bit MODP) with prime p and generator g=2. This provides ~112 bits of security, sufficient for current threats.

**Key Derivation:** Raw DH output is hashed with SHA-256 to produce a 32-byte AES key:

```python
shared_secret_bytes = int_to_bytes(g^(ab) mod p, 256 bytes)
aes_key = SHA256(shared_secret_bytes)  # Produces 32 bytes for AES-256
```

This ensures:
- Fixed output length (256 bits) suitable for AES-256
- Uniform distribution of key bits
- One-way transformation (computing shared_secret from aes_key is infeasible)

**Security Properties:** DH resists passive eavesdropping (discrete logarithm hardness) and requires no pre-shared secrets. However, it lacks authentication (vulnerable to active MITM), non-repudiation, and message integrity.

### 3.3 Additional Security Mechanisms

**Random Number Generation:** Uses Python's `secrets` module and pycryptodome's `get_random_bytes()`, both utilizing OS cryptographic RNGs (/dev/urandom on Linux/macOS, CryptGenRandom on Windows).

**Base64 Encoding:** All ciphertext is Base64-encoded for safe text-based transmission and GUI display, with ~33% size overhead.

---

## 4. System Architecture

### 4.1 Component Organization

The system uses three-layer architecture:

**Cryptographic Layer** (`aes_encryption.py`, `diffie_hellman.py`): Core encryption/decryption and key exchange, independent of GUI and reusable.

**User Interface Layer** (`GUI/gui.py`, `GUI/main_window.py`): User interactions, displays, and event processing via Qt Designer-generated interfaces.

**Application Logic Layer** (`GUI/main_window.py`): Coordinates cryptographic and UI layers, implements attack simulations, manages application state.

**PLACEHOLDER FOR DIAGRAM: System architecture layers**

### 4.2 Module Descriptions

**AESEncryption Module:** Encapsulates AES-CBC with automatic IV generation, padding handling, string-based interface, and Base64 encoding.

**DiffieHellman Module:** Implements classic DH with RFC 3526 parameters, SHA-256 key derivation, and separate methods for key generation and secret computation.

**GUI Module:** Auto-generated `gui.py` from Qt Designer defines window layout; `main_window.py` extends it with button handlers, encryption/decryption logic, attack simulations, and logging.

### 4.3 Data Flow

**Startup Flow:**
```
Initialize PyQt5 → Create DH instances → Perform key exchange → 
Derive AES key → Display GUI → Log completion
```

**Message Encryption:**
```
User types message → Clicks "Encrypt & Send" → 
AES-CBC encryption (random IV, padding, encrypt, Base64) → 
Display ciphertext → Log event
```

**Message Decryption:**
```
Ciphertext present → User clicks "Decrypt & Verify" → 
Decode Base64 → Extract IV → Decrypt → Remove padding → 
Display plaintext → Log success
```

**PLACEHOLDER FOR SCREENSHOT: Application startup with DH logs**

---

## 5. GUI Design and Workflow

### 5.1 Interface Layout

**Client Panels:** Two symmetric panels (A and B) with text areas and "Encrypt & Send" / "Decrypt & Verify" buttons.

**Attack Controls:** Dropdown menu for attack selection with "Simulate" button.

**System Log:** Auto-scrolling panel showing key exchange, encryption/decryption, and attack events.

**PLACEHOLDER FOR SCREENSHOT: Main window with labeled components**

### 5.2 Design Rationale

The two-panel design clarifies the two-party system with visible message flow. Minimal buttons reduce cognitive load. The log panel provides continuous educational feedback. Both plaintext and ciphertext visibility demonstrates encryption's transformation. Identical client interfaces emphasize symmetric communication.

### 5.3 User Workflow

**Standard Message Exchange:**
```
1. User types message in Client A
2. Click "Encrypt & Send"
3. Observe ciphertext in Client B
4. Click "Decrypt & Verify"
5. Observe plaintext restoration
```

**Attack Simulation:**
```
1. Select attack type from dropdown menu
2. Click "Simulate" button
3. Observe attack execution in real-time
4. Read defense analysis in system logs
```

**PLACEHOLDER FOR SCREENSHOT: Message encryption sequence**

### 5.4 Qt Designer Integration

GUI designed visually in `main_gui.ui` → Generated to Python with `pyuic5` → Extended in `main_window.py`. This separates design from logic, enables visual iteration, and ensures professional appearance.

---

## 6. Attack Simulations

### 6.1 Dictionary Attack

**Description:** Brute-force key guessing using common password lists. This simulation demonstrates why dictionary attacks fail against cryptographically random 256-bit keys.

**Implementation:** Attempts common passwords ["password", "123456", "admin", "qwerty", "secret"] against the AES key, logging each failure and explaining computational infeasibility (2^256 keyspace requires ~10^57 years at 1 trillion keys/second).

**PLACEHOLDER FOR SCREENSHOT: Dictionary attack failed attempts**

**Lesson:** Strong cryptographic keys resist brute-force. Key quality (random generation) matters as much as algorithm strength.

### 6.2 Message Injection Attack

**Description:** Demonstrates that encryption provides confidentiality but not authenticity. An attacker with the key can forge valid encrypted messages.

**Implementation:** Attacker obtains shared key → Creates malicious plaintext "HACKED MESSAGE" → Encrypts with shared key → Injects into Client A → System logs the successful injection.

**PLACEHOLDER FOR SCREENSHOT: Injected forged message**

**Security Analysis:** AES-CBC doesn't verify message origin. Encryption ≠ Authentication. Defense requires MAC/HMAC or authenticated encryption modes (AES-GCM).

### 6.3 Session Hijacking (MITM)

**Description:** Man-in-the-middle attack simulation showing passive eavesdropper's failure to compute DH shared secret.

**Implementation:** Attacker observes public key exchange → Generates own DH key pair → Attempts to compute shared secret → System compares real vs. attacker's "secret" → Keys don't match → Attack fails.

**PLACEHOLDER FOR SCREENSHOT: MITM failure with key comparison**

**Security Analysis:** DH resists passive eavesdropping (discrete logarithm problem). However, active MITM (intercepting and modifying exchange) requires authentication via certificates or digital signatures.

### 6.4 Flooding Attack

**Description:** Denial-of-Service via message volume overwhelming system resources.

**Implementation:** Rapid loop generating 10 encrypted messages → Logs each transmission → Displays defense recommendations (rate limiting, connection throttling).

**PLACEHOLDER FOR SCREENSHOT: Flooding logs**

**Security Analysis:** Even efficient encryption can't prevent resource exhaustion. Availability requires rate limiting, network throttling, CAPTCHA, and traffic analysis beyond cryptographic mechanisms.

### 6.5 Summary

The four attacks demonstrate:

1. **Dictionary Attack:** Strong cryptographic keys resist brute-force
2. **Message Injection:** Encryption alone doesn't guarantee authenticity
3. **Session Hijacking:** DH resists passive eavesdropping but needs authentication
4. **Flooding:** Availability requires resource management beyond encryption

**PLACEHOLDER FOR TABLE: Attack summary and lessons**

---

## 7. Security Evaluation

### 7.1 Cryptographic Strength

**AES-256-CBC Strengths:** Proven algorithm, CBC pattern concealment, random IV, correct PKCS#7 padding, 256-bit long-term security.

**AES-256-CBC Limitations:** Vulnerable to padding oracle attacks if errors exposed, no integrity protection, susceptible to bit-flipping attacks.

**DH Strengths:** 2048-bit standardized parameters, passive eavesdropping resistance, no pre-shared secrets, proper SHA-256 derivation.

**DH Limitations:** Vulnerable to active MITM without authentication, static keys (no ephemeral DH), no perfect forward secrecy, no identity verification.

### 7.2 Implementation Security

**Positive Aspects:** Uses well-tested libraries (pycryptodome), OS cryptographic RNGs, no hardcoded secrets, clear separation of concerns.

**Areas for Improvement:** Key material in memory vulnerable to dumps, no secure deletion, error messages could leak padding information, limited input validation.

### 7.3 Protocol Security

**Achieved:** ✅ Confidentiality (AES-256), ✅ Key Agreement (DH), ✅ Computational Security

**NOT Achieved:** ❌ Authentication, ❌ Integrity, ❌ Non-repudiation, ❌ Perfect Forward Secrecy, ❌ Replay Protection

### 7.4 Threat Model

**Defended:** Passive eavesdropping, dictionary attacks on keys, pattern analysis

**NOT Defended:** Active MITM, message tampering, replay attacks, key compromise, DoS (limited)

### 7.5 Comparison with Production Systems

**Signal Protocol:** AES-GCM, Double Ratchet forward secrecy, MAC, key fingerprints

**TLS 1.3:** Authenticated encryption, ephemeral DH, certificates, formal verification

**Our Implementation:** Educational focus, fundamental mechanisms, deliberate simplifications, suitable for learning only

### 7.6 Security Assessment

| Category | Grade | Justification |
|----------|-------|---------------|
| Cryptographic Algorithms | **A** | Uses strong, standard algorithms correctly |
| Key Management | **B+** | Good DH implementation, lacks authentication |
| Protocol Design | **B-** | Good confidentiality, weak integrity/authentication |
| Implementation Quality | **B+** | Secure libraries, good practices |
| Production Readiness | **D** | Educational tool, not suitable for real secrets |
| **Overall Assessment** | **B** | Solid educational implementation with known limitations |

---

## 8. Limitations and Future Work

### 8.1 Critical Limitations

**No Message Authentication:** MACs/signatures absent; attackers with keys can forge messages, tampering undetected. *Future:* HMAC-SHA256 or AES-GCM.

**Static Keys:** DH keys reused throughout session; compromise decrypts all messages. *Future:* Ephemeral DH with periodic rekeying.

**No Identity Verification:** Cannot verify communication party; vulnerable to active MITM. *Future:* X.509 certificates or TOFU with key fingerprints.

**Single-Instance Simulation:** Both clients in same application; not true network protocol. *Future:* TCP/UDP sockets for multi-machine communication.

**No Session Management:** Cannot handle reconnections, state persistence, timeouts. *Future:* Session IDs, timeouts, renegotiation triggers.

**GUI Thread Blocking:** Heavy crypto on main thread could freeze UI. *Future:* Background threading with QThread/asyncio.

### 8.2 Missing Features

**Digital Signatures:** No RSA/ECDSA; cannot prove origin or non-repudiation. *Future:* RSA signature integration.

**PKI:** No certificate infrastructure; cannot verify public keys. *Future:* Simple certificate system.

**Secure Storage:** Keys lost on close; no persistent sessions. *Future:* Encrypted keystore with master password.

**Multi-User Support:** Only two clients; no group messaging. *Future:* Multiple clients with roster management.

**Message History:** No persistent storage or conversation review. *Future:* Encrypted message database.

### 8.3 Proposed Enhancements

**Short-Term (1-2 weeks):** Add HMAC, improve logging timestamps, implement input validation, uniform error handling.

**Medium-Term (1 month):** Network implementation, key fingerprints, session management, threading.

**Long-Term (2-3 months):** AES-GCM upgrade, Double Ratchet forward secrecy, certificate support, message persistence, group messaging, file transfer.

### 8.4 Educational vs. Production Use

This project excels as an educational tool (clear principles demonstration, interactive visualization, hands-on tradeoffs) but is not production-ready due to missing authentication/integrity, single-instance limitation, and lack of formal security analysis. Production systems require formal protocol design, extensive auditing, defense-in-depth, and ongoing maintenance.

---

## 9. Conclusion

### 9.1 Achievements

This project successfully demonstrates secure communication per P01 specifications:

**Cryptographic Implementation:** AES-256-CBC with PKCS#7 padding providing strong confidentiality with random IVs preventing pattern analysis.

**Key Exchange:** Classic Diffie-Hellman with RFC 3526 parameters enabling shared secret establishment without prior secure channels.

**User Interface:** Intuitive PyQt5 desktop application with real-time cryptographic operation observation and comprehensive logging.

**Attack Simulations:** Four distinct attacks demonstrating computational infeasibility of brute-force, encryption vs. authentication distinction, DH passive eavesdropping resistance, and availability protection needs.

**Educational Impact:** Successfully bridges theoretical cryptography and practical implementation with hands-on security concept experience.

### 9.2 Key Lessons

**Cryptography is Complex:** Even "simple" encryption requires careful attention to padding, IV generation, key derivation. Well-tested libraries essential.

**Encryption Alone Insufficient:** Message injection clearly shows confidentiality ≠ integrity/authentication. Multiple complementary mechanisms required.

**Security is Contextual:** No absolute security; appropriate to threat model. Educational tradeoffs differ from production requirements.

**Limitations Matter:** Understanding what systems DON'T protect is as critical as understanding protections. Honest assessment enables better security decisions.

### 9.3 Objectives Met

All five primary objectives achieved per P01 specifications:

- ✅ **Objective 1:** AES-256-CBC with PKCS#7 padding
- ✅ **Objective 2:** Classic Diffie-Hellman with proper parameters
- ✅ **Objective 3:** Intuitive desktop GUI with feedback
- ✅ **Objective 4:** Four required attack simulations
- ✅ **Objective 5:** Security principles demonstration

### 9.4 Final Thoughts

Secure communication underpins modern computing. This project provides foundational understanding of encryption algorithms, key exchange protocols, and security attacks—the same principles in production systems used by billions daily.

While intentionally simplified for education, the core concepts demonstrated here translate to real-world security. The limitations discussed aren't failures but learning opportunities. True security requires understanding basics first, then adding sophistication: authentication, forward secrecy, secure channels, defense-in-depth.

This project serves as a starting point for deeper cryptography exploration. The field is vast, evolving, and critically important. Every student gaining practical understanding becomes better equipped to build secure systems our digital society depends upon.

### 9.5 Recommendations

**For Students:**
- Experiment with the code and modify parameters
- Exploit the identified limitations
- Research how production systems address these issues
- Use this as a foundation for further study

**For Instructors:**
- Use as a demonstration tool in cryptography lectures
- Assign extensions as homework (add HMAC, implement RSA signatures)
- Have students conduct security reviews and propose improvements
- Encourage implementation of the future work items

**For Practitioners:**
- Recognize this as an educational tool, not production code
- Use it to explain security concepts to non-technical stakeholders
- Appreciate the value of simple demonstrations in security education

---

## 10. References

### Cryptographic Standards

1. National Institute of Standards and Technology (NIST). "Advanced Encryption Standard (AES)." FIPS PUB 197, November 2001.
2. National Institute of Standards and Technology (NIST). "Recommendation for Block Cipher Modes of Operation." SP 800-38A, December 2001.
3. Krawczyk, H., Bellare, M., and R. Canetti. "HMAC: Keyed-Hashing for Message Authentication." RFC 2104, February 1997.
4. Kivinen, T. and M. Kojo. "More Modular Exponential (MODP) Diffie-Hellman groups for Internet Key Exchange (IKE)." RFC 3526, May 2003.

### Cryptographic Algorithms

5. Daemen, J. and V. Rijmen. "The Design of Rijndael: AES - The Advanced Encryption Standard." Springer-Verlag, 2002.
6. Diffie, W. and M. Hellman. "New Directions in Cryptography." IEEE Transactions on Information Theory, vol. IT-22, no. 6, pp. 644-654, November 1976.
7. Kaliski, B. "PKCS #7: Cryptographic Message Syntax Version 1.5." RFC 2315, March 1998.

### Security Analysis

8. Ferguson, N., Schneier, B., and T. Kohno. "Cryptography Engineering: Design Principles and Practical Applications." Wiley, 2010.
9. Menezes, A., van Oorschot, P., and S. Vanstone. "Handbook of Applied Cryptography." CRC Press, 1996.
10. Katz, J. and Y. Lindell. "Introduction to Modern Cryptography." 2nd Edition, CRC Press, 2014.

### Implementation Resources

11. Python Software Foundation. "secrets — Generate secure random numbers for managing secrets." Python Documentation.
12. Pycryptodome Contributors. "PyCryptodome Documentation." Version 3.20.0.
13. Riverbank Computing Limited. "PyQt5 Reference Guide." 2023.

### Attack Methodologies

14. Vaudenay, S. "Security Flaws Induced by CBC Padding." Advances in Cryptology - EUROCRYPT 2002, pp. 534-545, 2002.
15. Bleichenbacher, D. "Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS #1." Advances in Cryptology - CRYPTO '98, pp. 1-12, 1998.

### Related Protocols

16. Signal. "Signal Protocol." Technical Documentation. https://signal.org/docs/
17. Rescorla, E. "The Transport Layer Security (TLS) Protocol Version 1.3." RFC 8446, August 2018.
18. OpenSSL Project. "OpenSSL Cryptography and SSL/TLS Toolkit." https://www.openssl.org/

### Educational Resources

19. Boneh, D. and V. Shoup. "A Graduate Course in Applied Cryptography." Stanford University, 2020.
20. Stallings, W. "Cryptography and Network Security: Principles and Practice." 8th Edition, Pearson, 2020.

---

## Appendix A: Installation Quick Reference

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Install dependencies and run
pip install -r requirements.txt
python GUI/main_window.py
```

## Appendix B: Code Structure

```
ics344_project/
├── README.md, USER_GUIDE.md, TECHNICAL_REPORT.md
├── requirements.txt, .gitignore
├── diffie_hellman.py          # DH implementation
├── aes_encryption.py          # AES-CBC implementation
└── GUI/
    ├── main_gui.ui            # Qt Designer definition
    ├── gui.py                 # Auto-generated PyQt5
    └── main_window.py         # Application logic
```

## Appendix C: Glossary

| Term | Definition |
|------|------------|
| **AES** | Advanced Encryption Standard - Symmetric encryption algorithm using 128-bit blocks |
| **CBC** | Cipher Block Chaining - Block cipher mode where each block is XORed with previous ciphertext |
| **DH** | Diffie-Hellman - Key exchange protocol based on discrete logarithm problem |
| **HMAC** | Hash-based Message Authentication Code - For verifying integrity and authenticity |
| **IV** | Initialization Vector - Random value used to initialize CBC mode encryption |
| **MAC** | Message Authentication Code - Cryptographic checksum to verify message integrity |
| **MITM** | Man-in-the-Middle - Attack where adversary intercepts communication |
| **PKCS#7** | Padding scheme for block ciphers |
| **SHA-256** | Cryptographic hash function producing 256-bit output |

---

## Document Information

| Property | Value |
|----------|-------|
| **Version** | 2.0 (Condensed) |
| **Date** | November 2025 |
| **Pages** | ~7-8 pages (formatted) |
| **Project** | ICS344 Secure Communication System |
| **Bucket** | P01 (Python \| AES-CBC PKCS#7 \| Diffie-Hellman \| Desktop) |

---

**End of Technical Report**
