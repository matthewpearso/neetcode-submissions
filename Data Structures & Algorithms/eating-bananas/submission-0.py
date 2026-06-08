class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        output = r
        
        while l <= r:
            k = (l + r) // 2
            current_h = 0
            
            for p in piles:
                current_h += math.ceil(p / k)
                            
            if current_h > h:
                l = k + 1
            elif current_h <= h:
                r = k - 1
                output = min(output, k)
        
        return output
            

                
        


