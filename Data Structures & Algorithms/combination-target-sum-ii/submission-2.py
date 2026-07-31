class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dup = set()

        def recurse(candidates, index, remainder, current):
            if remainder == 0:
                self.res.append(current.copy())
                return
            
            if remainder < 0 or index > len(candidates) - 1:
                return
            
            num = candidates[index]
            
            current.append(num)
            removed = candidates[:index] + candidates[index+1:]
            choose = recurse(removed, index, remainder - num, current)
            current.pop()
            
            while index < len(candidates) - 1 and candidates[index + 1] == num:
                index += 1
            
            no_choose = recurse(candidates, index + 1, remainder, current)
        
        candidates = sorted(candidates)
        current = []
        recurse(candidates, 0, target, current)
        return self.res

