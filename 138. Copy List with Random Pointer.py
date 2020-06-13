"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        nodeDict = {None:None}
        
        temp = head
        while temp:
            nodeDict[temp] = Node(temp.val)
            temp = temp.next
        
        
        
        temp = head
        while temp:
            nodeDict[temp].next = nodeDict[temp.next]
            nodeDict[temp].random = nodeDict[temp.random]
            temp = temp.next
        
        newHead = nodeDict[head]
        
        return newHead