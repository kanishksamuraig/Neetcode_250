class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def neighboursfunc(node):
            r,c=node
            lst=[]
            for dr,dc in [(-1,0),(0,-1),(0,1),(1,0)]:
                nr=dr+r
                nc=dc+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[r][c]<grid[nr][nc]<float('inf'):
                    lst.append((nr,nc))
            return lst
        
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    queue.append((i,j))
        
        while queue:
            node=queue.pop()
            neighbours=neighboursfunc(node)
            for neighbour in neighbours:
                if grid[neighbour[0]][neighbour[1]]>(grid[node[0]][node[1]]+1):
                    grid[neighbour[0]][neighbour[1]]=grid[node[0]][node[1]]+1
                    queue.append(neighbour)
        
