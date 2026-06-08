class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i], (target - position[i]) / speed[i]))
        
        cars.sort(key=lambda item: item[0], reverse=True)

        stack = []
        for i in range(len(cars)):
            stack.append(cars[i][2])
            if len(stack) > 1 and stack[len(stack) - 1] <= stack[len(stack) - 2]:
                stack.pop()
    
        return len(stack)
