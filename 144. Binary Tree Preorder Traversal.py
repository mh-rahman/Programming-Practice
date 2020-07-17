# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ##Stack - add right and then left
        res = []
        st = []
        if root:
            st.append(root)
        while st:
            curr = st.pop()
            res.append(curr.val)
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
        return res