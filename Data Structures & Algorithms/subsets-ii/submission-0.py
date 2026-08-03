class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums = sorted(nums)

        def dfs(i, current):
            if i == len(nums):
                self.res.append(current.copy())
                return
            
            current.append(nums[i])
            choose = dfs(i + 1, current)
            current.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            skip = dfs(i + 1, current)
        
        current = []
        dfs(0, current)
        return self.res