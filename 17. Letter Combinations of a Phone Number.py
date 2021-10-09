class Solution:
    def letterCombinations(self, digits: str):
        combinations = []
        phone_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def rec(idx, temp_str=""):
            if len(temp_str) == len(digits):
                combinations.append(temp_str)
                return
            for digit in phone_dict[digits[idx]]:
                rec(idx + 1, temp_str + digit)

        if digits:
            rec(0)
        return combinations



