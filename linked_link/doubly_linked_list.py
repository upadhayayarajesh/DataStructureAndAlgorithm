class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = Node()


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
