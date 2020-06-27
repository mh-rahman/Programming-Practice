class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def helper(s,idx,constructed, rem_count, open_count):
            # print((idx,constructed, rem_count, open_count))
            if rem_count > min_rem:
                return
            if idx >= len(s):
                if open_count == 0:
                    res.add(constructed)
                return
            if constructed in lookup[idx]:
                return
            
            curr = s[idx]
            new_count = open_count
            if curr not in ('(',')'):
                helper(s,idx+1,constructed+curr,rem_count,new_count)
                lookup[idx].add('constructed')
                return
            elif curr == '(':
                new_count = open_count+1
            elif curr == ')':
                new_count = open_count-1
            #check if potential removals less than min required removals
            if new_count >= 0: 
                helper(s,idx+1,constructed+curr,rem_count,new_count)
            # if rem_count + (len(s) - idx) > min_rem:
            helper(s,idx+1,constructed,rem_count+1,open_count)
            lookup[idx].add('constructed')
            return
        
        if not s:
            return [""]
        st = []
        lookup = []
        for c in s:
            lookup.append(set())
            if c not in ('(',')'):
                continue
            if c == ')' and st and st[-1] == '(':
                st.pop()
            else:
                st.append(c)
        
        min_rem = len(st)

        res = set()
        helper(s,0,'',0,0)
        # print(res)
        if not res:
            res = [""]
        # print(res)
        return res
        return []