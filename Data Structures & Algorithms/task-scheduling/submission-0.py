class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [count for count in freq.values()]

        heapq.heapify_max(maxHeap)
        time = 0
        queue = deque()

        while maxHeap or queue:
            time += 1
            if maxHeap:
                best = heapq.heappop_max(maxHeap)
                if best - 1 != 0:
                    queue.append([best - 1, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush_max(maxHeap, queue.popleft()[0])
            
        return time
        



        