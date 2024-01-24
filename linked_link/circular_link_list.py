class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Circular_linked_list:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def insert_head(self, data):
        if self.size == 0:
            self.head.data = data
            self.head.next = self.head
            self.size += 1
        else:
            new_node = Node(data)
            new_node.next = self.head.next
            self.head.next = new_node
            self.head.next.data = self.head.data
            self.head.data = data
            self.size += 1

    def insert_tail(self, data):
        head = self.head
        if self.size == 0:
            self.head.data = data
            self.size += 1
        else:
            curr = self.head
            while curr.next.data != head.data:
                curr = curr.next
            new_node = Node(data)
            new_node.next = self.head
            curr.next = new_node

    def display(self):
        if self.size == 0:
            return
        res = ""
        head = self.head
        curr = self.head
        while curr.next != head:
            res += str(curr.data) + " "
            curr = curr.next
        res += str(curr.data)
        print(res)


if __name__ == "__main__":
    cll = Circular_linked_list()
    cll.insert_head(10)
    cll.insert_head(30)
    cll.insert_head(20)
    cll.insert_tail(40)
    cll.display()
