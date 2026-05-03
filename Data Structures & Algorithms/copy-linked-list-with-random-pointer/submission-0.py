"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hash={}
        hash[head]=Node(head.val)
        curr=head
        while curr:
            if curr.random and curr.random not in hash:
                hash[curr.random]=Node(curr.random.val)
            if curr.next and curr.next not in hash:
                hash[curr.next]=Node(curr.next.val)
            hash[curr].random=None if not curr.random else hash[curr.random]
            hash[curr].next=None if not curr.next else hash[curr.next]
            curr=curr.next
        return hash[head]