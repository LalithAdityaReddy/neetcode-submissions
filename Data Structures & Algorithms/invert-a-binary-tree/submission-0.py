# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def func(root):
            if not root:
                return
            if root.left:
                left=root.left
            else:
                left=None
            if (root.right):
                right=root.right
            else:
                right=None
            root.right=func(left)
            root.left=func(right)
            return root
        return func(root)
