class MyHashSet:

    def __init__(self):
        self.hash=[]

    def add(self, key: int) -> None:
        flag=False
        for i in range(len(self.hash)):
            if self.hash[i]==key:
                return
        self.hash.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hash)):
            if self.hash[i]==key:
                self.hash=self.hash[:i]+self.hash[i+1:]
                return
                

    def contains(self, key: int) -> bool:
        for i in range(len(self.hash)):
            if self.hash[i]==key:
                return True
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)