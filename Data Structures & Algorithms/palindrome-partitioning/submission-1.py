class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def ispalin(s,j,i):
            while j <= i:
                if s[i] != s[j]:
                    return False
                j+=1
                i-=1
            return True

        def dfs(j,i):
            if i >= len(s):
                if i == j:
                    res.append(part[:])
                return
            
            if ispalin(s,j,i):
                part.append(s[j:i+1])
                dfs(i+1,i+1)
                part.pop()
            
            dfs(j,i+1)

        dfs(0,0)
        return res
        


                