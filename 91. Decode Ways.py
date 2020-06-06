class Solution:
    def numDecodings(self, s: str) -> int:
        
        def recursionHelper(idx):
            # print(s)
            count = 0
            if idx<len(s) and s[idx] == '0':
                count = 0
            elif idx>len(s)-2:
                count = 1
            else:
                
                if lookup.get(idx+1,-1) != -1:
                    count+=lookup[idx+1]
                else:
                    count+=recursionHelper(idx+1)
                if ('0' < s[idx] < '2') or (s[idx] == '2' and s[idx+1] < '7'):
                    if lookup.get(idx+2,-1) != -1:
                        count+=lookup[idx+2]
                    else:
                        count+=recursionHelper(idx+2)
            # print(s,count)
            lookup[idx] = count
            return count
            
        if not s or s[0] == '0':
            return 0
        lookup = {} #idx:count
        return recursionHelper(0) 

            