class MyHashMap:

    def __init__(self):
        self.keylist=[]
        self.valuelist=[]
    def put(self, key: int, value: int) -> None:
        if key in self.keylist:
            for index,keye in enumerate(self.keylist):
                if keye==key:
                    self.valuelist[index]=value
                    return
        self.keylist.append(key)
        self.valuelist.append(value)

    def get(self, key: int) -> int:
        for index,keye in enumerate(self.keylist):
            if keye==key:
                return self.valuelist[index]
        return -1
        

    def remove(self, key: int) -> None:
        for index,keye in enumerate(self.keylist):
            if keye==key:
                i=index
                while i<len(self.keylist)-1:
                    self.keylist[i]=self.keylist[i+1]
                    self.valuelist[i]=self.valuelist[i+1]
                    i+=1
                self.keylist.pop()
                self.valuelist.pop()
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)