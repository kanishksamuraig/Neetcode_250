# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(root1,root2):
            if (root1!=None and root2==None) or (root1==None and root2!=None):
                return False
            if root1!=None and root2!=None and (root1.val!=root2.val):
                return False
            if root1==None and root2==None:
                return True
            l=inorder(root1.left,root2.left)
            r=inorder(root1.right,root2.right)
            return l and r
        return inorder(p,q)
            

            