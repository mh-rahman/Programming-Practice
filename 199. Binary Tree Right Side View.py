# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res,res2,Q = {},[],deque([])
        
        if root:
            Q.append([root,0])
            
        while Q:
            curr,lvl = Q.popleft()
            res[lvl] = curr.val
            if curr.left:
                Q.append([curr.left,lvl+1])
            if curr.right:
                Q.append([curr.right,lvl+1])
                
        for i in range(len(res)):
            res2.append(res[i])
            
        return res2