# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root==None:
                return 0
            return 1+max(height(root.left),height(root.right))
        res=[0]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            res[0]=max(res[0],height(root.left)+height(root.right))
            inorder(root.right)
        inorder(root)
        return res[0]
        