# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        # head = TreeNode(0,root)
        def helper(root,L,R):
            
            while root and not (L <= root.val <= R):
                
                while root and root.val < L:
                    root = root.right

                while root and root.val > R:
                    root = root.left
                
            if root:
                root.left = helper(root.left,L,R)
                root.right = helper(root.right,L,R)
            
            return root
        
        root = helper(root,L,R)
        return root