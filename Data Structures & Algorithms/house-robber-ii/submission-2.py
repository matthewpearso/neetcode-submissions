class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
                val = -1
                for j in nums:
                    if j > val:
                        val = j
                return val
        
        memo_1 = [-1] * (len(nums) - 1)
        memo_2 = [-1] * (len(nums) - 1)
        nums_1 = nums[0:len(nums)-1]
        nums_2 = nums[1:len(nums)]
        
        return max(self.dfs(0, nums_1, memo_1), self.dfs(0, nums_2, memo_2))

    def dfs(self, i, nums, memo):
            if i > len(nums)-1:
                return 0
            if memo[i] != -1:
                return memo[i]
            else:
                memo[i] = max(nums[i] + self.dfs(i+2, nums, memo), self.dfs(i+1, nums, memo))
            return memo[i]