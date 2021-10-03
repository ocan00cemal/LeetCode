class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        long_len = len(temp)

        for c in s:
            if not c in temp:
                temp += c
            else:
                if len(temp) > long_len:
                    long_len = len(temp)
                temp = temp[temp.index(c) + 1 :] + c

        if len(temp) > long_len:
            long_len = len(temp)

        return long_len
