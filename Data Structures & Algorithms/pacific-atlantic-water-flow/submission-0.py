class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(node,hash,flags):
            hash.add(node)
            r,c=node
            if r==0 or c==0:
                flags[0]=True
            if r==len(heights)-1 or c==len(heights[0])-1:
                flags[1]=True
            if flags[1] and flags[0]:
                return
            neighbours=neighboursfunc(node)
            for neighbour in neighbours:
                if neighbour not in hash:
                    dfs(neighbour,hash,flags)
        def neighboursfunc(node):
            r,c=node
            lst=[]
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr=dr+r
                nc=dc+c
                if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and heights[r][c]>=heights[nr][nc]:
                    lst.append((nr,nc))
            return lst
        res=[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                flags=[False,False]
                hash=set()
                dfs((i,j),hash,flags)
                if flags[1] and flags[0]:
                    res.append([i,j])
        return res
