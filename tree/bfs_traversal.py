from queue import Queue


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BFS_Traversal:
    """
    Breadth First Search traversals
    """

    def __init__(self):
        self.root = Node

    def bfs_traversal(self, root):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root.data is None:
            return
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            print(node.data)
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)


if __name__ == '__main__':
    tree = BFS_Traversal()
    tree.root.data = 10
    tree.root.left = Node(20)
    tree.root.right = Node(30)
    tree.root.left.left = Node(40)
    tree.root.left.right = Node(50)
    tree.root.right.right = Node(70)
    tree.bfs_traversal(tree.root)
