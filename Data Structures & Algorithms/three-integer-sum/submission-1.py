class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        
        for i in range(len(sorted_nums) - 1):
            
            if sorted_nums[i] > 0:
                break

            if sorted_nums[i] == sorted_nums[i-1] and i > 0:
                continue

            j = i+1
            k = len(sorted_nums) - 1
            
            while j < k:
                if sorted_nums[j] + sorted_nums[k] + sorted_nums[i] < 0:
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] + sorted_nums[i] > 0:
                    k -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    # handle duplicates?
                    j += 1
                    k -= 1
                    while sorted_nums[j] == sorted_nums[j-1] and j < k:
                        j += 1
        
        return result





