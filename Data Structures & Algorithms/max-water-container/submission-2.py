class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        
        l = 0
        r = len(heights) - 1
        max_amt = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            amt = w * h
            
            if amt > max_amt:
                max_amt = amt

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_amt
            

        
