class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.age = -1
        self.cache = {}
        self.lt = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.age += 1
        self.lt[key] = self.age
        
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            if key not in self.cache:
                i = min(self.lt, key=self.lt.get)
                del self.lt[i]
                del self.cache[i]
            
                self.cache[key] = value
        else:
            if key not in self.cache:
                self.cap -= 1
                
        self.cache[key] = value
        self.age += 1
        self.lt[key] = self.age


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


