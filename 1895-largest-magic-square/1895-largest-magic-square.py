class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        height,width=len(grid),len(grid[0])
        row_sum = [[0] * (width+1) for _ in range(height)]
        col_sum = [[0] * (width) for _ in range(height+1)]
        for i in range(height):
            for j in range(width):
                row_sum[i][j+1] = row_sum[i][j] + grid[i][j]
                col_sum[i+1][j] = col_sum[i][j] + grid[i][j]
        for k in range(min(height,width),1,-1):
            for i in range(height - k + 1):
                for j in range(width - k + 1):
                    target = row_sum[i][j+k] - row_sum[i][j]
                    match = True

                    for r in range(i,i+k):
                        if (row_sum[r][j+k] - row_sum[r][j]) != target:
                            match = False
                            break
                    if not match:
                        continue
                    for c in range(j,j+k):
                        if (col_sum[i+k][c] - col_sum[i][c]) != target:
                            match = False
                            break
                    if not match:
                        continue
                    d1,d2=0,0
                    for d in range(k):
                        d1 += grid[i+d][j+d]
                        d2 += grid[i+d][j+k-1-d]
                    if d1 == target and d2 == target:
                        return k
        return 1