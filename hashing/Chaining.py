from hashing.Linked_list import LinkedList


class Chaining:
    def __init__(self, size=7):
        self.hash_table = [None] * size
        self.size = size

    def insert(self, data):
        hash_value = self._hash(data)
        if not self.hash_table[hash_value]:
            linked_list = LinkedList()
            linked_list.insert(data)
            self.hash_table[hash_value] = linked_list
        else:
            self.hash_table[hash_value] = self.hash_table[hash_value].insert(data)

    def search(self, data):
        hash_value = self._hash(data)
        if not self.hash_table[hash_value]:
            return False
        else:
            return self.hash_table[hash_value].search(data)

    def delete(self, data):
        if not self.search(data):
            return False
        else:
            hash_value = hash(data)
            self.hash_table[hash_value].delete(data)

    def _hash(self, value):
        return value % self.size


if __name__ == '__main__':
    chaining = Chaining()
    chaining.insert(70)
    chaining.insert(71)
    print(chaining.search(70))
    print(chaining.search(74))
