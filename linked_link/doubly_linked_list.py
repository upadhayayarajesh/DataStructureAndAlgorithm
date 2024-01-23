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


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_begin(3)
    doubly_linked_list.insert_begin(2)
    doubly_linked_list.insert_begin(4)
    doubly_linked_list.display()
