class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        for num in nums:
            numsDict[num] = numsDict.get(num,0)+1
            
        dict_items = sorted(list(numsDict.items()), key = lambda x: x[1], reverse=True)
        # print(dict_items)
        
        res = [x[0] for x in dict_items[:k]]
        
        return res
        