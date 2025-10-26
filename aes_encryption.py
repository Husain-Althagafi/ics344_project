"""
AES Encryption Module for ICS344 Project
Implements AES encryption and decryption using CBC mode
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


class AESEncryption:
    """
    AES Encryption/Decryption handler
    Uses AES-256 in CBC mode with PKCS7 padding
    """
    
    def __init__(self, key=None):
        """
        Initialize AES encryption with a key
        
        Args:
            key (bytes): 16, 24, or 32 bytes key for AES-128, AES-192, or AES-256
                        If None, a random 32-byte key (AES-256) will be generated
        """
        if key is None:
            self.key = get_random_bytes(32)  # AES-256
        else:
            if len(key) not in [16, 24, 32]:
                raise ValueError("Key must be 16, 24, or 32 bytes long")
            self.key = key
    
    def encrypt(self, plaintext):
        """
        Encrypt plaintext using AES
        
        Args:
            plaintext (str): The text to encrypt
            
        Returns:
            str: Base64 encoded string containing IV + ciphertext
        """
        # Convert plaintext to bytes
        plaintext_bytes = plaintext.encode('utf-8')
        
        # Generate a random IV (Initialization Vector)
        iv = get_random_bytes(16)
        
        # Create cipher object
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        # Pad the plaintext to be multiple of 16 bytes and encrypt
        ciphertext = cipher.encrypt(pad(plaintext_bytes, AES.block_size))
        
        # Combine IV and ciphertext, then encode to base64 for easy transmission
        encrypted_data = iv + ciphertext
        return base64.b64encode(encrypted_data).decode('utf-8')
    
    def decrypt(self, encrypted_data):
        """
        Decrypt AES encrypted data
        
        Args:
            encrypted_data (str): Base64 encoded string containing IV + ciphertext
            
        Returns:
            str: Decrypted plaintext
        """
        # Decode from base64
        encrypted_bytes = base64.b64decode(encrypted_data)
        
        # Extract IV (first 16 bytes) and ciphertext
        iv = encrypted_bytes[:16]
        ciphertext = encrypted_bytes[16:]
        
        # Create cipher object
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        # Decrypt and unpad
        decrypted_padded = cipher.decrypt(ciphertext)
        plaintext_bytes = unpad(decrypted_padded, AES.block_size)
        
        return plaintext_bytes.decode('utf-8')
    
    def get_key_hex(self):
        """
        Get the key as a hexadecimal string
        
        Returns:
            str: Hexadecimal representation of the key
        """
        return self.key.hex()
    
    @staticmethod
    def from_hex_key(hex_key):
        """
        Create an AESEncryption instance from a hexadecimal key string
        
        Args:
            hex_key (str): Hexadecimal string representation of the key
            
        Returns:
            AESEncryption: New instance with the provided key
        """
        key_bytes = bytes.fromhex(hex_key)
        return AESEncryption(key_bytes)


# Example usage
if __name__ == "__main__":
    # Create an AES encryption instance
    aes = AESEncryption()
    
    # Print the key (in production, keep this secret!)
    print(f"Generated Key (hex): {aes.get_key_hex()}")
    
    # Original message
    message = "Hello, this is a secret message for ICS344 project!"
    print(f"\nOriginal message: {message}")
    
    # Encrypt the message
    encrypted = aes.encrypt(message)
    print(f"\nEncrypted (base64): {encrypted}")
    
    # Decrypt the message
    decrypted = aes.decrypt(encrypted)
    print(f"\nDecrypted message: {decrypted}")
    
    # Verify
    print(f"\nVerification: {message == decrypted}")
    
    # Example with a specific key
    print("\n" + "="*50)
    print("Using a specific key:")
    hex_key = aes.get_key_hex()
    aes2 = AESEncryption.from_hex_key(hex_key)
    
    encrypted2 = aes2.encrypt("Another secret message")
    print(f"Encrypted: {encrypted2}")
    print(f"Decrypted: {aes2.decrypt(encrypted2)}")
