class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            updateSet = set()
            for j in dp:
                updateSet.add(j + nums[i])
                updateSet.add(j)
            dp = updateSet
        
        return target in dp



        