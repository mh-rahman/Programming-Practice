class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not  strs:
            return ''
        
        small = min(strs, key = lambda x: len(x))
        for s in strs:
            while small and small != s[:len(small)]:
                small = small[:-1]
            if  not small:
                break
        
        return small