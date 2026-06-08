class Solution:
    def maxArea(self, heights: List[int]) -> int:
        value = 0
        for l in range(len(heights)):
            for r in range(len(heights)):
                if l == r:
                    continue
                width = r - l
                height = min(heights[l], heights[r])
                if width * height > value:
                    value = width * height
        
        return value
