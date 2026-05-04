# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        left=dummy
        right=dummy
        for i in range(0,r+1):
            if i<l-1:
                left=left.next
            right=right.next
        curr=left.next;prev=right

        while curr!=right:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        left.next=prev
        return dummy.next