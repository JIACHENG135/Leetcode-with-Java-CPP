class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        for i in range(len(min(strs,key=lambda x: len(x)))):
            if all(strs[k][i] == strs[k+1][i] for k in range(len(strs)-1)):
                res += strs[0][i]
            else:
                break
        return res