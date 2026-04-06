# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root,val):
            if root==None:
                root=TreeNode(val)
            elif root.val<val:
                if root.right==None:
                    root.right=TreeNode(val)
                    return
                insert(root.right,val)
            elif root.val>val:
                if root.left==None:
                    root.left=TreeNode(val)
                    return
                insert(root.left,val)
        if root==None:
            root=TreeNode(val)
        else:
            insert(root,val)
        return root
        