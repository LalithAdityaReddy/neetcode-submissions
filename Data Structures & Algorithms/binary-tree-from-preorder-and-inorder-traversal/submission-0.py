# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx=0
        def find(inorder,root_val,l,r):
            for i in range(l,r+1):
                if(inorder[i]==root_val):
                    return i
            return -1
        def helper(inorder,idx,l,r):
            if l>r:
                return None
            node=TreeNode(preorder[self.idx])
            index=find(inorder,node.val,l,r)
            self.idx+=1
            node.left=helper(inorder,idx,l,index-1)
            node.right=helper(inorder,idx,index+1,r)
            return node
        return helper(inorder,0,0,len(inorder)-1)