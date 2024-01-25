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


if __name__ == '__main__':
    tree = Tree()
    tree.initialize_sample_tree()
    root = tree.get_root()
    print(tree.height(root))
    tree.node_distance(root, 2)
