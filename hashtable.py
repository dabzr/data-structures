class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=100):
        self.table = [None] * size
        self.__keys = []
        self.capacity = size

    def hash(self, key):
        return sum(map(ord, str(key))) % self.capacity
    def keys(self):
        return self.__keys
    def __setitem__(self, key, value):
        idx = self.hash(key)
        if self.table[idx] is None:
            self.table[idx] = Node(key, value)
            self.__keys.append(key)
            return
        current = self.table[idx]
        while True:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                current.next = Node(key, value)
                self.__keys.append(key)
                return
            current = current.next

    def __getitem__(self, key):
        idx = self.hash(key)
        if self.table[idx] is None:
            return None
        current = self.table[idx]
        while True:
            if current.key == key:
                return current.value
            if current.next == None:
                return None
            current = current.next

a = HashTable()
a["V"] = 3
print(a["V"])
a["K"] = 5
a["V"] = 6
print(a["V"])
print(a.keys())
