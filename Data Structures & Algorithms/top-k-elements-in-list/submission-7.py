class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] =1
            else:
                dic[nums[i]] +=1

        res =sorted(dic, key=dic.get, reverse=True)
        return res[:k]