class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def neighbours(node):
            r,c=node
            for dr,dc in [(0,-1),(-1,0),(0,1),(1,0)]:
                nr=dr+r
                nc=dc+c
                if 0<= nr < len(grid) and 0 <= nc <len(grid[0]) and grid[nr][nc]==1:
                    yield (nr,nc)
        d={0:4, 1:3, 2:2, 3:1, 4:0}
        hash=set()
        start=(-1,-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    start=(i,j)
        queue=deque()
        queue.append(start)
        perimeter=0
        while queue:
            node=queue.popleft()
            hash.add(node)
            perimeter+=d[len(list(neighbours(node)))]
            for neighbour in neighbours(node):
                if neighbour not in hash:
                    hash.add(neighbour)
                    queue.append(neighbour)
        print(hash)
        return perimeter