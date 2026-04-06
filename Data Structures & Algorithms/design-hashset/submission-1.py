class MyHashSet:

    def __init__(self):
        self.size=1000
        self.hash=[[] for _ in range(self.size)]
    def hashkey(self,key):
        return key%self.size
    def add(self, key: int) -> None:
        data=self.hashkey(key)
        if key not in self.hash[data]:
            self.hash[data].append(key)
    def remove(self, key: int) -> None:
        data=self.hashkey(key)
        if key in self.hash[data]:
            for i in range(len(self.hash[data])):
                if self.hash[data][i]==key:
                    r=i
                    while(r<len(self.hash[data])-1):
                        self.hash[data][r]=self.hash[data][r+1]
                    self.hash[data].pop()
    def contains(self, key: int) -> bool:
        data=self.hashkey(key)
        for i in range(len(self.hash[data])):
            if self.hash[data][i]==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)