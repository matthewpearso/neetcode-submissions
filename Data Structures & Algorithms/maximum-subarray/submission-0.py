class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        absoluteSum = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            absoluteSum = max(absoluteSum, curSum)
        
        return absoluteSum