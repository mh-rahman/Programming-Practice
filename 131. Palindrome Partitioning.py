class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(s,constructed):
            if not s:
                res.append(constructed)
                return
            for i in range(1,len(s) +1):
                if s[:i] == s[i-1::-1]:
                    helper(s[i:],constructed+[s[:i]])
            return
        
        res = []
        helper(s,[])
        return res
            
        