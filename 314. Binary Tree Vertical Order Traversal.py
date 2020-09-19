# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    count = 0
    
    def bfs(self, root, currLevel, depth, levels):
        if not root:
            return
        if currLevel not in levels:
            levels[currLevel] = []
        self.count += 1
        levels[currLevel].append([root.val, depth, self.count])
        self.bfs(root.left, currLevel-1, depth+1, levels)
        self.bfs(root.right, currLevel+1, depth+1, levels)
        return
    
    
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        self.count = 0
        levels = {}
        self.bfs(root, 0, 0, levels)
        # print(levels)
        res = []
        for l in sorted(levels):
            # print(levels[l])
            levels[l].sort(key = lambda x: (x[1], x[2]))
            res.append([x[0] for x in levels[l]])
        return res