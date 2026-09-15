class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def simulate(k):
            res = 0
            for pile in piles:
                res += math.ceil(pile / k)

            return res
        
        arr = []
        l = 1
        r = max(piles)
        while l <= r:
            k = (l + r) // 2
            
            time = simulate(k)

            if time <= h:
                arr.append(k)
                r = k - 1
            elif time > h:
                l = k + 1
        
        return min(arr)
            
            
