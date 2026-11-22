class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.points[(x,y)] = self.points.get((x,y), 0) + 1
        return

    def count(self, point: List[int]) -> int:
        count = 0
        x1 = point[0]
        y1 = point[1]
        for v in self.points.keys():
            x2 = v[0]
            y2 = v[1]
            
            isValid = abs(x1 - x2) == abs(y1 - y2) and (x1 != x2 and y1 != y2)
            
            if (isValid and self.points.get((x1, y2), False) and self.points.get((x2, y1), False)):
                multiplier = self.points.get((x1, y1), 1) * self.points[(x1,y2)] * self.points[(x2,y1)] * self.points[(x2, y2)]
                count += (1 * multiplier)
        
        return count

