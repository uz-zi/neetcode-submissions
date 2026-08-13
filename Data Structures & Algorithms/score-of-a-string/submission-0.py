class Solution:
    def scoreOfString(self, s: str) -> int:
        j = 1
        score = 0
        for i in range(len(s)-1):
            score += (abs(ord(s[j]) - ord(s[i])))
            j+=1

        return score
            
            
        