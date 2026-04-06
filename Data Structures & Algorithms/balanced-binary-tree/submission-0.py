# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self,root):
        if root==None:
            return 0
        return 1+ max(self.depth(root.left),self.depth(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        lheight=self.depth(root.left)
        rheight=self.depth(root.right)
        diff=lheight-rheight
        if diff>1 or diff<-1:
            return False
        return True and self.isBalanced(root.left) and self.isBalanced(root.right)
        