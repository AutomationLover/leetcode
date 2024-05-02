class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 94.
def test():
    # Example
    #         1
    #        /
    #       3
    #        \
    #         2
    # need to change to
    #         3
    #        /
    #       1
    #        \
    #         2
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)

    return search(root)
    
def test2():
    # Example
    #         3
    #        / \
    #       1   4
    #          /
    #         2
    # need to change to
    #         2
    #        / \
    #       1   4
    #          /
    #         3
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)

    return search(root)

def search(root):
    prev_node = TreeNode(-float('inf'))
    x = y = None
    seq = []
    for node in inorder(root):
        seq.append(node.val)
        if x is None:
            if node.val < prev_node.val:
                x = prev_node
                y = node
        else:
            if node.val < prev_node.val:
                y = node
                break
        prev_node = node
    if not x and not y:
        x.val, y.val = y.val, x.val
    
    
def inorder(root):
    WHITE, GRAY = 0, 1
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None:
            continue
        if color == WHITE:
            stack.append((WHITE, node.right))
            stack.append((GRAY, node))
            stack.append((WHITE, node.left))
        else:
            yield node


