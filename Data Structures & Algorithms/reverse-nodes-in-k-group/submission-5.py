# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total=0
        curr=head
        while curr:
            total+=1
            curr=curr.next
        curr=head
        prev=None
        if total<k:
            return head
        cnt=0
        while cnt<k:
            cnt+=1
            nextOne=curr.next
            curr.next=prev
            prev=curr
            curr=nextOne
        head.next=self.reverseKGroup(curr,k)
        return prev

                     

