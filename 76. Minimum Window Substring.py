class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def isValid():
            for key in tcounter.keys():
                if ccounter[key] < tcounter[key]:
                    return False
            return True
        
        if not s or not t:
            return ''
        
        Q = []
        min_win = len(s)+1
        res = ''
        tcounter = collections.Counter(t)
        ccounter = {k:0 for k in tcounter.keys()}
        
        i = 0
        while i < len(s):
            c = s[i]
            if tcounter.get(c,-1) == -1:
                i+=1
                continue
            ccounter[c]+=1
            Q.append([i,c])
            while Q and isValid():
                rem_i,rem_c = Q[0]
                curr_win = Q[-1][0] - Q[0][0]
                if curr_win < min_win:
                    min_win = curr_win
                    res = s[rem_i:rem_i+curr_win+1]
                ccounter[rem_c]-=1
                del(Q[0])
                # print(ccounter)
                # print(res)
            i+=1
                
        return res