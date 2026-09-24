# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root == None:
            return TreeNode(val, None, None)
        
        def dfs(cur, prev):
            if not cur:
                if val > prev.val:
                    prev.right = TreeNode(val, None, None)
                else:
                    prev.left = TreeNode(val, None, None)
                return

            if val > cur.val:
                dfs(cur.right, cur)
            
            if val < cur.val:
                dfs(cur.left, cur)
            
            return
        
        dfs(root, None)

        return root
