from tree.Tree import Tree


class DFS_Traversal:
    """
    Depth First Search traversals
    """

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
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(h), where h is the height of the tree.
        """
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data)


if __name__ == '__main__':
    tree = Tree()
    tree.initialize_sample_tree()
    root = tree.get_root()
    dfs = DFS_Traversal()
    print("Inorder Traversal")
    dfs.inorder_traversal(root)
    print("Preorder Traversal")
    dfs.preorder_traversal(root)
    print("Postorder Traversal")
    dfs.postorder_traversal(root)
