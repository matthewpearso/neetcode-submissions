class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        
        hashmap = {}
        for num in nums:
            if num - 1 not in num_set:
                hashmap[num] = []
                i = 1
                while num + i in num_set:
                    hashmap[num].append(num + i)
                    i += 1
                    
        result = 0
        for value in hashmap.values():
            if len(value) + 1 > result:
                result = len(value) + 1

        return result
