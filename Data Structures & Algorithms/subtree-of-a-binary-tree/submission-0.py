# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        def sameTree(root, subroot):
            if not root and not subroot:
                return True
            equal = root and subroot and root.val == subroot.val
            if equal:
                left = sameTree(root.left, subroot.left)
                right = sameTree(root.right, subroot.right)
                return left and right
            else:
                return False
        
        if sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        



