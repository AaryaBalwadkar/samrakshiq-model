import pytest
import time
from src.transform.redact.apply import redact_entities
from src.transform.hash.apply import hash_entities
from src.transform.pseudo.apply import pseudonymize_entities
from src.transform.fpe.apply import fpe_entities
from src.keystroke.crypto.aes import AESEncryptor

real_messages = [
    "SBI: Txn to +919876543210, ID: SBI-1234, card 4111-1111-1111-1111.",
]

@pytest.mark.parametrize("text", real_messages)
def test_roundtrip_performance(text):
    aes = AESEncryptor()
    
    # Measure redaction
    start = time.time()
    redacted = redact_entities(text)
    redact_time = time.time() - start
    
    # Measure hashing
    start = time.time()
    hashed = hash_entities(text)
    hash_time = time.time() - start
    
    # Measure pseudonymization
    start = time.time()
    pseudo = pseudonymize_entities(text)
    pseudo_time = time.time() - start
    
    # Measure FPE
    start = time.time()
    fpe = fpe_entities(text)
    fpe_time = time.time() - start
    
    # Measure AES encryption
    start = time.time()
    encrypted = aes.encrypt(text)
    decrypted = aes.decrypt(encrypted)
    aes_time = time.time() - start
    
    print(f"Original: {text}")
    print(f"Redacted: {redacted}, Time: {redact_time:.4f}s")
    print(f"Hashed: {hashed}, Time: {hash_time:.4f}s")
    print(f"Pseudo: {pseudo}, Time: {pseudo_time:.4f}s")
    print(f"FPE: {fpe}, Time: {fpe_time:.4f}s")
    print(f"Encrypted: {encrypted}, Decrypted: {decrypted}, Time: {aes_time:.4f}s")
    assert text == decrypted, "AES roundtrip failed"