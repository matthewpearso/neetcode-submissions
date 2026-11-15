'''
This is a divide and conquer merge sort algorithm that recursively breaks apart the array into individual parts and merges the sorted versions back up the recursive tree.

I'll need one algorithm to break apart the array recursively, and another to put it back together.

Break apart algorithm:

- Base case: when there is at most one element in the array
- Find midpoint of current array
- Call recursive case on left and right halves of the array
- Return the merged (helper function) left and right pieces which will be sorted

Merging Algorithm:

- Create a new list to store the sorted result
- Given the left and right arrays, iterate through both using index pointers starting at 0
- Each iteration, pick the element that is lesser, append it to result then move the respective pointer for that element
- Iterate until you reach the end of one array
- If either right or left array still has remaining elements, append them to the result, as this should be sorted at this point
- Return result
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
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
















