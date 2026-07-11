class Solution:
    def reorganizeString(self, s: str) -> str:
        freq={}
        for i in s:
            freq[i] = 1 + freq.get(i,0)
        
        heap=[]
        for i in freq:
            heapq.heappush(heap,(-freq[i],i))
        queue = deque()
        time=0;res=""
        while heap or queue:
            if not heap:
                if queue and time < queue[0][2]:
                    time = queue[0][2]
            
            if heap:
                frequency,character = heapq.heappop(heap)
                frequency += 1
                time+=1
                if frequency!=0:
                    queue.append((frequency,character,time+1))
                if len(res)>0 and res[-1]==character:
                    return ""
                res+=character

            if queue and queue[0][2]<=time:
                frequency,character,t = queue.popleft()
                heapq.heappush(heap,(frequency,character))
        return res if len(res)==len(s) else ""

