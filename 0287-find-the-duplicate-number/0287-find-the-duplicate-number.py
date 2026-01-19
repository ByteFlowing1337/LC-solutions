class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map_ = set()
        for i in range(len(nums)):
            if nums[i] in map_:
                return nums[i]
            else:
                map_.add(nums[i])