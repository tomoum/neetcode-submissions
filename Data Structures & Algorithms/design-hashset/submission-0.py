class MyHashSet:

    def __init__(self):
        self.size = 101
        self.container = [None] * self.size
        
    def index(self, key: int)-> int:
        return (key * 2654435761) % self.size

    def add(self, key: int) -> None:
        self.container[self.index(key)] = key

    def remove(self, key: int) -> None:
        self.container[self.index(key)] = None
        

    def contains(self, key: int) -> bool:
        return self.container[self.index(key)] == key
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)