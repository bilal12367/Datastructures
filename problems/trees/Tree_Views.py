from TreeMod import Tree as Node, TreeOps


# Recursive function print left view of a binary tree
# def leftViewUtil(root, level, max_level):
#     if root is None:
#         return

#     print(root.val, end=" ")
#     print("Max Lvl: ", max_level[0])
#     print('Level:', level)
#     # If this is the first node of its level
#     if (max_level[0] < level):
#         # print(root.val, end=" ")
#         max_level[0] = level
#     # Recur for left and right subtree
#     leftViewUtil(root.left, level + 1, max_level)
#     leftViewUtil(root.right, level + 1, max_level)

# A wrapper over leftViewUtil()

def LeftViewTree(root, level, st):
    if root is None:
        return

    if level not in st:
        print(root.val, end=" ")
        st[level] = 1

    LeftViewTree(root.left, level + 1, st)
    LeftViewTree(root.right, level + 1, st)


def RightViewTree(root, level, st):
    if root is None:
        return

    if level not in st:
        print(root.val, end=" ")
        st[level] = [root.val]

    RightViewTree(root.right, level+1, st)
    RightViewTree(root.left, level+1, st)


def TopView(root, level, st):
    if root is None:
        return

    if level not in st:
        print(root.val, ' ', level)
        st[level] = 1

    if level > 0:
        TopView(root.right, level+1, st)
        TopView(root.left, level-1, st)
    else:
        TopView(root.left, level-1, st)
        TopView(root.right, level+1, st)


def BottomView(root, level, st):
    if root is None:
        return st

    st[level] = root.val

    st1 = BottomView(root.left, level+1, st)
    st2 = BottomView(root.right, level-1, st)
    st1.update(st2)
    return st1


def leftView(root):
    max_level = [0]
    st = {}
    TopView(root, 0, st)


if __name__ == '__main__':
    arr = [4, 12, 7, 3, 1, 3, 9, 10]
    tree = None
    for i in arr:
        tree = TreeOps.insert(tree, i)

    # TreeOps.inorderTraversal(tree)
    # print(search(tree, 3).val)
    # leftView(tree)
    print(BottomView(tree, 0, {}))
