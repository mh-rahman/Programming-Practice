class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1 = p2 = math.inf
        res = math.inf
        for i,w in enumerate(words):
            if w == word1:
                p1 = i
                res = min(res, abs(p1-p2))
            if w == word2:
                p2 = i
                res = min(res, abs(p1-p2))
                
        return res