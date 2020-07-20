class Solution:
    def wordPattern(self, pattern: str, words: str) -> bool:
        p_lookup, w_lookup = {}, set([])
        words = words.split(' ')
        if len(pattern) != len(words):
            return False
        for p,word in zip(pattern,words):
            if p not in p_lookup:
                if word in w_lookup:
                    return False
                p_lookup[p] = word
                w_lookup.add(word)
            if p_lookup[p] != word:
                return False
        return True