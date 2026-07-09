# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left = min(p.val, q.val)
        right = max(p.val, q.val)

        def dfs(root, left, right):
            if root.val <= right and root.val >= left:
                return root
            elif root.val > right:
                return dfs(root.left, left, right)
            elif root.val < left:
                return dfs(root.right, left, right)
        
        return dfs(root, left, right)
            