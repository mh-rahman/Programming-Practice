class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for c in address:
            if c != '.':
                res.append(c)
            else:
                res.append('[.]')
        return ''.join(res)