'''
Objective: return the element in an array that is the majority given that there will always be a majority element.

My approach: O(n) search straight through, using a hashmap to count frequencies, return the max. Space should be O(n/2) -> O(n)


'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        i = 1
        res = nums[0]
        count = 1
        while i < len(nums):
            if nums[i] == res:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                res = nums[i]
                count = 1
            
            i += 1

        return res






