
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal( root):
    if root is None:
        return
    
    inorder_traversal(root.left)
    inorder_traversal(root.right)
    print("Val: ",root.val)

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result