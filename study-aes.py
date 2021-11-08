import base64
from hashlib import md5
from Crypto.Cipher import AES


class AESCipher:
    """
    Usage:
        c = AESCipher("password").encrypt("message")
        m = AESCipher("password").decrypt(c)
    """

    def __init__(self, key: str):
        self.key = md5(key.encode("utf-8")).hexdigest()

    def pkcs7padding(self, s: str):
        BLOCK_SIZE = AES.block_size
        return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

    def encrypt(self, msg: str):
        cipher = AES.new(self.key.encode("utf-8"), AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(self.pkcs7padding(msg).encode("utf-8")))

    def decrypt(self, enc: str):
        cipher = AES.new(self.key.encode("utf-8"), AES.MODE_ECB)
        return cipher.decrypt(base64.b64decode(enc)).decode("utf-8")


if __name__ == "__main__":
    msg = input("Message...: ")
    pwd = input("Password..: ")

    ciphertext = AESCipher(pwd).encrypt(msg)
    print("Ciphtext:", ciphertext)
    print("Rawtext:", AESCipher(pwd).decrypt(ciphertext))
