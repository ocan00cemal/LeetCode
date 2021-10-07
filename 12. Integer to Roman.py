from math import ceil, log10


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }

        if num in [1, 10, 100, 1000]:
            return roman_dict[num]

        roman = ""
        num_range = ceil(log10(num))
        
        for i in range(num_range):
            n = 10 ** (i + 1)
            m = n // 2
            k = n // 10

            n_remainder = num % n
            m_remainder = num % m

            if n_remainder in roman_dict.keys() and n_remainder >= k:
                roman = roman_dict[n_remainder] + roman
            elif n_remainder > 9 * (k):
                roman = roman_dict[9 * (k)] + roman
            elif n_remainder > m:
                roman = roman_dict[m] + (m_remainder // (k)) * roman_dict[k] + roman
            elif n_remainder >= 4 * (k):
                roman = roman_dict[4 * (k)] + roman
            elif n_remainder < m:
                roman = (m_remainder // (k)) * roman_dict[k] + roman

        return roman
