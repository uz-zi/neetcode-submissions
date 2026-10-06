class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(i,j):
            if i == j == n:
                res.append("".join(stack))
                return

            if i < n:
                stack.append("(") 
                dfs(i+1,j)
                stack.pop()

            if j < i:
                stack.append(")")
                dfs(i,j+1)
                stack.pop()   

        dfs(0,0)

        return res            
