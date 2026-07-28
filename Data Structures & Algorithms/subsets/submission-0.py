class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        def recurse(nums, index, subset):
            if index > len(nums) - 1:
                self.res.append(subset)
                return
          
            choose = recurse(nums, index + 1, subset + [nums[index]])
            dont_choose = recurse(nums, index + 1, subset)

        recurse(nums, 0, [])

        return self.res
