# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root,value):
            if root==None:
                return root
            elif root.val<value:
                root.right=delete(root.right,value)
            elif root.val>value:
                root.left=delete(root.left,value)
            else:
                if not root.left and not root.right:
                    root=None
                elif root.left and not root.right:
                    root=root.left
                elif root.right and not root.left:
                    root=root.right
                else:
                    temp=root
                    temp=temp.right
                    while temp.left!=None:
                        temp=temp.left
                    root.val=temp.val
                    val=temp.val
                    root.right=delete(root.right,val)
            return root
        root=delete(root,key)
        return root