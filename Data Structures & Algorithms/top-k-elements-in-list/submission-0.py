class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        counts_list = []
        for key, value in counts.items():
            counts_list.append([key, value])
        sorted_list = sorted(counts_list, key=lambda x : x[1])
        result = []
        for i in range(k):
            result.append(sorted_list.pop()[0])
        return result
        
        