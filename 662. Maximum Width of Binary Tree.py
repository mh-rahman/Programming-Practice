# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        ##Assign numbers to nodes and its children
        ##k = 2k+1, 2(k+1)
        ##maxWidth = diff between first and last entry of a level
        
        currQ = deque()
        nextQ = deque()
        maxW = 0
        if root:
            root.val = 0
            maxW = 1
            currQ.append(root)
        while currQ:
            node = currQ.popleft()
            k = node.val
            if node.left:
                node.left.val = 2*k + 1
                nextQ.append(node.left)
            if node.right:
                node.right.val = 2*k + 2
                nextQ.append(node.right)
                
            if not currQ and not nextQ:
                break
            if not currQ:
                currQ = nextQ
                rightval = nextQ[-1].val
                leftval = nextQ[0].val
                currW =  rightval - leftval + 1
                nextQ = deque()
                maxW = max(maxW,currW)
        
        return maxW
    
    
    def notWorkingwidthOfBinaryTree(self, root: TreeNode) -> int:
        
        currLevelNodes = []
        nextLevelNodes = []
        i,currLevel,currWidth,maxWidth,noneWidth = 0,1,0,0,0
        if root:
            # currLevelNodes.append([root,1])
            currLevelNodes.append(root)
        while i < len(currLevelNodes):
            
            node = currLevelNodes[i]
            if not node:
                noneWidth+=1
            else:
                currWidth = currWidth + 1 + noneWidth
                noneWidth = 0
                # nextLevelNodes.append([node.left,currLevel+1])
                # nextLevelNodes.append([node.right,currLevel+1])
                nextLevelNodes.append(node.left)
                nextLevelNodes.append(node.right)

            maxWidth = max(maxWidth,currWidth)
            i+=1
            if i == len(currLevelNodes):
                i = 0
                currLevel+=1
                currWidth = 0
                currLevelNodes = nextLevelNodes
                nextLevelNodes = []
                
        # print(maxWidth)
        return maxWidth