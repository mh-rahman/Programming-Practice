# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            if root == None:
                return 0,0
            lh,lpath = helper(root.left) 
            rh,rpath = helper(root.right)

            return max(lh,rh)+1, max(lh+rh,lpath,rpath)
        
        depth,path = helper(root)
        return path