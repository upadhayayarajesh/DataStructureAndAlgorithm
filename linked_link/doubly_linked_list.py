class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0

    def insert_begin(self, data):
        """
        Time Complexity: O(1)
        """
        if not self.head.data:
            self.head.data = data
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def display(self):
        """
        Time Complexity: O(n)
        """
        res = ""
        if self.size == 0:
            print(res)
        else:
            curr = self.head
            while curr:
                res += str(curr.data) + " "
                curr = curr.next
        print(res)

    def insert_end(self, data):
        if self.size == 0:
            self.head.data = data
            self.size += 1
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            new_node = Node(data)
            new_node.prev = curr
            curr.next = new_node


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    empty = DoublyLinkedList()
    doubly_linked_list.insert_begin(3)
    doubly_linked_list.insert_begin(2)
    doubly_linked_list.insert_begin(4)
    doubly_linked_list.insert_end(1)
    doubly_linked_list.display()
