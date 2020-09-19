"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        head = Node(0)
        curr = head
        st = []
        
        st.append(root)
            
        while st:
            n = st.pop()
            while n:
                st.append(n)
                temp = n
                n = n.left
                temp.left = None
                
            n = st.pop()
            
            if n.right:
                st.append(n.right)

            # add to list
            curr.right = n
            n.left = curr
            curr = n
            
            
            # print(n.val, end=", ")
            
        head = head.right
        curr.right = head
        head.left = curr
        
                    
        
        return head