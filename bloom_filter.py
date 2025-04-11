import hashlib
import base64

class BloomFilter:
    def __init__(self, m, k):
        self.m = m  # size of bit array
        self.k = k  # number of hash functions
        self.data = [0] * m  # bit array
        self.n = 0  # number of inserted elements

    def insert(self, element):
        element = element.encode()
        if self.k == 1:
            hash1 = h1(element) % self.m
            self.data[hash1] = 1
        elif self.k == 2:
            hash1 = h1(element) % self.m
            hash2 = h2(element) % self.m
            self.data[hash1] = 1
            self.data[hash2] = 1
        self.n += 1

    def search(self, element):
        element = element.encode()
        if self.k == 1:
            hash1 = h1(element) % self.m
            if self.data[hash1] == 0:
                return "Not in Bloom Filter"
        elif self.k == 2:
            hash1 = h1(element) % self.m
            hash2 = h2(element) % self.m
            if self.data[hash1] == 0 or self.data[hash2] == 0:
                return "Not in Bloom Filter"
        prob = (1.0 - ((1.0 - 1.0 / self.m) ** (self.k * self.n))) ** self.k
        return f"Might be in Bloom Filter with false positive probability {prob:.6f}"

def h1(w):
    h = hashlib.md5(w).digest()
    b64 = base64.b64encode(h)[:6]
    return hash(b64)

def h2(w):
    h = hashlib.sha256(w).digest()
    b64 = base64.b64encode(h)[:6]
    return hash(b64)
