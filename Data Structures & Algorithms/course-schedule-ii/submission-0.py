class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for edges in prerequisites:
            a = edges[0]
            b = edges[1]
            graph[b].append(a)
            indegree[a]+=1
        
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        lst = []
        count = 0
        while queue:
            count+=1
            node = queue.popleft()
            lst.append(node)
            for neighbour in graph[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        if count==numCourses:
            return lst
        return []


        