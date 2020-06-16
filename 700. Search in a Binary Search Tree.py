# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root:
#             return root
        
        while root != None:
            if val == root.val:
                return root
            if val > root.val:
                root = root.right
            else:
                root = root.left

        return root