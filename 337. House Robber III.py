# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def robHelper(root):
            if root == None:
                return (0,0)

            lrobbed,lnot_robbed = robHelper(root.left)
            rrobbed,rnot_robbed = robHelper(root.right)

            robbed = root.val + lnot_robbed + rnot_robbed
            not_robbed = max(lrobbed,lnot_robbed)+max(rrobbed,rnot_robbed)

            return (robbed,not_robbed)
        
        (robbed,not_robbed) = robHelper(root)
        
        return max(robbed,not_robbed)
    

        