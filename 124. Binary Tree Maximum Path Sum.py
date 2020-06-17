# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def constructSumTree(node):
            left,right = None,None
            lsum = rsum = 0
            maxval = -math.inf
            val = node.val
            if node.left:
                left,lmaxval = constructSumTree(node.left)
                lsum = max(left.lsum+node.left.val,left.rsum+node.left.val,0)
                val = max(val,val+lsum)
                maxval = max(maxval,lmaxval)
            if node.right:
                right,rmaxval = constructSumTree(node.right)
                rsum = max(right.lsum+node.right.val,right.rsum+node.right.val,0)
                val = max(val,val+rsum)
                maxval = max(maxval,rmaxval)
            maxval = max(maxval,val)            
            return snode(val,left,right,lsum,rsum),maxval
            
        _,maxval = constructSumTree(root)
        return maxval
         
            
        
class snode:
    def __init__(self,val,left,right,lsum,rsum):
        self.val = val #max sum at this node - will always include node
        self.left = left
        self.right = right
        self.lsum = lsum
        self.rsum = rsum
