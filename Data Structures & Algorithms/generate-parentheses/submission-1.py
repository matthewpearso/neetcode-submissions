class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def recurse(opened, closed, current):
            if opened > n or closed > opened:
                return
            
            if opened == closed and opened == n:
                self.res.append(current)
            
            open_new = recurse(opened + 1, closed, current + "(")
            
            close_old = recurse(opened, closed + 1, current + ")")
        
        current = "("
        recurse(1, 0, current)
        return self.res
