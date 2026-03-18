class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        total = 0
        for i in range(row_len):
            for j in range(col_len):
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                if grid[i][j] <= k:
                    total += 1
                elif j == 0:
                    break
        return total
