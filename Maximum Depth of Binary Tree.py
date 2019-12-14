# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            # empty node or empty tree
            return 0
        
        if root is not None and root.left is None and root.right is None:
            # leaf node
            return 1
        
        else:
            # non-leaf node
            return max( self.maxDepth(root.left), self.maxDepth(root.right) ) + 1
