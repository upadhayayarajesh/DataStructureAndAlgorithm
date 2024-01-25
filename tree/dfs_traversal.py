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
        :param root:
        :return:
        """
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)
