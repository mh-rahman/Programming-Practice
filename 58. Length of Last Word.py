class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        # print(s)
        for i in range(len(s)-1,-1,-1):
            # print(s[i])
            if len(s[i])>0:
                return len(s[i])
        return 0
        return 0