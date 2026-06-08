class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        
        output = [intervals[0]]

        for i in intervals:
            # if start of i is <= start of previous, merge
            if i[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], i[1]) # merged interval end is max of the two ends
            else:
                output.append(i)
        
        return output
            


        


            