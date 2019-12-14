# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        db = {}
        def BFS(debth , r):
            if r == None:
                return
            if debth not in db:
                db[debth] = [r.val]
            else:
                db[debth] = db[debth] + [r.val]
            BFS(debth + 1, r.left)
            BFS(debth + 1, r.right)


        BFS(0, root)
        return db.values()