class dsu:
    def __init__(self,size):
        self.rank = [0]*size
        self.parent = [x for x in range(size)]
        self.size = size
    #path compression
    def find(self,value):
        u = value
        if u != self.parent[u]:
            u = self.find(self.parent[u])
            self.parent[value] = u
        return u
    def union(self,u,v):
        ultu = self.find(u)
        ultv = self.find(v)
        if self.rank[ultu]>=self.rank[ultv]:
            if self.rank[ultu]==self.rank[ultv]:
                self.rank[ultu]+=1
            self.parent[ultv] = ultu
        else:
            self.parent[ultu] = ultv
    def noofcomponents(self):
        count = 0
        for i in range(self.size):
            if self.parent[i]==i:
                count+=1
        return count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = dsu(n)
        for edge in edges:
            graph.union(*edge)
        return graph.noofcomponents()

        