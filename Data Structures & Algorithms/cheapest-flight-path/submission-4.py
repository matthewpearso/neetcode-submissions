class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for f in flights:
            adj[f[0]].append([f[2], f[1]])
        cost = []
        for i in range(n):
            cost.append([math.inf] * (k+2))
        minHeap = [[0, 0, src]]

        while minHeap:
            c, stops, u = heapq.heappop(minHeap)

            if c > cost[u][stops] or stops == k + 1:
                continue
            
            for c2, v in adj[u]:
                if c + c2 < cost[v][stops + 1]:
                    cost[v][stops + 1] = c + c2
                    heapq.heappush(minHeap, [c + c2, stops + 1, v])
        res = min(cost[dst])
        return res if res != math.inf else -1