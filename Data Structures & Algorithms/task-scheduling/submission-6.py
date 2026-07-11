class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap=[]
        freq={}
        for i in tasks:
            freq[i] = 1 + freq.get(i,0)
        for i in freq:
            heapq.heappush(heap,-freq[i]) #if we use negative numbers then min heap acts like a max heap
        
        queue = deque()
        time=0
        while heap or queue:
            if not heap:
                time = queue[0][1]
            else:
                val = heapq.heappop(heap) + 1
                time+=1
                if val!=0:
                    queue.append((val,time+n))
            
            if queue and time>=queue[0][1]:
                heapq.heappush(heap,queue.popleft()[0])
        return time

        
