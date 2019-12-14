# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        stack = [root]
        result = []
        i = 1
        while stack:
            level = []
            next_level = []
            while stack:
                node = stack.pop()
                level.append(node.val)
                if i%2 == 1:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            i += 1
            stack = stack + next_level
            result.append(level)
        return result