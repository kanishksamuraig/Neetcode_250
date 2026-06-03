class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        def bfs(start: tuple[int]):
            queue=deque()
            queue.append(start)
            grid[start[0]][start[1]]="0"
            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc=dr+r,dc+c
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1":
                        grid[nr][nc]="0"
                        queue.append((nr,nc))
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    bfs((i,j))
        return count