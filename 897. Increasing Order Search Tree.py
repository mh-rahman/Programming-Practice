# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        st, res = [], TreeNode()
        result = res
        if root:
            st.append(root)
        while st:
            node = st[-1]
            while node.left:
                temp = node.left
                st.append(temp)
                node.left = None
                node = temp
            node = st.pop()
            if node.right:
                st.append(node.right)
            res.right = node
            res = res.right
            res.left = None
        return result.right
            