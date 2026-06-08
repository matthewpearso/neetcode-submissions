class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        
        current_lmax = 0
        current_rmax = 0
        l = 0
        r = len(height) - 1
        while l < len(height):
            left = height[l]
            right = height[r]
            if left > current_lmax:
                left_max.append(left)
                current_lmax = left
            else:
                left_max.append(current_lmax)
        
            if right > current_rmax:
                right_max.insert(0, right)
                current_rmax = right
            else:
                right_max.insert(0, current_rmax)
            
            l += 1
            r -= 1
        

        total_water = 0
        for i in range(len(height) - 1):
            total_water += min(right_max[i], left_max[i]) - height[i]
        
        return total_water
        



        
        