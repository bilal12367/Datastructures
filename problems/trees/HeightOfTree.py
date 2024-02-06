from TreeMod import Tree, TreeOps


def heightOfTree(root):
    if root is None:
        return 0

    lHeight = heightOfTree(root.left)
    rHeight = heightOfTree(root.right)
    return max(lHeight, rHeight) + 1

if __name__ == '__main__':
    arr = [5,2,7,1,3,6,9,8]
    root = None
    for i in arr:
        root = TreeOps.insert(root,i)

    height = heightOfTree(root)
    print(height)
    