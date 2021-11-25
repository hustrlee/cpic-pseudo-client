from hashlib import md5
from base64 import b64encode, b64decode
from Crypto.Cipher import AES


def pad(s: str, block_size=AES.block_size) -> bytes:
    """
    PKCS7 填充

    Args:
        s: 待填充的字符串
        block_size: 块的大小。默认为 AES 的块大小：16 bytes

    returns:
        经过 PKCS7 填充的“字节串”
    """
    s = s.encode("utf-8")
    return s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size).encode("utf-8")


def unpad(s: bytes, block_size=AES.block_size) -> str:
    """
    PKCS7 去填充

    Args:
        s: 待去填充的“字节串”
        block_size: 块的大小。默认为 AES 的块大小：16 bytes

    returns:
        经过 PKCS7 去填充的字符串
    """
    return s[:-ord(s[len(s)-1:])].decode("utf-8")


class AESCipher:
    """
    Usage:
        c = AESCipher("password").encrypt("message")
        m = AESCipher("password").decrypt(c)
    """

    def __init__(self, key_plaintext: str):
        """
        用密钥明文，初始化密钥（key）。
        由于 AES 算法要求密钥（key）的长度为 16/24/32，因此使用密钥明文的 32bits MD5 值作为密钥。

        Args:
            key_plaintext: 密钥明文
        """
        self.key = \
            md5(key_plaintext.encode("utf-8")).hexdigest().encode("utf-8")

    def encrypt(self, msg: str):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return b64encode(cipher.encrypt(pad(msg))).decode("utf-8")

    def decrypt(self, enc: str):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(b64decode(enc)))


if __name__ == "__main__":
    msg = input("Message...: ")
    pwd = input("Password..: ")

    ciphertext = AESCipher(pwd).encrypt(msg)
    print("Ciphtext:", ciphertext)
    print("Plaintext:", AESCipher(pwd).decrypt(ciphertext))
