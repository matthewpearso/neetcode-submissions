class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for t in tokens:
            if t == "*":
                operands.append(operands.pop() * operands.pop())
            elif t == "+":
                operands.append(operands.pop() + operands.pop())
            elif t == "-":
                i, j = operands.pop(), operands.pop()
                operands.append(j - i)
            elif t == "/":
                i, j = operands.pop(), operands.pop()
                operands.append(int(j / i))
            else:
                operands.append(int(t))
        
        return operands.pop()