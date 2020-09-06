import bisect

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dict1 = {}
        for i,x in enumerate(nums1):
            if x not in dict1:
                dict1[x] = []
            dict1[x].append(i)
        dict2 = {}
        for i,x in enumerate(nums2):
            if x not in dict2:
                dict2[x] = []
            dict2[x].append(i)
        
        # print(dict1)
        # print(dict2)
        
        res = 0
        
        # triplets-1
        
        for t in nums1:
            prod = t*t
            for j,n in enumerate(nums2):
                if prod%n != 0:
                    continue
                target = prod//n
                if target in dict2:
                    indices = dict2[target]
                    # Getting the number of 'k' > 'j'
                    insertion_point = bisect.bisect(indices, j) 
                    res += (len(indices) - insertion_point)
                    
        
        # triplets-2
        
        for t in nums2:
            prod = t*t
            for j,n in enumerate(nums1):
                if prod%n != 0:
                    continue
                target = prod//n
                if target in dict1:
                    indices = dict1[target]
                    # Getting the number of 'k' > 'j'
                    insertion_point = bisect.bisect(indices, j) 
                    res += (len(indices) - insertion_point)
                
                
                
        return res