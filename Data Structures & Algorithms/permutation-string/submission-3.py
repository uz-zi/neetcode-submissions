class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0] *26
        arr2 = [0] *26

        for s in s1:
            arr1[ord(s) - ord('a')]+=1

        window = len(s1)
        j = 0
        for i in range(len(s2)):
            arr2[ord(s2[i]) - ord('a')]+=1

            if i -j+1 > window:
                arr2[ord(s2[j]) - ord('a')] -=1
                j+=1
            
            if arr1 == arr2:
                return True
        return False
        