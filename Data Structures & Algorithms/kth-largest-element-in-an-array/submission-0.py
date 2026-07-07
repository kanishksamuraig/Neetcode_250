class minheap:
    def __init__(self):
        self.heap=[]
    def push(self,val):
        curr=len(self.heap)
        self.heap.append(val)
        while curr>0 and self.heap[curr]<self.heap[(curr-1)//2]:
            self.heap[curr],self.heap[(curr-1)//2]=self.heap[(curr-1)//2],self.heap[curr]
            curr=(curr-1)//2
    def pop(self):
        curr=0
        val=self.heap[0]
        if not self.heap:
            return -100001
        self.heap[0]=self.heap[len(self.heap)-1]
        self.heap.pop()
        while True:
            smallest=curr
            lchild = 2*curr+1
            rchild = 2*curr + 2

            if lchild < len(self.heap) and self.heap[lchild] < self.heap[smallest]:
                smallest = lchild

            if rchild < len(self.heap) and self.heap[rchild] < self.heap[smallest]:
                smallest = rchild

            if smallest == curr:
                return val

            self.heap[smallest],self.heap[curr]=self.heap[curr],self.heap[smallest]
            curr=smallest
        return val        
    def __len__(self):
        return len(self.heap)
    def __getitem__(self,index):
        return self.heap[index]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=minheap()
        for i in range(len(nums)):
            heap.push(nums[i])
            if len(heap)>k:
                heap.pop()
        return heap[0]
                
        