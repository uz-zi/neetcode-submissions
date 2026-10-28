class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        i = 0
        j = 0
        maxsize =0 

        while i < len(s):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

            maxf = max(dic.values())

            if (i - j+1) - maxf <= k:
                maxsize = max(i - j+1, maxsize)
            else:
                dic[s[j]] -=1
                j+=1

            i+=1

        return maxsize