# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy;
        curr1=l1;curr2=l2
        carry=0
        while curr1!=None and curr2!=None:
            curr.next=ListNode()
            tot=curr1.val+curr2.val+carry
            carry=tot//10
            curr.next.val=tot%10
            curr1=curr1.next
            curr2=curr2.next
            curr=curr.next
        while curr1!=None:
            curr.next=ListNode()
            tot=curr1.val+carry
            carry=tot//10
            curr.next.val=tot%10
            curr1=curr1.next
            curr=curr.next
        while curr2!=None:
            curr.next=ListNode()
            tot=curr2.val+carry
            carry=tot//10
            curr.next.val=tot%10
            curr2=curr2.next
            curr=curr.next
        if carry!=0:
            curr.next=ListNode()
            curr.next.val=carry
        return dummy.next
