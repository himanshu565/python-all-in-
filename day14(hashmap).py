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



# Q2 ransome note class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create Counter objects for the ransomNote and magazine strings
        note, mag = Counter(ransomNote), Counter(magazine)
        
        # Check if the intersection of note and mag Counter objects is equal to note Counter object
        # If it is, it means that all the letters in ransomNote can be formed using the letters in magazine
        # the intersection gives the minimum count of a character if a is 2 and b is 1 but b is not present in note it will return only a:2 
        if note & mag == note: return True
        return False
    
    

# Q3 maximum  number of balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have = {}
        for char in text:
            have[char] = have.get(char,0) + 1
        need= {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1 }
        res = float('inf')
        for char in need:
            fhave = have.get(char, 0)
            fneed = need[char]

            times = fhave // fneed

            res = min(res, times)

        return res

#      alternate 
#            def maxNumberOfBalloons(self, text: str) -> int:
#               f = Counter(text)
#               return min(f["b"], f["a"], f["l"] >> 1, f["o"] >> 1, f["n"])        
        
# Q4 409. Longest Palindrome
class Solution(object):
    def longestPalindrome(self, s):
        freq={}
        count=0
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            if freq[char]%2==0:
                count+=2
            else:
                continue
        has_odd = any(f%2==1 for f in freq.values())
        return count + (1 if has_odd else 0)