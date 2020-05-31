import itertools

class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        
        def getUnique(start,end):
            # ball_collect = collections.Counter(x[start:end+1])
            return len(set(x[start:end]))
            
            
            
        
        temp = []
        for i,ball in enumerate(balls):
            temp+=[i+1]*ball
        a = list(perm_unique(temp))
        den = len(a)
        num = 0
        for x in a:
            if getUnique(0,len(x)//2) == getUnique(len(x)//2, len(x)):
                num+=1
            
        
        # print(a)
        # print(len(a))
        # print(num,den)
        
        
        return num/den