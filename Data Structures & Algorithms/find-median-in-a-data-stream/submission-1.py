class MedianFinder:
    def __init__(self):
        self.heap=[]
        self.size=0

    def addNum(self, num: int) -> None:
        self.size+=1
        heapq.heappush(self.heap,-num)
        print(self.heap)
    def findMedian(self) -> float:
        lst=[];val=0
        if self.size%2==0:
            i=0
            while i<self.size//2-1:
                lst.append(heapq.heappop(self.heap))
                i+=1
            x=heapq.heappop(self.heap)
            y=heapq.heappop(self.heap)
            val=(-(x+y))/2
            lst.append(x)
            lst.append(y)
        else:
            i=0;
            while i<self.size//2:
                lst.append(heapq.heappop(self.heap))
                i+=1
            val =  -heapq.heappop(self.heap)
            lst.append(-val)
        for i in lst:
            heapq.heappush(self.heap,i)
        return val

            

        