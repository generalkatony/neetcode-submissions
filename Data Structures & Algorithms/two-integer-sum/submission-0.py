class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = 0

        for i in range(len(nums)):
            j = i + 1
            result = []

            value1 = nums[i]
            value2 = target - nums[i]

            for k in range(j,len(nums)):
                if nums[k] == value2:
                    return [i,k]