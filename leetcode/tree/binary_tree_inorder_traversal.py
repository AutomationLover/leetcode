class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def test():
    # Create a simple binary tree
    #         1
    #        / \
    #       2   3
    #      /   / \
    #     4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print()
    ans = inorder(root)
    print(ans)
    ans = inorderTravelsal(root)
    print(ans)
    ans = preorder(root)
    print(ans)
    ans = preorderTravelsal(root)
    print(ans)
    ans = postorder(root)
    print(ans)
    ans = postorderTravelsal(root)
    print(ans)
    
def inorder(root, res=[]):
    if root is None:
        return res
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)
    return res

def preorder(root, res=[]):
    if root is None:
        return res
    res.append(root.val)
    preorder(root.left, res)
    preorder(root.right, res)
    return res

def postorder(root, res=[]):
    if root is None:
        return res
    postorder(root.left, res)
    postorder(root.right, res)
    res.append(root.val)
    return res
#  need further processing (WHITE) and those ready to be output (GRAY),
# The color-coding (using WHITE and GRAY) effectively manages the state of each node in the traversal process:
#
# WHITE signifies that the node is yet to be explored. This means we need to process its left child, then the node itself, and finally its right child. By pushing nodes onto the stack with the WHITE tag, we're queuing them for further exploration.
#
# GRAY indicates that the node's left child has been dealt with, and now the node itself can be processed (i.e., its value can be added to the result list), followed by its right child.
def inorderTravelsal(root):
    WHITE, GRAY = 0, 1
    res = []
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
            res.append(node.val)
    return res

def preorderTravelsal(root):
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None:
            continue
        if color == WHITE:
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
            stack.append((GRAY, node))
        else:
            res.append(node.val)
    return res

def postorderTravelsal(root):
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None:
            continue
        if color == WHITE:
            stack.append((GRAY, node))
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
        else:
            res.append(node.val)
    return res