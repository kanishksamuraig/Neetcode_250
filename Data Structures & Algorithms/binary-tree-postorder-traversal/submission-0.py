# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        def postorder(root,lst):
            if root==None:
                return
            postorder(root.left,lst)
            postorder(root.right,lst)
            lst.append(root.val)
        postorder(root,lst)
        return lst
