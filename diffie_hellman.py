"""
Diffie-Hellman Key Exchange Implementation
Classic DH for secure key agreement between two parties
"""
import secrets
import hashlib


class DiffieHellman:
    """
    Classic Diffie-Hellman Key Exchange
    Uses a safe prime and generates shared secrets
    """
    
    # RFC 3526 - 2048-bit MODP Group (Group 14)
    # This is a standardized safe prime for DH
    PRIME = int(
        "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
        "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
        "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
        "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
        "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
        "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"
        "83655D23DCA3AD961C62F356208552BB9ED529077096966D"
        "670C354E4ABC9804F1746C08CA18217C32905E462E36CE3B"
        "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9"
        "DE2BCBF6955817183995497CEA956AE515D2261898FA0510"
        "15728E5A8AACAA68FFFFFFFFFFFFFFFF", 16
    )
    
    # Generator (commonly 2 or 5)
    GENERATOR = 2
    
    def __init__(self):
        """Initialize DH with a random private key"""
        # Private key: random integer between 2 and prime-2
        self.private_key = secrets.randbelow(self.PRIME - 2) + 2
        
        # Public key: g^private mod p
        self.public_key = pow(self.GENERATOR, self.private_key, self.PRIME)
        
        # Shared secret (will be computed after key exchange)
        self.shared_secret = None
        self.shared_key = None
    
    def get_public_key(self):
        """
        Get the public key to send to the other party
        
        Returns:
            int: Public key
        """
        return self.public_key
    
    def get_public_key_hex(self):
        """
        Get the public key as a hexadecimal string
        
        Returns:
            str: Public key in hex format
        """
        return hex(self.public_key)[2:]  # Remove '0x' prefix
    
    def compute_shared_secret(self, other_public_key):
        """
        Compute the shared secret using the other party's public key
        
        Args:
            other_public_key (int): The other party's public key
            
        Returns:
            bytes: 32-byte shared secret (SHA-256 hash of the raw secret)
        """
        # Shared secret: other_public^private mod p
        raw_shared_secret = pow(other_public_key, self.private_key, self.PRIME)
        
        # Convert to bytes and hash to get a fixed-length key
        raw_bytes = raw_shared_secret.to_bytes(256, byteorder='big')
        
        # Use SHA-256 to derive a 32-byte key (for AES-256)
        self.shared_secret = raw_shared_secret
        self.shared_key = hashlib.sha256(raw_bytes).digest()
        
        return self.shared_key
    
    def get_shared_key(self):
        """
        Get the computed shared key
        
        Returns:
            bytes: 32-byte shared key for AES-256
        """
        if self.shared_key is None:
            raise ValueError("Shared key not computed yet. Call compute_shared_secret() first.")
        return self.shared_key
    
    def get_shared_key_hex(self):
        """
        Get the shared key as a hexadecimal string
        
        Returns:
            str: Shared key in hex format
        """
        if self.shared_key is None:
            raise ValueError("Shared key not computed yet. Call compute_shared_secret() first.")
        return self.shared_key.hex()
    
    @staticmethod
    def from_hex_public_key(hex_public_key):
        """
        Convert a hexadecimal public key string to an integer
        
        Args:
            hex_public_key (str): Public key in hex format
            
        Returns:
            int: Public key as integer
        """
        return int(hex_public_key, 16)


def demonstrate_key_exchange():
    """
    Demonstrate Diffie-Hellman key exchange between Alice and Bob
    """
    print("=" * 60)
    print("Diffie-Hellman Key Exchange Demonstration")
    print("=" * 60)
    
    # Alice generates her key pair
    alice = DiffieHellman()
    print(f"\n[Alice] Generated private key: {alice.private_key}")
    print(f"[Alice] Computed public key: {alice.get_public_key()}")
    print(f"[Alice] Public key (first 32 chars): {alice.get_public_key_hex()[:32]}...")
    
    # Bob generates his key pair
    bob = DiffieHellman()
    print(f"\n[Bob] Generated private key: {bob.private_key}")
    print(f"[Bob] Computed public key: {bob.get_public_key()}")
    print(f"[Bob] Public key (first 32 chars): {bob.get_public_key_hex()[:32]}...")
    
    # Exchange public keys (in real scenario, this happens over the network)
    print("\n" + "=" * 60)
    print("Exchanging public keys...")
    print("=" * 60)
    
    alice_public = alice.get_public_key()
    bob_public = bob.get_public_key()
    
    # Both compute the shared secret
    alice_shared = alice.compute_shared_secret(bob_public)
    bob_shared = bob.compute_shared_secret(alice_public)
    
    print(f"\n[Alice] Computed shared key: {alice.get_shared_key_hex()[:32]}...")
    print(f"[Bob] Computed shared key: {bob.get_shared_key_hex()[:32]}...")
    
    # Verify they match
    print("\n" + "=" * 60)
    if alice_shared == bob_shared:
        print("✅ SUCCESS! Both parties have the same shared key!")
        print(f"Shared Key: {alice.get_shared_key_hex()}")
    else:
        print("❌ ERROR! Keys don't match!")
    print("=" * 60)
    
    return alice, bob


if __name__ == "__main__":
    demonstrate_key_exchange()
