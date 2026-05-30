# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def inorder(root,p,q):
            if root:
                if p<=root.val<=q:
                    return root
                
                left=inorder(root.left,p,q)
                right=inorder(root.right,p,q)

                if left is not None:
                    return left
                else:
                    return right
        return inorder(root,min(p.val,q.val),max(p.val,q.val))