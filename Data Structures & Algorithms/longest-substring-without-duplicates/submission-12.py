class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l = 0
        r = 0
        maxlength = 0
        length = 0

        while r < len(s):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]]+1
            
            dic[s[r]] = r
            length = (r -l)+1
            maxlength = max(length,maxlength)
            r+=1

        return maxlength

        
        