import pyscrypt

class Encode:

    def hash_password(self, password):
        salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
        password = bytes(password, encoding='utf-8')
        key = pyscrypt.hash(password, salt, 2048, 8, 1, 32)
        return key.hex()

    def verify(self, hash, password):
        hash2 = self.hash_password(password)
        return hash == hash2
