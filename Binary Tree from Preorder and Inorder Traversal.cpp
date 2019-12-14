/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int index;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        index = 0;
        return buildPreorder(preorder, inorder, 0, inorder.size()-1);
    }
    
    TreeNode* buildPreorder(vector<int>& preorder, vector<int>& inorder, int l, int r)
    {
        if(r < l) return nullptr;
        TreeNode* root = new TreeNode(preorder[index++]);
        int pos = findIndex(inorder, root->val, l, r);
        root->left = buildPreorder(preorder, inorder, l, pos-1);
        root->right = buildPreorder(preorder, inorder, pos+1, r);
        return root;
    }
    
    int findIndex(vector<int>& inorder, int val, int l, int r)
    {
        for(int i=l; i<=r; i++)
            if(inorder[i] == val)
                return i;
        return -1;
    }
};