class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        for i in range(len(accounts)):
            account = accounts[i]
            account[0],account[-1] = account[-1],account[0]
            name = account.pop()
            accounts[i] = [name,set(account)]
            
        for i in range(len(accounts)):
            name1,set1 = accounts[i]
            j = 0
            if not name1:
                continue
            while j < len(accounts):
                name2,set2 = accounts[j]
                if i == j or not name2 or name1 != name2 or not set1.intersection(set2):
                    j+=1
                    continue
                set1 = set1.union(set2)
                accounts[j] = [None,None]
                accounts[i] = [name1,set1]
                j = 0
        res = [[name]+sorted(list(eset)) for name,eset in accounts if name]
        return res
            