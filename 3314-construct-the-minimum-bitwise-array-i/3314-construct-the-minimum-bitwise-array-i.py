class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in nums:
            if i == 2:
                ans.append(-1)
            else:
                p = 0
                while (i >> p) & 1:
                    p += 1
                ans.append(i ^ (1 << (p-1)))
        return ans