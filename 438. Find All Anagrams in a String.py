class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p)>len(s):
            return []
        if p == s:
            return [0]
        
        pointer = 0
        plist = list(p)
        res = []
        i = 0
        while i<len(s) and pointer<len(s)-len(p)+1:
            # print(i,s[i],plist,pointer)
            c = s[i]
            if c in plist:
                plist.remove(c)
                if len(plist) == 0:
                    res.append(pointer)
                    plist = list(s[pointer])
                    # plist = list(p)
                    # plist.remove(s[pointer])
                    i = i+1
                    pointer=pointer+1
                else:
                    i+=1
            else:
                if c not in p:
                    pointer = i+1    
                    plist = list(p)
                    i = pointer
                else:
                    plist.append(s[pointer])
                    pointer = pointer+1
                    # plist = list(p)
                    # i = pointer
                    
                

            
        return res