class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        negated= {'R':0, 'D':0}
        opp = {'R':'D', 'D':'R'}
        while count['D'] >0 and count['R'] > 0:
            # print(senate)
            senate = [c for c in senate if c]
            for i,c in enumerate(senate):
                if negated[c] > 0:
                    negated[c] -= 1
                    count[c] -= 1
                    senate[i] = ''
                    continue
                else:
                    negated[opp[c]] += 1
        return 'Dire' if count['D'] > 0 else 'Radiant'

        
    def TLEPredictPartyVictory(self, senate: str) -> str:
        
        countDict, senate = Counter(senate), [c for c in senate]
        # print(countDict)
        
        while True:
            l = len(senate)
            # print(l)
            for i in range(l):
                curr, opp = senate[i],'R'
                if not curr:
                    continue
                if curr == 'R':
                    opp = 'D'
                    
                ## Negate the first oopposition:
                j = (i+1)%l
                while j != i:
                    if senate[j] == opp:
                        senate[j] = ''
                        countDict[opp] -= 1
                        break
                    j = (j+1)%l
            senate = [c for c in senate if c]
            if countDict['R'] == 0 or countDict['D'] == 0:
                break
        
        return 'Dire' if countDict['R'] == 0 else 'Radiant'