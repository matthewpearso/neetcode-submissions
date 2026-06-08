class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        result = [0] * len(temps)
        stack = []
        for i in range(len(temps)):
            while len(stack) > 0 and temps[i] > stack[len(stack) - 1][0]:
                top = stack.pop()
                result[top[1]] = i - top[1]
            stack.append([temps[i], i])

        return result


                

        
