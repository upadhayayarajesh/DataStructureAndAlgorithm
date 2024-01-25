class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class DFS_Traversal:
    """
    Depth First Search traversals
    """

    def __init__(self):
        self.root = Node

    def inorder_traversal(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(h), where h is the height of the tree.
        """
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(h), where h is the height of the tree.
        """
        if root is not None:
            print(root)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(h), where h is the height of the tree.
        """
        if root is not None:
            self.postorder_traversal(root.right)
            print(root)
