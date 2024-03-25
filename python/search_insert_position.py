# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         if target == 0:
#             return 0
#         elif target == 1:
#             return 1
        
#         j = 0


#         for i in range(len(nums)-1):
#             if nums[i] == target:
#                 return i
            
#             elif nums[i+1]  > target:
#                 print("elif")
#                 return i+1
#             j += 1

#         return j if target in nums else j+1

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        
        lnums = len(nums)

        for i in range(lnums):
            if nums[i] >= target:
                return i
        return lnums

res = Solution().searchInsert([-1,3,5,6], 70)
print(res)
