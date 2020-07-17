# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.curr = root
        self.st = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.curr:
            self.st.append(self.curr)
            self.curr = self.curr.left            
        nxt = self.st.pop()
        self.curr = nxt.right
        return nxt.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.curr != None or len(self.st) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()