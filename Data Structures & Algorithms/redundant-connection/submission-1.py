class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph={}
        def cycle(node,parent,visited):
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if cycle(neighbour,node,visited):
                        return True
                elif neighbour!=parent:
                    return True
            return False
        curr = None
        for edge in edges:
            src = edge[0]
            dest = edge[1]
            lst1 = graph.get(src,[]) + [dest]
            lst2 = graph.get(dest,[]) + [src]
            graph[src] = lst1
            graph[dest] = lst2
            visited = dict(zip(list(graph.keys()),[False]*len(graph)))
            if cycle(dest,None,visited):
                curr = edge
                graph[src].pop()
                graph[dest].pop()
        return curr