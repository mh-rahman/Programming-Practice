class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        s = [c for c in s]
        i,j = 0, len(s)-1
        while i < j:
            while i < j and s[i].lower() not in vowels:
                i += 1
            while j > i and s[j].lower() not in vowels:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
