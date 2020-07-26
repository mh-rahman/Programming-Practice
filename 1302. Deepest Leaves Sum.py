# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = 0
        currL, nextL = [], []
        if root:
            currL.append(root)
        i = 0
        while i < len(currL):
            curr = currL[i]
            res += curr.val
            if curr.left:
                nextL.append(curr.left)
            if curr.right:
                nextL.append(curr.right)
z            i += 1
            if i >= len(currL) and nextL:
                del(currL)
                currL, res, i = nextL, 0, 0
                nextL = []
        return res