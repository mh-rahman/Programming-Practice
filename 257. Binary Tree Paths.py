# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(root,const):
            const.append(str(root.val))
            if not root.left and not root.right:
                res.append('->'.join(const))
                const.pop()
                return

            if root.left:
                helper(root.left,const)
            if root.right:
                helper(root.right,const)
            const.pop()
            return
        
        if not root:
            return []
        res = []
        helper(root,[])
        return res

            
            
            
            
            
            
            
            
            