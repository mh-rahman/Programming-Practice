class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        def helper(k):
            # print(lookup)
            if len(lookup) == 0:
                return True
            num = next(iter(lookup))
            count = lookup[num]
            if count-1 > 0:
                lookup[num] = count-1
            else:
                lookup.pop(num)
            keys = list(lookup.keys())
            for key in keys:
                if (num+key)%k != 0:
                    continue
                key_count = lookup.pop(key)
                if key_count-1 > 0:
                    lookup[key] = key_count-1
                if helper(k):
                    return True
                else:
                    lookup[key] = key_count
                
            lookup[num] = count
            return False
                
        lookup = Counter(arr)
        return helper(k)
        