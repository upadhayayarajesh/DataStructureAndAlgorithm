from queue import Queue

from tree.Tree import Tree


class BFS_Traversal:
    """
    Breadth First Search traversals
    """

    def bfs_traversal(self, root):
        """
        Time Complexity: O(n + h), h is the height of the tree
        Space Complexity: O(w) , w is the width of the tree
        """
        if root.data is None:
            return
        res = ""
        queue = Queue()
        queue.put(root)
        queue.put(None)
        while queue.qsize() > 1:
            node = queue.get()
            if node is None:
                res += "\n"
                queue.put(None)
                continue
            res += str(node.data) + " "
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
        print(res)

    def bfs_traversal2(self, root):
        """
        Time Complexity: O(n)
        Space Complexity: O(w) , w is the width of the tree
        """
        if root is not None:
            queue = Queue()
            queue.put(root)
            while not queue.empty():
                count = queue.qsize()
                res = ""
                for i in range(count):
                    node = queue.get()
                    res += str(node.data) + " "
                    if node.left is not None:
                        queue.put(node.left)
                    if node.right is not None:
                        queue.put(node.right)
                print(res)


if __name__ == '__main__':
    tree = Tree()
    tree.initialize_sample_tree()
    root = tree.get_root()
    bfs = BFS_Traversal()
    bfs.bfs_traversal(root)
    bfs.bfs_traversal2(root)
