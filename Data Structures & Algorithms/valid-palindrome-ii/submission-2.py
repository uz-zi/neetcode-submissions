class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(string, l, r):
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1
        while (l < r):
            if s[l] == s[r]:
                r -= 1
                l += 1
            else:
                return is_pali(s, l + 1, r) or is_pali(s, l, r - 1)

        return True