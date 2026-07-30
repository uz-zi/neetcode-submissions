class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic= {}
        require = 0

        for i in range(len(nums)):
            require = target - nums[i]
            if require in dic:
                return [dic[require], i ]
            else:
                dic[nums[i]] = i

            

            



            

        