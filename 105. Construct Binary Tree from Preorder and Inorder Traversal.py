# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(preorder,inorder,inorder_st,inorder_end,pre_ind):
            
            if not (0 <= inorder_st < len(preorder) and 0 <= inorder_end < len(preorder) and 0 <= pre_ind < len(preorder)) or inorder_st > inorder_end:
                return None
            
            # print(inorder_st,inorder_end,pre_ind, preorder[pre_ind])
            
            if inorder_st == inorder_end:
                return TreeNode(preorder[pre_ind])
            
            root = TreeNode(preorder[pre_ind])
            ind = inorder.index(preorder[pre_ind])
            left_len = ind - inorder_st
            root.left = helper(preorder,inorder,inorder_st,ind-1,pre_ind+1)
            root.right = helper(preorder,inorder,ind+1,inorder_end,left_len+pre_ind+1)
            
            return root

            
        return helper(preorder,inorder,0,len(preorder)-1,0) if preorder else None