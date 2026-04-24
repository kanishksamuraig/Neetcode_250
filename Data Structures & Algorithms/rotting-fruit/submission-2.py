class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def neighboursfunc(node):
            r,c=node;lst=[]
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr=dr+r
                nc=dc+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                    lst.append((nr,nc))
            return lst

        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
        min1=0
        while queue:
            n=len(queue)
            flag=False
            for i in range(n):
                node=queue.popleft()
                neighbours=neighboursfunc(node)
                for neighbour in neighbours:
                    if grid[neighbour[0]][neighbour[1]]==1:
                        grid[neighbour[0]][neighbour[1]]=2
                        queue.append(neighbour)
                        flag=True
            if flag:
                min1+=1
        for row in grid:
            if 1 in row:
                return -1
        return min1
