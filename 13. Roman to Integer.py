class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for char in s:
            result += roman_dict[char]

        if "IV" in s or "IX" in s:
            result -= 2
        if "XL" in s or "XC" in s:
            result -= 20
        if "CD" in s or "CM" in s:
            result -= 200
        return result
