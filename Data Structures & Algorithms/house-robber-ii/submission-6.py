class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return max(nums)
        
        nums1 = nums[:n-1]
        nums2 = nums[1:]

        def dp(arr):
            memo = [-1] * len(arr)
            memo[0] = arr[0]
            memo[1] = max(arr[0], arr[1])

            for i in range (2, len(arr)):
                memo[i] = max(memo[i-1], arr[i] + memo[i-2])
            
            return memo[-1]
        
        return max(dp(nums1), dp(nums2))
        
