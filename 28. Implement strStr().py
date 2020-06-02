class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        if not needle:
            return 0
            
        
        res = 0
        curr = 0
        idx = 0
        while curr < len(haystack):
            if haystack[curr] == needle[idx]:
                curr+=1
                idx+=1
            else:
                res+=1
                idx = 0
                curr = res
            if idx == len(needle):
                return res
            
        return -1
            