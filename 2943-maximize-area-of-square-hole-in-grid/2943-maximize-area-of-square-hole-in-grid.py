class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def get_grid(bars):
            max_side = 1
            current_side = 1
            bars.sort()
            for i in range(len(bars)):
                if bars[i] == bars[i-1] +1:
                    current_side += 1
                else:
                    current_side = 1
                max_side = max(max_side,current_side)
            return max_side +1
        vSide = get_grid(vBars)
        hSide = get_grid(hBars)
        Side = min(vSide,hSide)
        return Side**2