class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = 0
        r = 0
        nums = sorted(nums)
        while r < len(nums):
            
            if r == 0:
                r += 1

            elif nums[l] == nums[r]:
                return True
            
            else:
                l += 1
                r += 1
        return False