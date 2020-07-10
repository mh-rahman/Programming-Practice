"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        def unwrap(head):
            res1 = []
            while head:
                val,nxt,child = head.val,head.next,head.child
                res1.append([val])
                if child:
                    res1.append(unwrap(child))
                head = nxt
            
            res = []
            for lst in res1:
                for n in lst:
                    res.append(n)
            
            return res
        
        if not head:
            return head
        
        res = unwrap(head)
        # print(res)
        head = Node(0,None,None,None)
        prev = head
        for n in res:
            curr = Node(n,None,None,None)
            prev.next = curr
            curr.prev = prev
            prev = curr
            
        head = head.next
        head.prev = None
        
        return head
        
        
        
        
        
        
        
        
        
        
        
        