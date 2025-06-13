import random

class HashTableAssignment:
    def __init__(self, table_size=10):
        self.m = table_size
        self.p = 109345121  # large prime
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        self.table = [[] for _ in range(self.m)]
        self.size = 0

    def _hash(self, key):
        key_hash = hash(key) if isinstance(key, str) else key
        return ((self.a * key_hash + self.b) % self.p) % self.m

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, _) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
        self.size += 1

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, _) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                self.size -= 1
                return True
        return False

    def load_factor(self):
        return self.size / self.m

if __name__ == "__main__":

    hash_table = HashTableAssignment(table_size=7)

    # Insert key-value pairs
    hash_table.insert("Football", 20)
    hash_table.insert("BasketBall", 10)
    hash_table.insert("Jogging", 30)
    hash_table.insert("Climbing", 40)
    hash_table.insert("Running", 50)

    print("Search Football:", hash_table.search("Football"))  # should return 20
    print("Search Running:", hash_table.search("Running"))      # should return 50
    print("Search Ski:", hash_table.search("ski"))    # should return None

    # Delete a key
    print("Delete Climbing:", hash_table.delete("Climbing"))  # should return True
    print("Search Climbing:", hash_table.search("Climbing"))  # should return None

    # Check load factor
    print("Current Load Factor:", hash_table.load_factor())