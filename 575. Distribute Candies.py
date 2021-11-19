class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        candy_dict = {}
        for i in candyType:
            if not i in candy_dict:
                candy_dict[i] = True

        m = len(candy_dict)

        if n >= m:
            return m
        elif n < m:
            return n
