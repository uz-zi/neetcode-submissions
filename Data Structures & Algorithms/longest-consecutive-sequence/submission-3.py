class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlen  =0
        length =0
        current = 0

        for num in s:
            if num-1 not in s:
                current = num
                length = 1

                while(current + 1 in s):
                    current = current+1
                    length +=1
                

            maxlen = max(maxlen, length)

        return maxlen
                
        