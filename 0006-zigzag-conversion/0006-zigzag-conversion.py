class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        step = 1
        current_row = 0
        rows = [""] * numRows
        for char in s:
            rows[current_row] += char
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
            current_row += step
        return "".join(rows)