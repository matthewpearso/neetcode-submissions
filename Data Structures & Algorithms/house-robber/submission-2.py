class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        def dfs(i):
            if i > n - 1:
                return 0
            
            if i == n - 1:
                return nums[i]
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            
            return cache[i]
        
        return dfs(0)


