class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        res = ''
        for l in s:
            if l in cs:
                res += l.lower()
        return res == res[::-1]