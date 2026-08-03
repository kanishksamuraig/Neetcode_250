class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #perform bfs or dfs on the borders of pacific and atlantic
        #instead of using dfs for each and every node use dfs on the edge of the matrix
        pacific=set()
        atlantic=set()
        def dfs(start,hash):
            hash.add(start)
            r,c = start
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and heights[r][c]<=heights[nr][nc] and (nr,nc) not in hash:
                    hash.add((nr,nc))
                    dfs((nr,nc),hash)
        
        for i in range(len(heights[0])):
            dfs((0,i),pacific)
            dfs((len(heights)-1,i),atlantic)
        
        for i in range(len(heights)):
            dfs((i,0),pacific)
            dfs((i,len(heights[0])-1),atlantic)
        return list(pacific & atlantic)

