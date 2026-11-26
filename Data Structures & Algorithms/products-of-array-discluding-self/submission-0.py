class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        postfix = {}
        output = []

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i+1] * nums[i]

        
        for i in range(len(nums)):
            l = i - 1
            r = i + 1
            if l < 0:
                output.append(postfix[r])
            elif r > len(nums) - 1:
                output.append(prefix[l])
            else:
                output.append(prefix[l] * postfix[r])

        return output