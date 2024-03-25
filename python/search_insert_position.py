class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        
        lnums = len(nums)

        for i in range(lnums):
            if nums[i] >= target:
                return i
        
        return lnums
