class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        for k in r_counter:
            if k not in m_counter or m_counter[k] < r_counter[k]:
                return False
        return True