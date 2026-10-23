class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        sufix = 1
        arr = [1] * n
        for i in range(n):
            arr[i] = prefix
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            arr[i] *= sufix
            sufix *= nums[i]

        return arr






        