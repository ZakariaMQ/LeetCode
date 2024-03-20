class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while prefix not in s[:len(prefix)]:
                prefix = prefix[:-1]
        
        return prefix
    