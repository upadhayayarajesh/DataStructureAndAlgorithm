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
        self.size += 1

    def insert_end(self, data):
        """
        Time Complexity: O(n)
        """
        if self.size == 0:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        self.size += 1

    def insert_position(self, data, position):
        """
        Time Complexity: O(position)
        """
        if position > self.size:
            return
        if position == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while position > 1:
                current = current.next
                position -= 1
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def delete_first_node(self):
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next

    def delete_last_node(self):
        if self.head.next:
            current = self.head.next
            pre = self.head
            while current.next:
                pre = current
                current = current.next
            pre.next = None
        else:
            self.head = Node()

    def reverse_linked_list(self):
        """
        Time Complexity: O(N)
        """
        if self.size > 1:
            current = self.head
            prev = None
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next

            self.head = prev


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(30)
    linked_list.append(50)
    linked_list.display()
    linked_list.insert_begin(2)
    linked_list.display()
    linked_list.insert_end(40)
    empty = LinkedList()
    linked_list.display()
    empty.insert_end(5)
    empty.display()
    linked_list.insert_position(27, 3)
    linked_list.display()
    linked_list.delete_first_node()
    linked_list.display()
    linked_list.delete_last_node()
    empty.display()
    empty.delete_first_node()
    empty.display()
    linked_list.display()
    linked_list.reverse_linked_list()
    linked_list.display()
