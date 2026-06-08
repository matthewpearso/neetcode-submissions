class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}
        solution = []

        for i in range(len(numbers)):
            num = numbers[i]
            comp = target - num
            index_of_comp = complements.get(comp)
            if index_of_comp != None:
                solution.append(complements[comp] + 1)
                solution.append(i + 1)
                return solution
            complements[num] = i
            
        
            
        
                
        

        
