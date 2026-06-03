class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def neighbours(node: tuple[int]):
            lst=[]
            r,c=node;val=grid[r][c]
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr=dr+r
                nc=dc+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]>val+1:
                    lst.append((nr,nc))
            return lst

        def bfs(start: tuple[int]):
            queue=deque()
            queue.append(start)
            while queue:
                node=queue.popleft()
                val=grid[node[0]][node[1]]
                for neighbour in neighbours(node):
                    if grid[neighbour[0]][neighbour[1]]>val+1:
                        grid[neighbour[0]][neighbour[1]]=val+1
                        queue.append(neighbour)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    bfs((i,j))