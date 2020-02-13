class Codec:
    def serialize(self, root):
        # take care of base cases
        # if a node is empty, add 'x' to string
        # you can set 'x' to any mark as you want
        if not root: return 'x'
        # preoder(Root->left->right)
        # ex,
        #     1
        #    / \
        #   2   3
        #      / \
        #     4   5 
        # 
        # return (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
        # if you look at the return statement close, it is actually very intuitive
        # for value 1, you have 2 as left child and 3 as right child
        # for value 2, you have 'x'(None) as left child and 'x'(None) as right child, so on.
        return root.val, self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        #######################INTUITION#########################
        # The initial data string will be something like below:#
        # (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))#
        # if you loop through string: 
        # 1                                 -> this is node value
        # (2, 'x', 'x')                     -> this is node left
        # (3, (4, 'x', 'x'), (5, 'x', 'x')) -> this is node right
        ########################################################
        # always take care of base case: if the node's value is 'x' then return None
        if data[0] == 'x': return None
        # create new treenode for node value
        node = TreeNode(data[0])
        # do the recursive to unpack string value
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        # return the new TreeNode that we just created
        return node