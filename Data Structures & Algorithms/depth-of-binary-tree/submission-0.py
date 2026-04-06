# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        i=0;max1=0
        def inorder(root,i):
            if root==None:
                return i
            return max(inorder(root.left,i+1),inorder(root.right,i+1))
            
            
            
            
        return inorder(root,0)
        