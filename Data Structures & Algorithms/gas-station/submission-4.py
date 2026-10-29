class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        
        total = 0
        start = 0
        for i in range(len(diff)):
            if total == 0 and diff[i] < 0:
                start = i + 1
                continue
            
            total += diff[i]

            if total < 0:
                start = i + 1
                total = 0
        
        return start
        
