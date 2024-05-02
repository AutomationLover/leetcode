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
    prev_node = TreeNode(-float('inf'))
    x = y = None
    for node in inorder(root):
        if x is None:
            if node.val < prev_node.val:
                x = prev_node
        else:
            if node.val < prev_node.val:
                y = node
                break
        prev_node = node
    print(x.val)
    print(y.val)
    
    
    
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


def test1():
    pass
