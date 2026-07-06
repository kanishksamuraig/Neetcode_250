class minheap:
    def __init__(self,nums):
        self.nums=nums
        self.size=len(nums)
        for i in range(len(nums)-1,-1,-1):
            curr=i
            while True:
                smallest=curr
                lchild=2*curr+1
                rchild=2*curr+2
                
                if lchild < self.size and self.nums[lchild]<self.nums[smallest]:
                    smallest=lchild
                
                if rchild < self.size and self.nums[rchild] < self.nums[smallest]:
                    smallest=rchild 

                if smallest==curr:
                    break
                self.nums[curr],self.nums[smallest]=self.nums[smallest],self.nums[curr]
                curr=smallest
    
    def push(self,val):
        self.nums.append(val)
        curr=self.size
        self.size+=1
        while curr>0 and self.nums[curr] < self.nums[(curr-1)//2]:
            self.nums[curr],self.nums[(curr-1)//2]=self.nums[(curr-1)//2],self.nums[curr]
            curr=(curr-1)//2 
    
    def pop(self):
        min1=self.nums[0]
        self.size-=1
        self.nums[0]=self.nums[self.size]
        self.nums.pop()
        curr=0
        while True:
            smallest=curr
            lchild = 2*curr+1
            rchild = 2*curr+2
            if lchild < self.size and self.nums[lchild]<self.nums[smallest]:
                smallest=lchild
            
            if rchild < self.size and self.nums[rchild] < self.nums[smallest]:
                smallest=rchild
            
            if smallest==curr:
                return min1
            
            self.nums[smallest],self.nums[curr]=self.nums[curr],self.nums[smallest]
            curr=smallest
        return min1
            

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap=minheap(nums)
        self.k=k
        while self.heap.size>k:
            self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.push(val)
        if self.heap.size>self.k:
            self.heap.pop()
        return self.heap.nums[0]


    