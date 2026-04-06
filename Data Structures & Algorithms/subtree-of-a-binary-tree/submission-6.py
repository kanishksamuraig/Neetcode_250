# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(root1,root2):
            if root1==None and root2==None:
                return True
            elif root1==None or root2==None or root1.val!=root2.val:
                return False
            return isSametree(root1.left,root2.left) and isSametree(root1.right,root2.right)
        def dfs(root1,root2):
            if not root1:
                return False
            if root1.val==root2.val and isSametree(root1,root2):
                return True
                
            return dfs(root1.left,root2) or dfs(root1.right,root2)
            
        return dfs(root,subRoot)

        """
        queue=deque()
        queue.append(root)
        root2=subRoot
        while queue:
            node=queue.popleft()
            if node: 
                if node.val==root2.val:
                    if isSametree(node,root2):
                        return True
                    root2=subRoot
                queue.append(node.left)
                queue.append(node.right)
        return False
        """
    