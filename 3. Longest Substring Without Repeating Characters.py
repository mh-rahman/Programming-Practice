class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # print(len(set([1,2,1,3])))
        start = 0
        end = 0
        unique = set([])
        maxlen = 0
        while end<len(s):
            # print()
            if s[end] not in unique:
                unique.add(s[end])
                end+=1
                maxlen = max(maxlen, end-start)
            else:
                unique.remove(s[start])
                start+=1
            # print(maxlen)
        return maxlen
        
        # return 3
        
        
        
        
        
        
        
        
        
        
        ##Approach1 - fails for abcb
        # if s == '':
        #     return 0
        # maxChar = max(s, key = lambda x: s.count(x))
        # # print(maxChar)
        # return 1+max([self.lengthOfLongestSubstring(sent) for sent in s.split(maxChar)])
        
        