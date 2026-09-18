from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        parent = {}
        rank = defaultdict(int)
        
        def find(var1):
            v = var1
            if v != parent[v]:
                v = find(parent[v])
            parent[var1] = v
            return v
        def union(var1, var2):
            ultu = find(var1)
            ultv = find(var2)
            if ultu!=ultv:
                if rank[ultu] >= rank[ultv]:
                    parent[ultv] = ultu
                    if rank[ultu] == rank[ultv]:
                        rank[ultu] += 1
                else:
                    parent[ultu] = ultv
        for index, (var1, var2) in enumerate(equations):
            graph[var1].append([var2,values[index]])
            graph[var2].append([var1, 1/values[index]])
            if var1 not in parent:
                parent[var1] = var1
                rank[var1] = 0
            if var2 not in parent:
                parent[var2] = var2
                rank[var2] = 0
            
            union(var1, var2)
        
        def dfs(var1,value,visited,var2):
            visited[var1] = True
            if var1 == var2:
                return value
            
            for neighbour, val in graph[var1]:
                if not visited[neighbour]:
                    newval = dfs(neighbour, val * value, visited, var2)
                    if newval!=1:
                        return newval
            return 1
        values = [] 
        for query in queries:
            a = query[0]
            b = query[1]
            if (a not in graph) or (b not in graph) or find(a)!=find(b):
                values.append(float(-1))
            else:
                values.append(dfs(a,1,defaultdict(bool),b))
        return values