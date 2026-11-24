class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        i = 0
        j = 1
        while j < len(intervals):
            if res[i][1] >= intervals[j][0]:
                res[i] = [res[i][0], max(intervals[j][1], res[i][1])]
            else:
                res.append(intervals[j])
                i += 1
            
            j += 1
        
        return res

            


        


            