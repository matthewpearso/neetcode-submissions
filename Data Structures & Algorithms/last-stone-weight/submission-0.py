class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop_max(maxHeap)
            y = heapq.heappop_max(maxHeap)
            if x == y:
                continue
            if x < y:
                heapq.heappush_max(maxHeap, (y-x))
            else:
                heapq.heappush_max(maxHeap, (x-y))
        
        return maxHeap[0] if maxHeap else 0
