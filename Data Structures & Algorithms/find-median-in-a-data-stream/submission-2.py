class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        self.size=0

    def addNum(self, num: int) -> None:
        self.size+=1
        heapq.heappush(self.maxheap,-num)
        if self.size%2==0:
            x=heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-x)
        else:
            if self.minheap and self.minheap[0]<-self.maxheap[0]:
                x=-heapq.heappop(self.maxheap)
                y=heapq.heappop(self.minheap)
                heapq.heappush(self.minheap,x)
                heapq.heappush(self.maxheap,-y)


    def findMedian(self) -> float:
        if self.size%2==0:
            return (-self.maxheap[0]+self.minheap[0])/2
        else:
            return -self.maxheap[0]
        
        