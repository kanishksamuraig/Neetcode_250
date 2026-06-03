class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def neighbours(node: tuple[int]):
            lst=[]
            r,c=node
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr=dr+r
                nc=dc+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1":
                    lst.append((nr,nc))
            return lst
        def bfs(start: tuple[int]):
            queue=deque()
            queue.append(start)
            grid[start[0]][start[1]]="0"
            while queue:
                node = queue.popleft()
                for neighbour in neighbours(node):
                    grid[neighbour[0]][neighbour[1]]="0"
                    queue.append(neighbour)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    bfs((i,j))
        return count