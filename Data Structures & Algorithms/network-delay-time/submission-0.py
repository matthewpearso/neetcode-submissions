class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for edge in times:
            adj[edge[0]].append((edge[1], edge[2]))

        pq = []
        heapq.heappush(pq, (0, k))
        t = 0
        visited = set()
        while pq:
            time1, src = heapq.heappop(pq)
            if src in visited:
                continue
            visited.add(src)
            t = time1
            
            for targ, time2 in adj[src]:
                if targ not in visited:
                    heapq.heappush(pq, (time1 + time2, targ))
            
        if len(visited) < n:
            return -1
        
        return t
                    
            

        





