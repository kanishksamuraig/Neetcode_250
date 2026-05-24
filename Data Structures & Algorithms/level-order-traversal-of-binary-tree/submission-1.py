# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        if root==None:
            return []
        queue.append((root,0))
        i=0
        res=[];lst=[]
        while queue:
            node,level=queue.popleft()
            if i==level:
                lst.append(node.val)
            else:
                i+=1
                res.append(lst)
                lst=[]
                lst.append(node.val)
            if node.left!=None:
                queue.append((node.left,level+1))
            if node.right!=None:
                queue.append((node.right,level+1))
        if (res and lst!=res[-1]) or lst not in res:
            res.append(lst)
        return res




