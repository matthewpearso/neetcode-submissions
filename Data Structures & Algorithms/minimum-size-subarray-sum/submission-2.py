class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLength = math.inf
        l = r = 0
        total = nums[l]
        while l < len(nums):
            if total >= target:
                minLength = min(r - l + 1, minLength)
                total -= nums[l]
                l += 1
            elif r == len(nums) - 1:
                total -= nums[l]
                l += 1
            else:
                r += 1
                total += nums[r]
        
        return minLength if minLength < math.inf else 0