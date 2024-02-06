from LevelOrderTraversal import printLevelOrder

class Tree:
    def __init__(TreeOps, val=None):
        TreeOps.val = val
        TreeOps.left = TreeOps.right = None


class TreeOps:
    @staticmethod
    def search(root, key):

        if root is None or root.key == key:
            return root

        # Key is greater than root's key
        if root.key < key:
            return TreeOps.search(root.right, key)

        # Key is smaller than root's key
        return TreeOps.search(root.left, key)

    @staticmethod
    def insert(root, val):
        if root is None:
            return Tree(val)
        else:
            if val < root.val:
                root.left = TreeOps.insert(root.left, val)
            elif val >= root.val:
                root.right = TreeOps.insert(root.right, val)

        return root

    @staticmethod
    def inorderTraversal(tree):
        if tree is None:
            return
        TreeOps.inorderTraversal(tree.left)
        print(tree.val)
        TreeOps.inorderTraversal(tree.right)

    @staticmethod
    def LevelOrderTraversal(root):
        printLevelOrder(root)