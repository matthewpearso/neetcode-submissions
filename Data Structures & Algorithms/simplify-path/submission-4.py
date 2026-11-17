'''
Approach:
We can easily identify what is a directory and what is an operation by storing what exists between two forward slashes. By storing each directory in a stack, if we get a .. operation, then we just pop from the stack. At the end, we put it all together.
'''


class Solution:
    def simplifyPath(self, path: str) -> str:
        element = ''
        stack = []
        for i, c in enumerate(path):
                
            if c == '/' or i == len(path) - 1:
                if i == len(path) - 1 and c != '/':
                    element += c

                if element == '..' and stack:
                    stack.pop() 
                elif element != '' and element != '..' and element != '.':
                    stack.append(element)
                element = ''
                continue

            element += c
        
        res = '/'
        for i in range(len(stack)):
            element = stack[i]
            if i != len(stack) - 1:
                element += '/'
            res += element
        
        return res


            


            
        

