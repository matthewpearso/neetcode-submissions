class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        numBoats = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
            else:
                r -= 1
            
            numBoats += 1
        
        return numBoats
