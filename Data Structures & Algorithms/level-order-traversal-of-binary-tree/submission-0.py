# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        q=deque()
        q.append((root,0))
        while q:
            l=len(q)
            t=[]
            for i in range(l):
                node,hd=q.popleft()
                t.append(node.val)
                if node.left:
                    q.append((node.left,hd+1))
                if node.right:
                    q.append((node.right,hd+1))
            ans.append(t)
        return ans
