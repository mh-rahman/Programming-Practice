# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return '#'
            return inorder(root.left)+str(root.val)+inorder(root.right)
        
        def preorder(root):
            if not root:
                return '#'
            return str(root.val)+preorder(root.left)+preorder(root.right)
        
        inS, preS = inorder(s), preorder(s)
        inT, preT = inorder(t), preorder(t)
        
        return inT in inS and preT in preS
            

    
    
    
    def TraverseisSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        Q = deque([])
        if s:
            Q.append(s)
            
        while Q:
            s = Q.popleft()
            if s.val == t.val and not (bool(s.left) ^ bool(t.left)) and not (bool(s.right) ^ bool(t.right)):
                break
            if s.left:
                Q.append(s.left)
            if s.right:
                Q.append(s.right)
        del(Q)
        
        Qs, Qt = deque([]), deque([])
        if s:
            Qs.append(s)
        if t:
            Qt.append(t)
            
        if len(Qs) != len(Qt) or s.val != t.val:
            return False
        
        # while len(Qs) == len(Qt) and len(Qs) > 0:
        while Qs and Qt:
            s,t = Qs.popleft(), Qt.popleft()
            if s.val != t.val:
                return False
            if bool(s.left) ^ bool(t.left):
                return False
            elif s.left and t.left:
                Qs.append(s.left)
                Qt.append(t.left)
                
            if bool(s.right) ^ bool(t.right):
                return False
            elif s.right and t.right:
                Qs.append(s.right)
                Qt.append(t.right)
                            
            
        if len(Qs) == len(Qt) and len(Qs) == 0:
            return True
        return False
        