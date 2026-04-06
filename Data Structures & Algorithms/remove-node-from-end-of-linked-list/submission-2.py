# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x=0
        prev=ListNode()
        node=head
        prev.next=head
        if node.next==None:
            return None
        while node!=None:
            x+=1
            node=node.next
        x-=n
        node=prev
        for i in range(0,x):
            node=node.next
        node.next=node.next.next
        return prev.next
        
