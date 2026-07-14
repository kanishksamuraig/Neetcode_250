from collections import deque
class LRUCache:
    def __init__(self, capacity: int):
        self.size=capacity
        self.dic={}
        self.queue=deque()
    def get(self, key: int) -> int:
        print(self.queue,"get before",self.dic)
        if key in self.dic:
            queue2=deque()
            while self.queue:
                val = self.queue.popleft()
                if val==key:
                    continue
                queue2.append(val)
            queue2.append(key)
            self.queue=queue2
            print(self.queue,"get after",self.dic)
            return self.dic[key]
        return -1
    def put(self, key: int, value: int) -> None:
        print(self.queue,"put before",self.dic)
        if key in self.dic:
            self.dic[key] = value
            queue2=deque()
            while self.queue:
                val = self.queue.popleft()
                if val==key:
                    continue
                queue2.append(val)
            queue2.append(key)
            self.queue=queue2
            print(self.queue,"put after",self.dic)
            return
        if self.size>0:
            self.dic[key]=value
            self.size-=1
        else:
            key2=self.queue.popleft()
            del self.dic[key2]
            self.dic[key]=value
        self.queue.append(key)

        
