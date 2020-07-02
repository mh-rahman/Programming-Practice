# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def helper(st,end,nums):
            if st > end:
                return None
            val = nums[st]
            root = TreeNode(val)
            i = st+1
            while i < end+1:
                if nums[i] > val:
                    break
                i+=1
                
            root.left = helper(st+1,i-1,nums)
            root.right = helper(i,end,nums)
            return root

        root = helper(0,len(preorder)-1,preorder)
        return root
        
        
    def abstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        left = []
        root_val = preorder[0]
        root = TreeNode(root_val)
        i = 1
        while i < len(preorder):
            n = preorder[i]
            if n > root_val:
                break
            left.append(n)
            i+=1
            
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(preorder[i:])
        return root