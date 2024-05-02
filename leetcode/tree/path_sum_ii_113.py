#  https://leetcode.cn/problems/path-sum-ii/description/
# 113. 路径总和 II
#  dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(root, target):
            if not root:
                return
            if not root.left and not root.right:
                if target == root.val:
                    res.append(path[:]+[root.val])
                return

            target -= root.val
            path.append(root.val)
            for child in [root.left, root.right]:
                if child:
                    dfs(child, target)
            path.pop()
            target += root.val


        dfs(root, targetSum)
        return res
