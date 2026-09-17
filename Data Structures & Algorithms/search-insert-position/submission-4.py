class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        res = r

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                res = mid + 1
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res
            
