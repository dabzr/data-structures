import mmh3
from faker import Faker
from itertools import product
from random import sample
fake = Faker()


class BitArray:
    def __init__(self, size):
        self.barray = [0] * (size%32)
    def set(self, idx):
        i = (idx//32)%(len(self.barray))
        bi = idx%32
        self.barray[i] |= 1 << bi 
    def get(self, idx):
        i = (idx//32)%(len(self.barray))
        bi = idx%32
        return (self.barray[i] >> bi) & 1

class Lista:
    def __init__(self, barray_size, hash_quantity):
        self.list = []
        self.size = barray_size
        self.bit_array = BitArray(barray_size)
        self.seeds = sample(range(1, 141115), hash_quantity)
    def append(self, item):
        self.list.append(item)
        for seed in self.seeds:
            self.bit_array.set(mmh3.hash(str(item), signed=False, seed=seed)%self.size)
    def __contains__(self, key):
        for seed in self.seeds:
            if self.bit_array.get(mmh3.hash(str(key), signed=False, seed=seed)%self.size) != 1:
                return False
        return True

quantities = [50, 250, 500]
hashes = [3, 6, 9]
spans = [50, 180, 350]
emails = [200, 500, 1000]
for quantity, hashy, span, email in product(quantities, hashes, spans, emails):
    lst = Lista(quantity, hashy)
    for i in range(span):
        lst.append(fake.email())
    randemails = [fake.email() for i in range(email)]
    print(f"{quantity}, {hashy}, {span}, {emails}",end=": ")
    print(len(list(filter(lambda x: x in lst, randemails))))

