class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        #length of strs is >= 2
        substring = ""
        for i in range(min(len(strs[0]), len(strs[1]))):
            if strs[0][i] == strs[1][i]:
                substring = substring + strs[0][i]
            else:
                break
        print(substring)
        for i in range(2,len(strs)):
            for j in range(min(len(substring), len(strs[i]))):
                if substring[j] == strs[i][j]:
                    print(strs[i][j])
                else:
                    substring = substring[:j]
                    break
            substring = substring[:min(len(substring), len(strs[i]))]
            print(substring)
        return substring