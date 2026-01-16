class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1,m])
        vFences.extend([1,n])
        hFences.sort()
        vFences.sort()
        max_len=-1
        hgap_set=set()
        for i in range(len(hFences)):
            for j in range(i+1,len(hFences)):
                hgap=hFences[j]-hFences[i]
                hgap_set.add(hgap)
        for i in range(len(vFences)):
            for j in range(i+1,len(vFences)):
                    vgap=vFences[j]-vFences[i]
                    if vgap in hgap_set:
                        max_len=max(max_len,vgap)
        if max_len ==-1:
            return -1
        else:
            return (max_len**2) % (10**9+7)