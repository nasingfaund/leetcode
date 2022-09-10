class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        longest_common_prefix = ""
        first_str = strs[0]
        for index in range(len(first_str)):
            if all(string[index] == first_str[index] if index < len(string) else False for string in strs[1:]):
                longest_common_prefix += first_str[index]
            else:
                break
                
        return longest_common_prefix

