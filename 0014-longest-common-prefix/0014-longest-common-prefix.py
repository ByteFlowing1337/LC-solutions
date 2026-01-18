class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        for i in range(len(base)):
            char = base[i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return base[:i]
        return base

                