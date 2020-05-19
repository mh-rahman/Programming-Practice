# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def getInfo(node):
            if node:
                return node.val, node.left, node.right
            else:
                return 0,None,None
            
        if not (t1 or t2):
            return None
        
        val1, left1, right1 = getInfo(t1)
        val2, left2, right2 = getInfo(t2)
        
        # print(val1,val2)
        
        if left1 or left2:
            left = self.mergeTrees(left1,left2)
        else:
            left = None
        
        if right1 or right2:
            right = self.mergeTrees(right1,right2)
        else:
            right = None
        
        
        return TreeNode(val1+val2,left,right)