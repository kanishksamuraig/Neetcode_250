"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None

        hashmap={}
        start=Node(0,None)
        
        hashmap[node.val]=start
        visited=set()
        queue=deque()
        queue2=deque()
        queue.append(node)
        queue2.append(start)
        while queue and queue2:
            node=queue.popleft()
            node2=queue2.popleft()
            if node.val not in visited:
                visited.add(node.val)
                node2.val=node.val
                for neighbour in node.neighbors:
                    if neighbour.val not in hashmap:
                        hashmap[neighbour.val]=Node()
                    node2.neighbors.append(hashmap[neighbour.val])
                    queue.append(neighbour)
                    queue2.append(hashmap[neighbour.val])
        return start

