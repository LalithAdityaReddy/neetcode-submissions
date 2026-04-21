# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        curr=dummy
        while l1!=None or l2!=None or carry!=0:
            if l1:
                x=l1.val
            else:
                x=0
            if l2:
                y=l2.val
            else:
                y=0
            sum=x+y+carry
            curr.next=ListNode(sum%10)
            curr=curr.next
            carry=sum//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next