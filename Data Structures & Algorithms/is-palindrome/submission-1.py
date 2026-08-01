class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(ch.lower() for ch in s if ch.isalnum())

        j = len(string) -1
        i = 0

        while(i <= j):
            if string[i] != string[j]:
                return False
            i+=1
            j-=1
        
        return True




        