# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traversal(root,minval):
            count=0
            if root:
                if root.val >= minval:
                    count=1
                    minval=root.val
                count+=traversal(root.left,minval)+traversal(root.right,minval)
                return count
            return 0
        return traversal(root,-float('inf'))
