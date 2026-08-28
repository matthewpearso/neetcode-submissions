class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        
        adj = defaultdict(list)
        for i in points:
            for j in points:
                i_tup = (i[0], i[1])
                j_tup = (j[0], j[1])
                if i_tup == j_tup:
                    continue
                dist = abs(i[0] - j[0]) + abs(i[1] - j[1])
                adj[i_tup].append((dist, j_tup))
                adj[j_tup].append((dist, i_tup))
        
        start = (0, (points[0][0], points[0][1]))
        minHeap = [start]
        visited = set()
        cost = 0
        while len(visited) < len(points):
            dist, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            cost += dist
            visited.add(point)
            for nbr in adj[point]:
                if nbr[1] not in visited:
                    heapq.heappush(minHeap, nbr)
        
        return cost


