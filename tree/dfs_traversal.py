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
    tree = DFS_Traversal()
    tree.root.data = 10
    tree.root.left = Node(20)
    tree.root.right = Node(30)
    tree.root.left.left = Node(40)
    tree.root.left.right = Node(50)
    tree.root.right.right = Node(70)
    tree.node_distance(tree.root, 2)
