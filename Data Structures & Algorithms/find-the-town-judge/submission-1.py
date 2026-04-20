class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        outdegree=[False for _ in range(n)]
        for edge in trust:
            graph[edge[0]-1].append(edge[1]-1)
            outdegree[edge[0]-1]=True
        
        for index,bol in enumerate(outdegree):
            if not bol:
                for i in range(len(graph)):
                    if i!=index and index not in graph[i]:
                        return -1
                return index+1
        return -1
        