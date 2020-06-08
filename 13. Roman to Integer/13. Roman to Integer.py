class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'IV':';4;',
            'IX':';9;',
            'XC':';90;',
            'XL':';40;',
            'CD':';400;',
            'CM':';900;'
        }
        t = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            
        }
        for key in m:
            s = s.replace(key,m[key])
        
        s = s.split(';')
        res = 0
        for i in s:
            if i:
                try:
                    res += int(i)
                except:
                    for l in i:
                        res += t[l]
        return res