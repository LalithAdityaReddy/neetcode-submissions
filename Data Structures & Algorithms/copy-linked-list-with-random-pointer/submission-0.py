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
        ptr=head
        while ptr:
            new_l=Node(ptr.val)
            new_l.next=ptr.next
            ptr.next=new_l
            ptr=new_l.next
        ptr=head
        while ptr:
            if ptr.random:
                ptr.next.random=ptr.random.next
            ptr=ptr.next.next
        new_head=head.next
        ptr=head
        while(ptr):
            k=ptr.next
            ptr.next=k.next
            if k.next:
                k.next=k.next.next
            ptr=ptr.next
        return new_head

        