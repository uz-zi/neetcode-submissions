class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        maxlength = 0
        length = 0
        i = 0
        j = 0
        maxf = 0

        while i <= len(s)-1:
            if s[i] in dic:
                dic[s[i]] +=1
            else:
                dic[s[i]] =1

            maxf = max(dic.values())
            
            length = (i -j)+1
            if length - maxf <= k:
                maxlength = max(length,maxlength)
            else:
                dic[s[j]] -=1
                j +=1
            
            i+=1

        return maxlength


        