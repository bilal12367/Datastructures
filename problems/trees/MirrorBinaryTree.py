class Tree:
    def __init__(self, val=None):
        self.val = val
        self.left = self.right = None

def mirrorify(root, mirror):
 
    if (root == None) :
        mirror = None
        return mirror
     
    # Create new mirror node 
    # from original tree node
    mirror = Tree(root.val)
    mirror.right = mirrorify(root.left, 
                           ((mirror).right))
    mirror.left = mirrorify(root.right, 
                          ((mirror).left))
    return mirror

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
    tree = mirrorify(tree, None)
    print("After Mirrorify")
    inorderTraversal(tree)
    # print(search(tree, 3).val)
