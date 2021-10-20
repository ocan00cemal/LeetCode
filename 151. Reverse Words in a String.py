class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        spaceless_s = []

        for i in s:
            if i != "":
                spaceless_s.append(i)

        return " ".join(reversed(spaceless_s))
