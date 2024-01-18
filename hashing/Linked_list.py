class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def delete(self, key):
        current = self.head
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


