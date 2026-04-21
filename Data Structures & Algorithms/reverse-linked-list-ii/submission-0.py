# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cnt=0
        curr=head
        while curr:
            cnt+=1
            curr=curr.next
        it=0
        def rev(head,k):
            curr=head
            prev=None
            cnt=0
            while cnt<k:
                nextone=curr.next
                curr.next=prev
                prev=curr
                curr=nextone
                cnt+=1
            return prev,curr
        curr=head
        prev=None
        while curr and it<left-1:
            prev=curr
            curr=curr.next
            it+=1
        newhead,newcurr=rev(curr,right-left+1)
        if prev:
            prev.next=newhead
        else:
            head=newhead
        curr.next=newcurr
        return head