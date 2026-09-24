class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        maxDist = math.inf
        bestL = None
        l, r = 0, k - 1

        while r < len(arr):
            curMax = 0
            curArr = arr[l:r + 1]
            for num in curArr:
                diff = abs(num - x)
                curMax += diff
            
            if curMax < maxDist:
                maxDist = curMax
                bestL = l
            
            l += 1
            r += 1
        
        return arr[bestL:bestL + k]



        