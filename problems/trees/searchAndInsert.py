class Tree:
    def __init__(self, val=None):
        self.val = val
        self.left = self.right = None


def search(root, key):

    if root is None or root.key == key:
        return root

    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


def insert(root, val):
    if root is None:
        return Tree(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        elif val >= root.val:
            root.right = insert(root.right, val)

    return root


def inorderTraversal(tree):
    if tree is None:
        return
    inorderTraversal(tree.left)
    print(tree.val)
    inorderTraversal(tree.right)


if __name__ == '__main__':
    arr = [5, 2, 12, 6, 85, 45, 43, 92, 12, 7, 11]
    tree = None
    for i in arr:
        tree = insert(tree, i)

    inorderTraversal(tree)
    # print(search(tree, 3).val)
