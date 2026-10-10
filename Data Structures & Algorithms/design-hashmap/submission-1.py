class MyHashMap:

    def __init__(self):
        self.hashmap = [[]] * 1000

    def put(self, key: int, value: int) -> None:
        hashKey = key % 1000
        
        for idx, pair in enumerate(self.hashmap[hashKey]):
            if pair[0] == key:
                self.hashmap[hashKey][idx] = (key, value)
                return
        
        self.hashmap[hashKey].append((key, value))
        return

    def get(self, key: int) -> int:
        hashKey = key % 1000
        
        for idx, pair in enumerate(self.hashmap[hashKey]):
            if pair[0] == key:
                return pair[1]
        
        return -1

    def remove(self, key: int) -> None:
        hashKey = key % 1000
        
        for idx, pair in enumerate(self.hashmap[hashKey]):
            if pair[0] == key:
                self.hashmap[hashKey].pop(idx)
                return
        
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)