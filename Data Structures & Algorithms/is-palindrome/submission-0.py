class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        copy =[]
        for char in s:
            if char.isalnum():
                copy.append(char.lower())
                stack.append(char.lower())
        for i in range(len(stack)):
            if stack.pop() != copy[i]:
                return False
        return True