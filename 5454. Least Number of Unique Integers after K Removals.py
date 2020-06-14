class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numcount = collections.Counter(arr)
        # numcount.sort(key = numcount.get)
        numcount = [[x,numcount[x]] for x in numcount]
        numcount.sort(key = lambda x: x[1],reverse=True)
        print(numcount)
        idx = len(arr)-1
        while k>0 and idx >=0:
            c = numcount.pop() 
            print(c)
            k-=c[1]
            idx-=1
        res = len(numcount)
        if k < 0:
            res+=1

        return res