from TreeMod import Tree, TreeOps


def LevelOrderTraversalTest(root, level, st):
    if root is None:
        return st

    if level in st:
        st[level] += [root.val]
    else:
        st[level] = [root.val]

    st1 = LevelOrderTraversalTest(root.left, level+1, st)
    st2 = LevelOrderTraversalTest(root.right, level+1, st)
    st1.update(st2)
    return st1


def LevelOrderTraversalRaw(root):
    res = []
    if root is None:
        return res
    queue = []
    queue.append(root)
    while queue:
        n = len(queue)
        print(n)
        temp = []
        for i in range(n):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            temp += [node.val]
        res.append(temp)

    return res


def LevelOrderTraversalRaw2(root):
    q = []
    if root is None:
        return q
    res = []
    q.append(root)
    while q:
        temp = []
        n = len(q)
        for i in range(n):
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            temp.append(node.val)
        res.append(temp)
    return res


if __name__ == '__main__':
    arr = [11, 9, 20, 15, 27]
    root = None
    for i in arr:
        root = TreeOps.insert(root, i)

    print(LevelOrderTraversalRaw2(root))
    # TreeOps.LevelOrderTraversal(root)
    # st = LevelOrderTraversalTest(root, 1, {})
    # order = True
    # for i in st.keys():
    #     if order:
    #         print(st[i])
    #     else:
    #         print(st[i][::-1])
    #     order = not order
