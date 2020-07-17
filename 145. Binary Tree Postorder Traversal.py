# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ##Keep going to right and keep adding visited to res, stack
        ##Once reached None, go back i.e. pop stack and root = left
        
        st, res = [], []
        while st or root:
            if root:
                st.append(root)
                res.append(root.val)
                root = root.right
            else:
                root = st.pop().left
                
        return res[::-1]