'''
Objective: return the element in an array that is the majority given that there will always be a majority element.

My approach: O(n) search straight through, using a hashmap to count frequencies, return the max. Space should be O(n/2) -> O(n)


'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        return max(freq, key=freq.get)