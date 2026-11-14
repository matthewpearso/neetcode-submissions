'''
This is a divide and conquer merge sort algorithm that recursively breaks apart the array into individual parts and merges the sorted versions back up the recursive tree.

I'll need one algorithm to break apart the array recursively, and another to put it back together.

'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        def merge(left, right):
            res = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            if i < len(left):
                res += left[i:]
            
            if j < len(right):
                res += right[j:]
            
            return res
        
        return merge(left, right)
                








