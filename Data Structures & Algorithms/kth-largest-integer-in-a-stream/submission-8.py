class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def push(self,element):
        self.heap.append(element)
        curr = self.size
        self.size+=1
        while curr > 0 and self.heap[curr] < self.heap[(curr-1)//2]:
            self.heap[curr],self.heap[(curr-1)//2] = self.heap[(curr-1)//2],self.heap[curr]
            curr = (curr-1)//2
    def pop(self):
        if self.size==0:
            return -float('inf')
        val = self.heap[0]
        self.size-=1
        self.heap[0] = self.heap[self.size]
        curr = 0
        self.heap.pop()
        while True:
            smallest = curr
            lchild = 2*curr+1
            rchild = 2*curr+2
            if lchild < self.size and self.heap[lchild] < self.heap[smallest]:
                smallest = lchild
            if rchild < self.size and self.heap[rchild] < self.heap[smallest]:
                smallest = rchild

            if smallest == curr:
                return val

            self.heap[curr],self.heap[smallest] = self.heap[smallest],self.heap[curr]
            curr = smallest 
        return val
    def __len__(self):
        return self.size

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap()
        for num in nums:
            self.heap.push(num)
            if len(self.heap)>k:
                self.heap.pop()
        self.k = k
        

    def add(self, val: int) -> int:
        self.heap.push(val)
        if len(self.heap)>self.k:
            self.heap.pop()
        return self.heap.heap[0]

        