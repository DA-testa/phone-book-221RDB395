class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash_function(self, key):
        return hash(key) % self.size
        
    def add(self, number, name):
        index = self._hash_function(number)
        for i, (n, _) in enumerate(self.table[index]):
            if n == number:
                self.table[index][i] = (number, name)
                return
        self.table[index].append((number, name))
        
    def delete(self, number):
        index = self._hash_function(number)
        for i, (n, _) in enumerate(self.table[index]):
            if n == number:
                del self.table[index][i]
                return
        
    def find(self, number):
        index = self._hash_function(number)
        for n, name in self.table[index]:
            if n == number:
                return name
        return "not found"


phone_book = HashTable()

n = int(input())
for i in range(n):
    query = input().split()
    if query[0] == "add":
        phone_book.add(query[1], query[2])
    elif query[0] == "del":
        phone_book.delete(query[1])
    elif query[0] == "find":
        print(phone_book.find(query[1]))
