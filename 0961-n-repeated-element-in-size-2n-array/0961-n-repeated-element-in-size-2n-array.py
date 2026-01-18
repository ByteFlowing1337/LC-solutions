class Solution:
        def repeatedNTimes(self, nums: List[int]) -> int:
            exist = set()
            for i in range(len(nums)):
                if nums[i] in exist:
                    return nums[i]
                else:
                    exist.add(nums[i])
