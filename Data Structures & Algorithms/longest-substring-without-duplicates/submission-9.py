class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic ={}
        j = 0
        i = 0
        maxlength = 0
        length = 0

        while i <= len(s)-1:
            if s[i] in dic:
                if dic[s[i]] >= j:
                    j = dic[s[i]] +1
            
            length = (i - j)+1
            maxlength = max(length, maxlength)
            dic[s[i]] = i
            i+=1

        return maxlength

        
        