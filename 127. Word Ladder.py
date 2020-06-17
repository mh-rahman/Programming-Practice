class Node:
    def __init__(val,level):
        self.val = val
        self.level = level
        self.children = []

class Solution:
    def ladderLength(self, bw: str, endWord: str, wordList: List[str]) -> int:
        def isdiff1(w1,w2):
            count = 2
            for c1,c2 in zip(w1,w2):
                if c1 != c2:
                    count-=1
                if not count:
                    return False
            return True
        
        Q = deque()
        Q.append([bw,1])
        try:
            wordList.remove(bw)
        except:
            pass
        while Q:
            bw,level = Q.popleft()
            if endWord == bw:
                return level
            idx = 0
            while idx < len(wordList):
                w = wordList[idx]
                if isdiff1(bw,w):
                    Q.append([w,level+1])
                    wordList[idx] = wordList[-1]
                    wordList.pop()
                else:
                    idx+=1
            #     print(wordList)
            # print('Queue', Q)
            
        return 0


        