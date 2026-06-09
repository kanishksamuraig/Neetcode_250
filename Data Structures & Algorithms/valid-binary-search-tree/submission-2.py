# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            if self.isValid(root.left,root.val,True) and self.isValid(root.right,root.val,False):
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            return False
        return True
    def isValid(self,root,val,isleft):
        if root:
            if (root.val<=val and not isleft) or (root.val>=val and isleft):
                return False
            return self.isValid(root.left,val,isleft) and self.isValid(root.right,val,isleft)
        return True

                