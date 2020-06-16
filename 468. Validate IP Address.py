class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(arr:List[str]) -> str:
            # print(arr)
            if len(arr) != 4:
                return 'Neither'
            for s in arr:
                try:
                    n = int(s)
                except:
                    return 'Neither'
                if (n and s[0] == '0') or (not 0 <= n < 256) or (not n and len(s)>1):
                    return 'Neither'
            return 'IPv4'
            
            
        def isIPv6(arr:List[str]) -> str:
            # print(arr)
            if len(arr) != 8:
                return 'Neither'
            for x in arr:
                if not 0 < len(x) < 5:
                    return 'Neither'
                s = x.lower()
                for c in s: 
                    if not ('0' <= c <= '9' or 'a' <= c <= 'f'):
                        return 'Neither'
            return 'IPv6'
            
        
        # print('abc123ABC'.lower())
        if '.' in IP:
            return isIPv4(IP.split('.'))
        elif ':' in IP:
            return isIPv6(IP.split(':'))
        return 'Neither'