class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = (math.sqrt((0 - x) ** 2 + (0 - y) ** 2))
            dist.append((distance, point))
        
        heapq.heapify_max(dist)
        while len(dist) > k:
            heapq.heappop_max(dist)
        
        output = []
        for node in dist:
            output.append(node[1])
        
        return output

        
