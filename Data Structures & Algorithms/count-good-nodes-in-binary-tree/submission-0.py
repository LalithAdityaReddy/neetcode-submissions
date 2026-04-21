# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt=0
        def helper(root,maxi):
            if not root:
                return 
            if root.val>=maxi:
                self.cnt+=1
            maxi=max(maxi,root.val)
            helper(root.left,maxi)
            helper(root.right,maxi)
            return
        helper(root,float('-inf'))
        return self.cnt