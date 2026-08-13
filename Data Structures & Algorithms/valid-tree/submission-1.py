class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = [0]*n
        graph = [[] for _ in range(n)]
        def dfs(node,visited,parent):
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if dfs(neighbour,visited,node):
                        return True
                elif parent!=neighbour:
                    return True
            return False
        for edge in edges:
            start=edge[0];dest=edge[1]
            if edge[0]>edge[1]:
                start = edge[1];dest = edge[0]
            if dsu[start]<dsu[dest]:
                dsu[dest]+=1
            else:
                dsu[start]+=1
            graph[start].append(dest)
            graph[dest].append(start)
        maxi=0;maxindex = 0
        for index, i in enumerate(dsu):
            if i>maxi:
                maxi = i
                maxindex = index
        visited = [False]*n
        flag =not dfs(maxindex,visited,-1)
        for i in visited:
            if not i:
                return False
        return flag
        

