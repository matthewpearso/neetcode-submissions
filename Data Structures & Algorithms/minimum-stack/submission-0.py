class MinStack:

    def __init__(self):
        self.items = []
        self.currentMin = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.currentMin) < 1 or val < self.currentMin[len(self.currentMin) - 1]:
            self.currentMin.append(val)
        else:
            self.currentMin.append(self.currentMin[len(self.currentMin) - 1])

    def pop(self) -> None:
        self.items.pop()
        self.currentMin.pop()

    def top(self) -> int:
        return self.items[len(self.items) - 1]

    def getMin(self) -> int:
        return self.currentMin[len(self.currentMin) - 1]
        
