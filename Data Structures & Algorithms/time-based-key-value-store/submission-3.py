class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashmap.get(key) == None:
            self.hashmap[key] = [(value, timestamp)]
        else:
            self.hashmap[key].append((value, timestamp))          
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap.keys():
            return ""
        
        arr = self.hashmap[key]
        if len(arr) < 1 or arr[0][1] > timestamp:
            return ""
        
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            if l == r:
                if arr[mid][1] < timestamp:
                    return arr[mid][0]
                else:
                    return arr[mid-1][0]
            
            if arr[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        return ""
        
