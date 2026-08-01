class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.length = len(nums)

        def dfs(nums, current):
            if len(current) == self.length:
                self.res.append(current.copy())
                return
            
            for index, num in enumerate(nums):
                current.append(num)
                dfs(nums[:index] + nums[index + 1:], current)
                current.pop()

        current = []
        dfs(nums, current)
        return self.res
        
