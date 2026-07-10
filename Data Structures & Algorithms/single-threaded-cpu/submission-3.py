class Heap:
    def __init__(self):
        self.heap=[]
        self.size=0
    
    def insert(self,val):
        self.heap.append(val)
        curr=self.size
        self.size+=1

        while curr > 0 and (self.heap[curr][1] < self.heap[(curr-1)//2][1] or (self.heap[(curr-1)//2][1]==self.heap[curr][1] and self.heap[(curr-1)//2][2] > self.heap[curr][2])):
            self.heap[curr],self.heap[(curr-1)//2]=self.heap[(curr-1)//2],self.heap[curr]
            curr = (curr-1)//2
    def delete(self):
        if self.size==0:
            return -1
        val=self.heap[0];
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap.pop()
        curr=0
        while True:
            smallest = curr
            lchild = 2*curr + 1
            rchild = 2*curr + 2

            if lchild < self.size and (self.heap[lchild][1] < self.heap[smallest][1] or (self.heap[smallest][1]==self.heap[lchild][1] and self.heap[smallest][2] > self.heap[lchild][2])):
                smallest = lchild

            if rchild < self.size and (self.heap[rchild][1] < self.heap[smallest][1] or (self.heap[smallest][1]==self.heap[rchild][1] and self.heap[smallest][2] > self.heap[rchild][2])):
                smallest = rchild

            if smallest == curr:
                return val
            
            self.heap[smallest],self.heap[curr] = self.heap[curr], self.heap[smallest]
            curr = smallest
        return val

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        heap = Heap()
        lst = []
        for index,task in enumerate(tasks):
            task.append(index)
            lst.append(task)
        print(lst)
        sortedstack=sorted(lst,key = lambda x: (x[0],x[2]))
        i=0;res=[]
        while i<len(sortedstack) or heap.size > 0:
            if heap.size==0:
                if time < sortedstack[i][0]:
                    time = sortedstack[i][0]
            
            while i<len(sortedstack) and time >= sortedstack[i][0]:
                heap.insert(sortedstack[i])
                i+=1

            if heap.size>0:
                val = heap.delete()
                time+=val[1]
                res.append(val[2])
            
        return res



        

        