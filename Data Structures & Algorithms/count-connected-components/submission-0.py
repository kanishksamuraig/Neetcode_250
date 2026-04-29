class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        seen=0
        def dfs(graph,node,visited):
            nonlocal seen
            visited[node]=True
            for neighbour in graph[node]:
                print(neighbour)
                if not visited[neighbour]:
                    dfs(graph,neighbour,visited)
            seen+=1
            
        visited=[False]*n
        count=0;
        while seen<n:
            smallunvisited=min([i for i in range(len(visited)) if not visited[i]])
            dfs(graph,smallunvisited,visited)
            count+=1
        return count

