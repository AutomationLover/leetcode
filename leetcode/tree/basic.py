class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


def backup_tree(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result


def recover_tree(data):
    if not data:
        return None
    
    iter_data = iter(data)
    root = TreeNode(next(iter_data))
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        try:
            left_val = next(iter_data)
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            right_val = next(iter_data)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        except StopIteration:
            break
    return root


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
    
    # Backup the tree to a list
    backup_list = backup_tree(root)
    print("Backup list:", backup_list)
    
    # Recover the tree from the list
    recovered_tree = recover_tree(backup_list)

    # Helper function to print the tree level by level to verify recovery
    def print_tree_by_level(root):
        if not root:
            return "Empty Tree"

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []
            for i in range(level_size):
                node = queue.popleft()
                if node:
                    level.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level.append("null")
            result.append(" ".join(level))

        return "\n".join(result)

    # Print the recovered tree
    print("Recovered Tree Level by Level:")
    print(print_tree_by_level(recovered_tree))