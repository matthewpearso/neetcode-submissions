class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def recurse(i, target, current):
            if target == 0:
                self.res.append(current.copy())
                return

            if i >= len(nums) or target < 0:
                return

            current.append(nums[i])
            recurse(i, target - nums[i], current)
            current.pop()
            recurse(i + 1, target, current)

        current = []
        recurse(0, target, current)
        return self.res