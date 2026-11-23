class Solution:
    def __init__(self):
        self.record = []
    
    def addScore(self, x: str) -> None:
        self.record.append(int(x))
        return

    def addPrevTwo(self) -> None:
        prevTwo = self.record[-1] + self.record[-2]
        self.record.append(prevTwo)
        return
    
    def addDouble(self) -> None:
        self.record.append(self.record[-1] * 2)
        return

    def remove(self) -> None:
        self.record.pop()
        return
    
    def calPoints(self, operations: List[str]) -> int:
        for op in operations:
            if op == '+':
                self.addPrevTwo()
            elif op == 'D':
                self.addDouble()
            elif op == 'C':
                self.remove()
            else:
                self.addScore(op)
        
        return sum(self.record)