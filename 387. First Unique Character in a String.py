class Solution:
    def firstUniqChar(self, s: str) -> int:
        # method1
#         charDict = {}
#         for i,c in enumerate(s):
#             # charDict[c] = charDict.get(c,-1)+1
#             if charDict.get(c,[-1,-1])[1] == -1:
#                 charDict[c] = [i,1]
#             else:
#                 charDict[c] = [charDict[c][0],charDict[c][1]+1]
#         for c in charDict.keys():
#             if charDict[c][1] == 1:
#                 return charDict[c][0]
#         return -1

        #method2
        charArray = [[0,0] for i in range(26)] 
        seenChars = []
        for i,c in enumerate(s):
            if c not in seenChars:
                seenChars.append(c)
                charArray[ord(c) - ord('a')][0] = i
            charArray[ord(c) - ord('a')][1]+=1
        for c in seenChars:
            if charArray[ord(c) - ord('a')][1] == 1:
                return charArray[ord(c) - ord('a')][0]
            
        # print(charArray)
        return -1