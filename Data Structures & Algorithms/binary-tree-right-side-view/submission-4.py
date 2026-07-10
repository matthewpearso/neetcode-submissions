# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = 0
        levelList = []

        def bfs(root, level, levelList):
            if not root:
                return
            
            if len(levelList) - 1 < level:
                levelList.append([])
            
            levelList[level].append(root.val)
            bfs(root.left, level + 1, levelList)
            bfs(root.right, level + 1, levelList)
        
        bfs(root, level, levelList)
        output = []
        for level in levelList:
            rightmost = level.pop()
            output.append(rightmost)
        
        return output
            




