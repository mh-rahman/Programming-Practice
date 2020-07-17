"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # print([n.val for n in node.neighbors])
        Q = deque()
        res, lookup = None, {}
        if node:
            res = Node(node.val)
            lookup[node.val] = res
            Q.append(node)
        
        while Q:
            old = Q.popleft()
            new = lookup[old.val]
            if old.neighbors:
                new.neighbors = []
            for n in old.neighbors:
                if n.val not in lookup:
                    temp = Node(n.val)
                    lookup[n.val] = temp
                    Q.append(n)
                new.neighbors.append(lookup[abs(n.val)])

        
        return res