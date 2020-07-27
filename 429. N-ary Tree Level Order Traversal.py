"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res,curr,nxt, i = [], [], [], 0
        if root:
            curr.append(root)
            res.append([])
        
        while i < len(curr):
            currNode = curr[i]
            res[-1].append(currNode.val)
            for c in currNode.children:
                nxt.append(c)
            i += 1
            if i == len(curr) and nxt:
                del(curr)
                curr, nxt = nxt, []
                i = 0
                res.append([])
                
        return res