from queue import Queue


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    """
    Binary Tree Data Structure
    """

    def __init__(self):
        self.root = Node

    def initialize_sample_tree(self):
        self.root.data = 10
        self.root.left = Node(20)
        self.root.right = Node(30)
        self.root.left.left = Node(40)
        self.root.left.right = Node(50)
        self.root.right.right = Node(70)

    def get_root(self):
        return self.root

    def height(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(h), where h is the height of the tree.
        """
        if root is not None:
            return 1 + max(self.height(root.left), self.height(root.right))
        else:
            return 0

    def node_distance(self, root, K):
        """
         Time Complexity: O(N)
         Space Complexity: O(h), where h is the height of the tree.
        """
        if root is not None:
            if K == 0:
                print(root.data)
            else:
                K -= 1
                self.node_distance(root.left, K)
                self.node_distance(root.right, K)

    def tree_size(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(h), where h is the height of the tree
        """

        if root is None:
            return 0
        else:
            return 1 + self.tree_size(root.left) + self.tree_size(root.right)

    def tree_maximum(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(h), where h is the height of the tree
        """
        if root is None:
            return float('-inf')
        else:
            return max(root.data, self.tree_maximum(root.left), self.tree_maximum(root.right))

    def tree_left(self, root):
        """
        Print only the left child if two child is only one child print that child
        """
        if root is not None:
            queue = Queue()
            queue.put(root)
            while not queue.empty():
                size = queue.qsize()
                for i in range(size):
                    node = queue.get()
                    if i == 0:
                        print(node.data)
                    if node.left is not None:
                        queue.put(node.left)
                    if node.right is not None:
                        queue.put(node.right)


if __name__ == '__main__':
    tree = Tree()
    tree.initialize_sample_tree()
    root = tree.get_root()
    print(tree.height(root))
    tree.node_distance(root, 2)
    print(tree.tree_size(root))
    print(tree.tree_maximum(root))
    tree.tree_left(root)
