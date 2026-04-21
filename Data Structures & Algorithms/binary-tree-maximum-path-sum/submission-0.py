# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float('-inf')
        def func(root):
            if not root:
                return 0
            left_sum=max(0,func(root.left))
            right_sum=max(0,func(root.right))
            self.ans=max(self.ans,left_sum+right_sum+root.val)
            return root.val+max(left_sum,right_sum)
        func(root)
        return self.ans



