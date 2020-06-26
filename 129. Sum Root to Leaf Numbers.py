# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        if not root: return res
        Q = deque()
        Q.append([root,0])
        while Q:
            node,s = Q.popleft()
            if node.left and node.right:
                Q.append([node.left,s*10+node.val])
                Q.append([node.right,s*10+node.val])
            elif node.left:
                Q.append([node.left,s*10+node.val])
            elif node.right:
                Q.append([node.right,s*10+node.val])
            else:
                res+=(s*10+node.val)
                
        return res