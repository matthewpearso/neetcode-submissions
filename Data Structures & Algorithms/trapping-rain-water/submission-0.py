class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        
        current_max = 0
        for left in height:
            if left > current_max:
                left_max.append(left)
                current_max = left
            else:
                left_max.append(current_max)
        
        current_max = 0
        for right in reversed(height):
            if right > current_max:
                right_max.insert(0, right)
                current_max = right
            else:
                right_max.insert(0, current_max)
        

        total_water = 0
        for i in range(len(height) - 1):
            total_water += min(right_max[i], left_max[i]) - height[i]
        
        return total_water
        



        
        