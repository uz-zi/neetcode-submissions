class Solution:
    def longestPalindrome(self, s: str) -> str:
        startingIndex = 0
        resLength = 0

        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r -l+1 > resLength:
                    resLength = r-l+1
                    startingIndex = l
                l-=1
                r+=1

            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r -l+1 > resLength:
                    resLength = r-l+1
                    startingIndex = l
                l-=1
                r+=1

        return s[startingIndex: startingIndex+resLength]
            

