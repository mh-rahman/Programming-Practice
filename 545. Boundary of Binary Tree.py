# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def setLeftBoundary(self, root, lboundary):
        if not root:
            return
        lboundary.append(root.val)
        if root.left:
            self.setLeftBoundary(root.left, lboundary)
        else:
            self.setLeftBoundary(root.right, lboundary)
            
    def setRightBoundary(self, root, rboundary):
        if not root:
            return
        if root.right:
            self.setRightBoundary(root.right, rboundary)
        else:
            self.setRightBoundary(root.left, rboundary)
        rboundary.append(root.val)
    
    
    def setLeaves(self, root, leaves):
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        if root.left:
            self.setLeaves(root.left, leaves)
        if root.right:
            self.setLeaves(root.right, leaves)
            
    
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        lboundary = []
        self.setLeftBoundary(root.left, lboundary)
        
        rboundary = []
        self.setRightBoundary(root.right, rboundary)
        
        leaves = []
        self.setLeaves(root, leaves)
        
        # print(lboundary)
        # print(rboundary)
        # print(leaves)
        
        return [root.val] + lboundary[:-1] + leaves + rboundary[1:]