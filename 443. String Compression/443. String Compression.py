class Solution:
    def compress(self, chars: List[str]) -> int:
        start,prev,ct = 0,0,0
        res = 0
        chars.append(1)
        for i in range(len(chars)):
            if chars[i] == chars[prev]:
                ct += 1
            else:
                if ct!=1:
                    chars[start] = chars[prev]
                    for j in range(1,len(str(ct))+1):
                        chars[start+j] = str(ct)[j-1]
                    start += len(str(ct)) + 1
                else:
                    chars[start] = chars[prev]
                    start += 1
                prev = i
                ct = 1
        while len(chars)>start:
            chars.pop()