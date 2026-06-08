class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        output = nums[0]

        if len(nums) < 3:
            return min(nums)

        if nums[l] < nums[r]:
            return output
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[l] > nums[mid]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid
        
        return output

        