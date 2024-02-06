

# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0

    return max(height(node.left), height(node.right)) + 1


def diameter(root):
    if root is None:
        return 0
    lHeight = height(root.left)
    rHeight = height(root.right)
    lDiameter = diameter(root.left)
    rDiameter = diameter(root.right)

    return max(lHeight + rHeight + 1, max(lDiameter, rDiameter))


def printLevelOrder(node):
    h = height(node)
    # Level Order
    # for i in range(1, h+1):
    # ReverseLevel Order
    # for i in range(h+1, 0, -1):
    for i in range(1, h+1):
        print("")
        print("Level: ",i, end=" ||        ")
        printCurrentLevel(node, i)


def printCurrentLevel(node, level):
    if node is None:
        return
    if level == 1:
        print(node.val, end=' ')
    elif level > 1:
        printCurrentLevel(node.left, level-1)
        printCurrentLevel(node.right, level-1)


# Driver program to test above function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.right.left = Node(6)
    # root.right.right = Node(7)

    print("Level order traversal of binary tree is -")
    # printLevelOrder(root)
    print(diameter(root))
