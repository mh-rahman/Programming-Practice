# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        ## As long as they are same, they are part of the left subtree
        ## The next element in the inorder will be the parent node
        ## Next elements until the parent node from..
        ## ..the postorder list will form the right node
        
        ## last node in postorder will always be root
        
        def getTree(inorder, postorder, st_i, end_i, st_p, end_p):
            if end_i < st_i:
                return None
            if end_i == st_i:
                return TreeNode(inorder[st_i])
            root_val = postorder[end_p]
            ind = inorder.index(root_val, st_i, end_i+1)
            left = getTree(inorder, postorder, st_i, ind-1, st_p, st_p + (ind-st_i-1))
            right = getTree(inorder, postorder, ind+1, end_i, st_p + (ind-st_i), end_p-1)
            return TreeNode(root_val, left, right)
        
        return getTree(inorder, postorder, 0, len(inorder)-1, 0, len(inorder)-1)
            