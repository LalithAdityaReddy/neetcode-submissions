# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def func(root,left=float('-inf'),right=float('inf')):
            if not root:
                return TreeNode(val)
            if val>left and val<root.val:
                root.left=func(root.left,left,root.val)
            if val<right and val>root.val:
                root.right=func(root.right,root.val,right)
            return root
        return func(root)