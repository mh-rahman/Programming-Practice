# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class node:
    def __init__(self,tn):
        self.tn = tn #TreeNode
        self.next = None
        # self.prev = None
        self.visited = 0

class llist:
    def __inti__(self):
        self.head = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        Q = [[root,0]] #[node,visited]
        unvisitedCount = 1
        idx = 0
        while unvisitedCount > 0:
            idx = 0 #update this step to store last good index
            #Reach first unvisited node
            while Q[idx][1]:
                idx+=1
            temp = []
            curr = Q[idx][0]
            left,right = curr.left, curr.right
            if left:
                unvisitedCount+=1
                temp.append([left,0])
            temp.append([curr,1])
            unvisitedCount-=1
            if right:
                unvisitedCount+=1
                temp.append([right,0])
            
            newQ = Q[:idx]+temp+Q[idx+1:]
            del(Q)
            Q = newQ
            
        Q = [node.val for node,_ in Q]
        # print(Q)

        return Q