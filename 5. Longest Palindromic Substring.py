class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        longest = ""

        for i in range(n):
            l, r = i - 1, i + 1
            try:
                while s[l] == s[r]:
                    if len(s[l : r + 1]) > len(longest):
                        longest = s[l : r + 1]
                    l -= 1
                    r += 1
            except:
                pass

        for i in range(n):
            j = i + 1
            l, r = i - 1, j + 1
            try:
                if s[i] == s[j]:
                    if len(longest) < 2:
                        longest = s[i : j + 1]
                    while s[l] == s[r]:
                        if len(s[l : r + 1]) > len(longest):
                            longest = s[l : r + 1]
                        l -= 1
                        r += 1
            except:
                pass

        return longest if len(longest) > 1 else s[0]
