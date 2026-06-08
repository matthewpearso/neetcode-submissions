class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        output = nums[0]
        while l <= r:
            mid = (l + r) // 2
            
            if nums[l] < nums[r]:
                output = min(output, nums[l])
                break
            
            output = min(output, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return output

        