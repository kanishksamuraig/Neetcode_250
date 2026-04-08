class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbours(node):
            r,c =node;l=[] 
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr=dr+r
                nc=dc+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1":
                    l.append((nr,nc))
            return l
        
        i=0;j=0;count=0
        hash=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in hash:
                    count+=1
                    queue=deque()
                    hash.add((i,j))
                    queue.append((i,j))
                    while queue:
                        node=queue.popleft()
                        neighbourlist=neighbours(node)
                        for neighbour in neighbourlist:
                            if neighbour not in hash:
                                hash.add(neighbour)
                                queue.append(neighbour)
                j+=1
            i+=1
        return count



            