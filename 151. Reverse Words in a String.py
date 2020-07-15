class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x for x in reversed(s.split(' ')) if x!=''])