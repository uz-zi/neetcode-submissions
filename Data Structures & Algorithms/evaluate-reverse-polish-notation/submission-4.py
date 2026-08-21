class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num = 0
        s = 0
        for ch in tokens:
            try:
                stack.append(int(ch))
            except:
                t1 = stack.pop()
                t2 = stack.pop()
                
                if (ch == "*"):
                    s = t1 * t2
                elif (ch == "+"):
                    s = t1 + t2
                elif (ch == "-"):
                    s = t2 - t1
                elif (ch == "/"):
                    s = int(t2 / t1)
                
                stack.append(s)
                
        return(stack.pop())
        

        