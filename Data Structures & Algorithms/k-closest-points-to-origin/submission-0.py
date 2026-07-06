class maxheap:
    def __init__(self):
        self.points = []

    def distance(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)

    def insert(self, point):
        curr = len(self.points)
        self.points.append(point)
        val = self.distance(point)

        while curr>0 and val > self.distance(self.points[(curr-1)//2]):
            self.points[curr],self.points[(curr-1)//2]=self.points[(curr-1)//2],self.points[curr]
            curr=(curr-1)//2
        
    def delete(self)->List[int]:
        if len(self.points)==0:
            return [-10000,-10000]
        curr=0
        point=self.points[0]
        self.points[0]=self.points[len(self.points)-1]
        self.points.pop()

        while True:
            largest = curr
            lchild = 2*curr+1
            rchild = 2*curr+2

            if lchild<len(self.points) and self.distance(self.points[lchild]) > self.distance(self.points[largest]):
                largest=lchild
            
            if rchild < len(self.points) and self.distance(self.points[rchild]) > self.distance(self.points[largest]):
                largest=rchild
            
            if largest==curr:
                return point

            self.points[curr],self.points[largest] = self.points[largest], self.points[curr]
            curr=largest
        return point
    def __len__(self):
        return len(self.points)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=maxheap()
        for i in range(len(points)):
            heap.insert(points[i])
            if len(heap)>k:
                heap.delete()
            
        return heap.points




