# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head;slow=head
        if fast==None:
            return False
        while fast.next!=None and fast.next.next!=None:
            
            fast=fast.next.next;slow=slow.next
            if fast==slow:
                return True
            elif fast==None:
                return False
        return False