# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def getSum(root):
            s, children = 0, [c for c in [root.left,root.right] if c]
            for child in children:
                for n in [c for c in [child.left,child.right] if c]:
                    s+=n.val
            return s
        
        st, res = [], 0
        if root:
            st.append(root)
        while st:
            root = st.pop()
            if root.val%2 == 0:
                res += getSum(root)
            if root.left:
                st.append(root.left)
            if root.right:
                st.append(root.right)
                
        return res