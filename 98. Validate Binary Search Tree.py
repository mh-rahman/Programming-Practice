# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root,leftCheck,rightCheck):
            if not root:
                return True
            print(root.val,leftCheck,rightCheck)
            lrightCheck = min(root.val,rightCheck)
            rleftCheck = max(root.val,leftCheck)
            # print(root.val,leftCheck,rightCheck,lrightCheck,rleftCheck)
            left,right = root.left, root.right
            if not left and not right:
                    return True
            elif not right:
                return leftCheck < left.val < lrightCheck and helper(left,leftCheck,lrightCheck)
            elif not left:
                return rleftCheck < right.val < rightCheck and helper(right,rleftCheck,rightCheck)
            else:
                return leftCheck < left.val < lrightCheck and rleftCheck < right.val < rightCheck and helper(left,leftCheck,lrightCheck) and helper(right,rleftCheck,rightCheck)
        
        return helper(root,-math.inf,math.inf)