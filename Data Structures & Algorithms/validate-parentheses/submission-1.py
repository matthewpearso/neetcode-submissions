class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comp = {'(':')', '{':'}', '[':']'}
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                continue
            if len(stack) < 1:
                return False
            if comp.get(stack.pop()) != s[i]:
                return False
        if len(stack) > 0:
            return False
        return True
            