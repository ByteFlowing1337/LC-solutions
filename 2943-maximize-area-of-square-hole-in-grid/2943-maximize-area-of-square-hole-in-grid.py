class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_maxlen(bars):
            if not bars:
                return 1
            else:
                current_len=1
                max_len=1
                bars.sort()
                for i in range(1,len(bars)):
                    if bars[i] == bars[i-1]+1:
                        current_len+=1
                    else:
                        current_len=1
                    max_len=max(max_len,current_len)
                return max_len+1
        hside=get_maxlen(hBars)
        vside=get_maxlen(vBars)
        side=min(hside,vside)
        return side*side
            