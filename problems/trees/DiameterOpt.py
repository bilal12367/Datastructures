# Python3 program to find the diameter of a binary tree
# A binary tree Node


class Node:

    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# utility class to pass height object


class Height:
    def __init(self):
        self.h = 0

# Optimised recursive function to find diameter
# of binary tree


def diameterOpt(root, height):
    lh = Height()
    rh = Height()
    if root is None:
        height.h = 0
        return 0
    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)
    height.h = max(lh.h, rh.h) + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))


# function to calculate diameter of binary tree


def diameter(root):
    height = Height()
    return diameterOpt(root, height)


# Driver Code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    """
Constructed binary tree is 
			1
		/ \
		2	 3
		/ \
	4	 5
"""

    print("The diameter of the binary tree is:", end=" ")
    # Function Call
    print(diameter(root))

# This code is contributed by Shweta Singh(shweta44)
