class Solution:
    
    def longestCommonPrefix(self, strs):
        long_common_pre = ""
        shortest_str_len = len(min(strs, key=len)) 
        for char in range(shortest_str_len):
            temp = ""
            for word in strs:
                if strs.index(word) == 0:
                    temp = word[char]                   
                if word[char] == temp and len(long_common_pre) < char+1:
                    long_common_pre += temp
                elif word[char] != temp:
                    return long_common_pre[:-1]
        return long_common_pre 
