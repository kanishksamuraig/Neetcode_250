class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for edges in prerequisites:
            start=edges[0]
            end = edges[1]
            graph[end].append(start)
            indegree[start]+=1
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            for i in graph[course]:
                indegree[i]-=1
                if indegree[i] == 0:
                    queue.append(i)
        
        for i in indegree:
            if i!=0:
                return False
        return True
