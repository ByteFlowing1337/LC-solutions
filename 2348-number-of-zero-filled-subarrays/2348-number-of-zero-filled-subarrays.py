class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        totalsub=0
        currentsub=0
        for num in nums:
            if num ==0:
                currentsub+=1
                totalsub+=currentsub
            else:
                currentsub=0
        return totalsub