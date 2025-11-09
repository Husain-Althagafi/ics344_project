"""
Main Window Controller
Handles all the logic and connects the GUI buttons to functionality
"""
import sys
from PyQt5 import QtWidgets, QtGui
from gui import Ui_MainWindow, QtCore
import sys
import os
from collections import deque

# Add parent directory to path to import aes_encryption and diffie_hellman
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from aes_encryption import AESEncryption
from diffie_hellman import DiffieHellman


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Main Window class that extends the auto-generated UI
    Add all your custom methods and button connections here
    """
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI from gui.py
        
        # Initialize Diffie-Hellman for both clients
        self.dh_client_a = DiffieHellman()
        self.dh_client_b = DiffieHellman()
        
        # Perform DH key exchange
        self.perform_key_exchange()
        
        # Initialize AES encryption with the shared DH key
        self.shared_aes = AESEncryption(self.dh_client_a.get_shared_key())
        
        # Store the shared key for both clients
        self.aes_client_a = self.shared_aes  # Client A uses shared key
        self.aes_client_b = self.shared_aes  # Client B uses shared key
        
        # Connect buttons to methods
        self.connect_signals()
        
        self._log_buffer = deque(maxlen=2000)

        # Initialize log
        self.log("System initialized with Diffie-Hellman key exchange ✓")
        self.log(f"Client A Public Key: {self.dh_client_a.get_public_key_hex()[:32]}...")
        self.log(f"Client B Public Key: {self.dh_client_b.get_public_key_hex()[:32]}...")
        self.log(f"Shared AES Key: {self.shared_aes.get_key_hex()[:32]}...")
    
    def perform_key_exchange(self):
        """Perform Diffie-Hellman key exchange between Client A and Client B"""
        # Get public keys
        client_a_public = self.dh_client_a.get_public_key()
        client_b_public = self.dh_client_b.get_public_key()
        
        # Exchange and compute shared secrets
        self.dh_client_a.compute_shared_secret(client_b_public)
        self.dh_client_b.compute_shared_secret(client_a_public)
        
        # Verify both clients have the same shared key
        if self.dh_client_a.get_shared_key() != self.dh_client_b.get_shared_key():
            raise ValueError("DH Key exchange failed - keys don't match!")
    
    def connect_signals(self):
        """Connect all button clicks to their handler methods"""
        self.button_A_ES.clicked.connect(self.client_a_encrypt_send)
        self.button_A_DV.clicked.connect(self.client_a_decrypt_verify)
        self.button_B_ES.clicked.connect(self.client_b_encrypt_send)
        self.button_B_DV.clicked.connect(self.client_b_decrypt_verify)
        self.button_attack.clicked.connect(self.simulate_attack)
        
        # Connect menu actions
        self.actionPrint_Logs.triggered.connect(self.print_logs)
    
    def log(self, message):
        """Add a message to the log panel"""
        # current_text = self.log_panel.text()
        # if current_text == "System Logs":
        #     self.log_panel.setText(message)
        # else:
        #     self.log_panel.setText(current_text + "\n" + message)

        if message is None:
            return
        
        self._log_buffer.append(message)

        sb = self.log_panel.verticalScrollBar()
        at_bottom = (sb.value() == sb.maximum())

        self.log_panel.setPlainText("\n".join(self._log_buffer))

        if at_bottom:
            cursor = self.log_panel.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            self.log_panel.setTextCursor(cursor)
            self.log_panel.ensureCursorVisible()
    
    # Client A Methods
    def client_a_encrypt_send(self):
        """Encrypt message from Client A and send to Client B"""
        plaintext = self.text_A.toPlainText()
        
        if not plaintext:
            self.log("Client A: No message to encrypt")
            return
        
        try:
            # Encrypt the message
            encrypted = self.aes_client_a.encrypt(plaintext)
            
            # Send to Client B (display in text_B)
            self.text_B.setPlainText(encrypted)
            
            self.log(f"Client A: Encrypted and sent message")
            self.log(f"Key (hex): {self.aes_client_a.get_key_hex()[:32]}...")
        except Exception as e:
            self.log(f"Client A Error: {str(e)}")
    
    def client_a_decrypt_verify(self):
        """Decrypt and verify message in Client A's text box"""
        encrypted_text = self.text_A.toPlainText()
        
        if not encrypted_text:
            self.log("Client A: No message to decrypt")
            return
        
        try:
            # Use the shared key to decrypt (message was encrypted by Client B)
            decrypted = self.shared_aes.decrypt(encrypted_text)
            self.text_A.setPlainText(decrypted)
            self.log("Client A: Message decrypted successfully ✓")
        except Exception as e:
            self.log(f"Client A: Decryption failed - {str(e)}")
    
    # Client B Methods
    def client_b_encrypt_send(self):
        """Encrypt message from Client B and send to Client A"""
        plaintext = self.text_B.toPlainText()
        
        if not plaintext:
            self.log("Client B: No message to encrypt")
            return
        
        try:
            # Encrypt the message
            encrypted = self.aes_client_b.encrypt(plaintext)
            
            # Send to Client A (display in text_A)
            self.text_A.setPlainText(encrypted)
            
            self.log(f"Client B: Encrypted and sent message")
            self.log(f"Key (hex): {self.aes_client_b.get_key_hex()[:32]}...")
        except Exception as e:
            self.log(f"Client B Error: {str(e)}")
    
    def client_b_decrypt_verify(self):
        """Decrypt and verify message in Client B's text box"""
        encrypted_text = self.text_B.toPlainText()
        
        if not encrypted_text:
            self.log("Client B: No message to decrypt")
            return
        
        try:
            # Use the shared key to decrypt (message was encrypted by Client A)
            decrypted = self.shared_aes.decrypt(encrypted_text)
            self.text_B.setPlainText(decrypted)
            self.log("Client B: Message decrypted successfully ✓")
        except Exception as e:
            self.log(f"Client B: Decryption failed - {str(e)}")
    
    # Attack Simulation
    def simulate_attack(self):
        """Simulate the selected attack type"""
        attack_type = self.attack_type.currentText()
        self.log(f"⚠ Simulating {attack_type} attack...")
        
        if attack_type == "Dictionary":
            self.simulate_dictionary_attack()
        elif attack_type == "Message Injection":
            self.simulate_message_injection()
        elif attack_type == "Session Hijack":
            self.simulate_session_hijack()
        elif attack_type == "Flooding Messages":
            self.simulate_flooding()
    
    def simulate_dictionary_attack(self):
        """Simulate a dictionary attack on encrypted messages"""
        self.log("Dictionary Attack: Attempting to crack encryption...")
        
        total_attempts = 0
        
        try:
            from dictionary import passwords

            shared_key = self.shared_aes
            match = False

            while not match:
                password = passwords[total_attempts]
                total_attempts += 1

                if password == shared_key:
                    self.log(f'Dictionary attack successful, key: {self.shared_aes} matches dictionary value : {password}')
                    match = True

                else:
                    self.log(f'Attempt number {total_attempts}: dictionary password: {password} -  No Match')

            if not match:
                self.log("Dictionary Attack: Failed - AES-256 is secure ✓")        

        except Exception as e:
            print('An error occured when simulating the dictionary attack:', e)



    
    def simulate_message_injection(self):
        """Simulate message injection attack"""
        injected = "HACKED MESSAGE"
        self.text_A.setPlainText(injected)
        self.log("Message Injection: Malicious message injected")
    
    def simulate_session_hijack(self):
        """Simulate session hijacking"""
        self.log("Session Hijack: Attempting to steal session...")
        self.log("Session Hijack: Detection mechanisms active ✓")
    
    def simulate_flooding(self):
        """Simulate message flooding attack"""
        self.log("Flooding Attack: Sending multiple messages...")
        for i in range(5):
            self.log(f"Flood message {i+1}")
    
    # Menu Actions
    def print_logs(self):
        """Print logs to console"""
        print("=== SYSTEM LOGS ===")
        print(self.log_panel.text())
        print("=" * 40)
        self.log("Logs printed to console")
    


def main():
    """Main entry point for the application"""
    # Enable High DPI scaling
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
