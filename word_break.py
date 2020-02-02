'''
The idea is the following:

    d is an array that contains booleans

    d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word
'''


class Solution:
    def word_break(self,s, words):
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in words:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.word_break(s,wordDict)
        