from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

class AESEncryptor:
    def __init__(self, key: bytes = None):
        self.key = key or get_random_bytes(32)  # 256-bit key
        self.cipher = AES.new(self.key, AES.MODE_CBC)

    def encrypt(self, data: str) -> str:
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.cipher.iv)
        padded_data = pad(data.encode(), AES.block_size)
        encrypted = cipher.encrypt(padded_data)
        return base64.b64encode(self.cipher.iv + encrypted).decode()

    def decrypt(self, enc_data: str) -> str:
        raw = base64.b64decode(enc_data)
        iv = raw[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        padded = cipher.decrypt(raw[16:])
        return unpad(padded, AES.block_size).decode()