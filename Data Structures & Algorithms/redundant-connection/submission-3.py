class DSU:
    def __init__(self):
        self.parent={}
        self.rank={}
    def find(self,node):
        v = node
        if v!=self.parent[v]:
            v=self.find(self.parent[v])
        self.parent[node] = v
        return v
    def union(self,u,v):
        ultu = self.find(u)
        ultv = self.find(v)
        if ultu!=ultv:
            if self.rank[ultu]>=self.rank[ultv]:
                self.parent[ultv] = ultu
                if self.rank[ultu]==self.rank[ultv]:
                    self.rank[ultu]+=1
            else:
                self.parent[ultu] = ultv
            return False
        return True
    def add(self,u,v):
        if u not in self.parent:
            self.parent[u] = u
            self.rank[u] = 0
        if v not in self.parent:
            self.parent[v] = v
            self.rank[v] = 0

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        curr = None
        for edge in edges:
            u = edge[0]
            v = edge[1]
            dsu.add(u,v)
            if dsu.union(u,v):
                curr = edge
        return curr

        