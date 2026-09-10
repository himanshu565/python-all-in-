# Q1 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = {}

        for i in range(len(s)):
            if s[i] in f:
                f[s[i]] += 1
            else:
                f[s[i]] = 1

        for i in range(len(s)):
            if f[s[i]] == 1:
                return i

        return -1



# Q2 ransome note 