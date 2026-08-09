class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        graph = [[] for _ in range(numCourses)]
        ingraph = [False]*numCourses
        indegree = [0]*numCourses
        for edges in prerequisites:
            start=edges[0]
            end = edges[1]
            graph[start].append(end)
            ingraph[start] = ingraph[end]=True
            indegree[end]+=1
        for i in range(len(indegree)):
            if ingraph[i] and indegree[i]==0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            ingraph[course] = False
            for i in graph[course]:
                indegree[i]-=1
                if indegree[i] == 0:
                    queue.append(i)
        
        for i in ingraph:
            if i:
                return False
        return True
