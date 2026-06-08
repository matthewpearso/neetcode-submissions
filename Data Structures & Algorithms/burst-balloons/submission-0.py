class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_total = 0
        for i in range(len(nums)):
            if i == 0:
                value = nums[i] * nums[i+1]
            elif i == len(nums)-1:
                value = nums[i-1] * nums[i]
            else:
                value = nums[i-1] * nums[i] * nums[i+1]
            
            sub = self.maxCoins(self.remove(nums, i))
            total = value + sub
            if total > max_total:
                max_total = total
        
        return max_total
    
    def remove(self, array, i):
        new_array = []
        for j in range(len(array)):
            if j != i:
                new_array.append(array[j])
        return new_array