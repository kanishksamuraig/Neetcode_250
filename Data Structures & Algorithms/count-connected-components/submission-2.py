class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist=[[] for _ in range(n)]
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        visited=[False]*n
        def dfs(node):
            visited[node]=True
            for neighbour in adjlist[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
        count=0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count+=1
        return count

            