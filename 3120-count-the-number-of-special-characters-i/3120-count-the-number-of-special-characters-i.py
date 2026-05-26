class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        return sum(c in s and c.upper() in s for c in string.ascii_lowercase)