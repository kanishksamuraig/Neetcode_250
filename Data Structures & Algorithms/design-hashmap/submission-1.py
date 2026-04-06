class MyHashMap:
    def __init__(self):
       self.size=1000
       self.hashmap=[[] for _ in range(self.size)] 
    def put(self, key: int, value: int) -> None:
        hashkey=key%self.size
        for i in range(len(self.hashmap[hashkey])):
            if self.hashmap[hashkey][i][0]==key:
                self.hashmap[hashkey][i][1]=value
                return
        self.hashmap[hashkey].append([key,value])
    def get(self, key: int) -> int:
        hashkey=key%self.size
        for i in range(len(self.hashmap[hashkey])):
            if self.hashmap[hashkey][i][0]==key:
                return self.hashmap[hashkey][i][1]
        return -1
        

    def remove(self, key: int) -> None:
        hashkey=key%self.size
        for i in range(len(self.hashmap[hashkey])):
            if self.hashmap[hashkey][i][0]==key:
                for j in range(i,len(self.hashmap[hashkey])-1):
                    self.hashmap[hashkey][j]=self.hashmap[hashkey][j+1]
                self.hashmap[hashkey].pop()
                return  
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)