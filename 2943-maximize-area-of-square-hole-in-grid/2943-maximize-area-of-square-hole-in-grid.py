class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_maxgrid(bars):
            if not bars:
                return 1
            else:
                bars.sort()
                max_len=1
                current_len=1
                for i in range(len(bars)):
                    if bars[i] == bars[i-1]+1:
                        current_len+=1
                    else:
                        current_len=1
                    max_len=max(max_len,current_len) 
            return max_len+1
        hgrid = get_maxgrid(hBars)
        vgrid = get_maxgrid(vBars)
        grid = min(hgrid,vgrid)
        return grid*grid