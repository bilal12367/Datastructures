

# Python program to print left view of Binary Tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive function print left view of a binary tree
def leftViewUtil(root, level, max_level):
    if root is None:
        return

    # If this is the first node of its level
    if (max_level[0] < level):
        print(root.data, end=" ")
        max_level[0] = level

    # Recur for left and right subtree
    leftViewUtil(root.right, level + 1, max_level)
    leftViewUtil(root.left, level + 1, max_level)


def inorderTraversal(tree):
    if tree is None:
        return
    inorderTraversal(tree.left)
    print(tree.data)
    inorderTraversal(tree.right)


def insert(root, val):
    if root is None:
        return Node(val)
    else:
        if val < root.data:
            root.left = insert(root.left, val)
        elif val >= root.data:
            root.right = insert(root.right, val)

    return root

# A wrapper over leftViewUtil()


def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)


if __name__ == '__main__':
    arr = [5, 2, 12, 6, 85, 45, 43, 92, 12, 7, 11]
    tree = None
    for i in arr:
        tree = insert(tree, i)

    inorderTraversal(tree)
    # print(search(tree, 3).val)
    leftView(tree)
