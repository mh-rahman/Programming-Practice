class Solution:
    def isMatchX(self, s: str, p: str) -> bool:
        
        def reducePatter(p):
            temp = []
            for c in p:
                if temp and c == '*' and temp[-1] == '*':
                    continue
                temp.append(c)
            return ''.join(temp)
        
        def checkpattern(pattern):
            for c in pattern:
                if c != '*':
                    return 0
            return 1
        
        def lenCheck(s,p):
            p = p.replace('*','')
            return len(s) >= len(p)
        
        def helper(s,p):
            pflag = checkpattern(p)
            if not s:
                return pflag
            if not p:
                return 0
            if pflag:
                return pflag
            # print(s,p)
            if not lenCheck(s,p):
                return 0
            combined = s+'#'+p
            if lookup.get(combined,-1) != -1:
                # print('CACHE!')
                return lookup[combined]
            else:
                flag = 0
                if p[0] == s[0] or p[0] == '?':
                    flag = helper(s[1:],p[1:])
                elif p[0] == '*':
                    flag = 0
                    i = 0
                    while i<len(s)+1 and not flag:
                        flag = helper(s[i:],p[1:])
                        i+=1
                else:
                    flag = 0
                
                lookup[combined] = flag
                return flag

        
        lookup = {} #'s#p':True/False
        flagDict = {1:True,0:False}
        p = reducePatter(p)
        flag = helper(s,p)
        # print(lookup)
        
        return flagDict[flag]
        
        



    def isMatchOptimal(self, s, p):
        s_cur = 0;
        p_cur= 0;
        match = 0;
        star = -1;
        while s_cur<len(s):
            if p_cur< len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=='?'):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur<len(p) and p[p_cur]=='*':
                match = s_cur
                star = p_cur
                p_cur = p_cur+1
            elif (star!=-1):
                p_cur = star+1
                match = match+1
                s_cur = match
            else:
                return False
        while p_cur<len(p) and p[p_cur]=='*':
            p_cur = p_cur+1
            
        if p_cur==len(p):
            return True
        else:
            return False
