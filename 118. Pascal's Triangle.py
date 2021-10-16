class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]

        cur_triangle = [[1], [1, 1]]

        for i in range(2, numRows):
            j = i - 1
            cur_row = [1]

            for internal in range(j):
                cur_row.append(
                    cur_triangle[j][internal] + cur_triangle[j][internal + 1]
                )

            cur_row.append(1)
            cur_triangle.append(cur_row)

        return cur_triangle
