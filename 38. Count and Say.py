class Solution:
    lookup = []
    def countAndSay(self, n: int) -> str:
        def generateNext(sent):
            prev = sent[0]
            res = ''
            count = 1
            for c in sent[1:]:
                if c == prev:
                    count+=1
                    continue
                else:
                    res = res + str(count)+prev
                    prev = c
                    count = 1
            res = res + str(count)+prev
            return res
        
        
        if n < 1:
            return ''
        l = len(self.lookup)
        if l == 0:
                self.lookup.append('1')
                l+=1
        if n <= l:
            return self.lookup[n-1]
        else:
            while n>l:
                prev = self.lookup[-1]
                self.lookup.append(generateNext(prev))
                n-=1

        return self.lookup[-1]