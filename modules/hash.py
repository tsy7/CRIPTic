# this file for classes :)

import hashlib
class Hash:
    def __init__(self, crypt):
        self.crypt = crypt

    def getWord(self):
        """
        here is result code and Hash
        """
        self.md5 = hashlib.md5(self.crypt.encode()).hexdigest()
        self.sha1 = hashlib.sha1(self.crypt.encode()).hexdigest()
        self.sha256 = hashlib.sha256(self.crypt.encode()).hexdigest()
        self.sha512 = hashlib.sha512(self.crypt.encode()).hexdigest()
        self.sha224 = hashlib.sha224(self.crypt.encode()).hexdigest()
        self.sha384 = hashlib.sha384(self.crypt.encode()).hexdigest()
        self.sha3_512 = hashlib.sha3_512(self.crypt.encode()).hexdigest()
        self.sha3_384 = hashlib.sha3_384(self.crypt.encode()).hexdigest()

    def Tabules(self):
        self.Data = [["MD5", hashlib.md5(self.crypt.encode()).hexdigest()],
        ["Sha1", hashlib.sha1(self.crypt.encode()).hexdigest()],
        ["Sha256", hashlib.sha256(self.crypt.encode()).hexdigest()],
        ["Sha512", hashlib.sha512(self.crypt.encode()).hexdigest()],
        ["Sha224", hashlib.sha224(self.crypt.encode()).hexdigest()],
        ["Sha384", hashlib.sha384(self.crypt.encode()).hexdigest()],
        ["Sha3_512", hashlib.sha3_512(self.crypt.encode()).hexdigest()],
        ["Sha3_384", hashlib.sha3_384(self.crypt.encode()).hexdigest()]]

