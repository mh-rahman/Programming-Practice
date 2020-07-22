class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        diff = math.inf
        for i in range(1,len(arr)):
            if diff == arr[i]-arr[i-1]:
                res.append([arr[i-1],arr[i]])
            elif diff > arr[i]-arr[i-1]:
                diff = arr[i]-arr[i-1]
                del(res)
                res = []
                res.append([arr[i-1],arr[i]])
        return res
        
            