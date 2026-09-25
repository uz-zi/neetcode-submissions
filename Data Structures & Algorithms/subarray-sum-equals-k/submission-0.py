class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0] = 1
        required = 0
        count = 0
        total_sum = 0

        for num in nums:
            total_sum += num
            required = total_sum - k
            count += dic.get(required,0)
            if total_sum not in dic.keys():
                dic[total_sum] = 1
            else:
                dic[total_sum] += 1

        return count

        

            
        