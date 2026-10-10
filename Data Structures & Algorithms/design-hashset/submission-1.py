class MyHashSet:

    def __init__(self):
        self.hashset = [[]] * 1000

    def add(self, key: int) -> None:
        hashkey = key % 1000
        
        for val in self.hashset[hashkey]:
            if val == key:
                return
        
        self.hashset[hashkey].append(key)
        return

    def remove(self, key: int) -> None:
        hashkey = key % 1000
        
        for idx, val in enumerate(self.hashset[hashkey]):
            if val == key:
                self.hashset[hashkey].pop(idx)
                return
        
        return

    def contains(self, key: int) -> bool:
        hashkey = key % 1000
        for idx, val in enumerate(self.hashset[hashkey]):
            if val == key:
                return True
        
        return False




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)