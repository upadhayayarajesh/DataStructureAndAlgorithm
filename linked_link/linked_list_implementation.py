class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation in python
    """

    def __init__(self):
        self.head = Node()
        self.size = 0

    def append(self, data):
        if self.size == 0:
            self.head.data = data
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node = Node(data)
            current.next = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def check(self, data):
        if self.size == 0:
            return False
        else:
            current = self.head
            while current is not None:
                if current.data == data:
                    return True
                current = current.next

    def remove(self, data):
        if self.check(data):
            current = self.head
            while current is not None:
                if current.data == data:
                    current.data = current.next.data
                    break
                current = current.next
        else:
            print("Not found")
            return False

    def display(self):
        display = ""
        current = self.head
        while current is not None:
            display += str(current.data) + " "
            current = current.next
        print(display)

    def insert_begin(self, data):
        """
        Time Complexity: \u03b8(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(30)
    linked_list.append(50)
    linked_list.display()
    linked_list.insert_begin(2)
    linked_list.display()
