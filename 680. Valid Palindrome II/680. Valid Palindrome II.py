class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range((len(s))//2):
            if s[i] != s[-1-i]:
                t, u = s[:i]+s[i+1:], s[:-1-i]+s[len(s)-i:]
                return t == t[::-1] or u == u[::-1]
        return True