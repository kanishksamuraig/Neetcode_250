# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start=head
        next=start.next
        end=head
        while end.next!=None:
            end=end.next
        while next!=None and next.next!=None:
            start.next=end
            end.next=next
            temp=next
            while temp.next!=end:
                temp=temp.next
            end=temp
            end.next=None
            start=next
            next=next.next
        


        