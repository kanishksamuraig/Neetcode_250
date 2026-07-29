class Heap:
    def heappush(self,arr,trip):
        passenger,start,end=trip
        arr.append(trip)
        curr = len(arr)-1
        while curr>0 and end < arr[(curr-1)//2][2]:
            arr[curr],arr[(curr-1)//2] = arr[(curr-1)//2],arr[curr]
            curr = (curr-1)//2
    def heappop(self,arr):
        if len(arr)==0:
            return []
        curr = 0 
        val = arr[0]
        arr[0]=arr[len(arr)-1]
        arr.pop()
        while True:
            smallest = curr
            lchild = 2*curr+1
            rchild = 2*curr + 2
            if lchild<len(arr) and arr[lchild]<arr[smallest]:
                smallest = lchild
            if rchild < len(arr) and arr[rchild] < arr[smallest]:
                smallest = rchild
            if smallest == curr:
                return val
            arr[smallest],arr[curr] = arr[curr],arr[smallest]
            curr=smallest
        return val
        
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dist = 0
        trips.sort(key=lambda x:(x[1]))
        curr = 0
        heap = Heap()
        i=0
        arr = []
        while i<len(trips):
            if dist < trips[i][1]:
                dist = trips[i][1]
            
            while arr and dist >= arr[0][2]:
                passengers,start,end = heap.heappop(arr)
                curr-=passengers
            
            while i<len(trips) and dist==trips[i][1]:
                if curr + trips[i][0]>capacity:
                    return False
                curr+=trips[i][0]
                heap.heappush(arr,trips[i])
                i+=1
        return True
        


















        