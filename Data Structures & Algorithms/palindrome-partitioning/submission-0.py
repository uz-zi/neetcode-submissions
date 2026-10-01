class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def is_palin(s,i,j):
            while (j < i):
                if s[j] != s[i]:
                    return False
                j +=1
                i -=1
            return True

        def dfs(j,i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if is_palin(s,i,j):
                part.append(s[j:i+1])
                dfs(i+1,i+1)
                part.pop()

            dfs(j,i+1)

        dfs(0,0)
        return res

        