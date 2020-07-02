# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,prev_level = [],0
        Q = deque()
        Q.append([root,1])
        while Q:
            curr,level = Q.popleft()
            if level > prev_level:
                res.append([])
            res[-1].append(curr.val)
            prev_level = level
            if curr.left:
                Q.append([curr.left,level+1])
            if curr.right:
                Q.append([curr.right,level+1])
                
        # print(res[::-1])
        
        return res[::-1]