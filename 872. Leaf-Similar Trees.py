# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not (root1 and root2):
            return False
        st1, st2, res1, res2 = [], [], [], []
        if root1:
            st1.append(root1)
        if root2:
            st2.append(root2)
        for st,res in [[st1,res1],[st2,res2]]:
            while st:
                n = st.pop()
                if not n.left and not n.right:
                    res.append(n.val)
                    continue
                if n.right:
                    st.append(n.right)
                if n.left:
                    st.append(n.left)
        
        if len(res1) != len(res2):
            return False
        for l1,l2 in zip(res1,res2):
            if l1 != l2:
                return False
        return True
            