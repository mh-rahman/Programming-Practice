# from queue import Queue
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        Q = collections.deque()
        Q.append((root,0))

        while Q:
            node,level = Q.popleft()
            if Q and level == Q[0][1]:
                node.next = Q[0][0]
            else:
                node.next = None
            if node.left:
                Q.append((node.left,level+1))
            if node.right:
                Q.append((node.right,level+1))
        
        return root
                
                
                
                