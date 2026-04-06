# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        prev=ListNode(0);prev.next=list1
        curr1=prev;curr2=list2;next1=curr1.next

        while curr1.next!=None and curr2!=None:
            if curr1.next.val>=curr2.val:
                next2=curr2.next
                curr2.next=curr1.next
                curr1.next=curr2
                curr2=next2
                curr1=curr1.next
            else:
                curr1=curr1.next
                next1=next1.next
        if curr2:
            curr1.next=curr2
        return prev.next
