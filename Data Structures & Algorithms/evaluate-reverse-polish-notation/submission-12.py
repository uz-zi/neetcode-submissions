class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            try:
                stack.append(int(ch))
            except:
                num1 = stack.pop()
                num2 = stack.pop()

                if ch == '*':
                    num1 *= num2
                elif ch == '+':
                    num1 += num2
                elif ch == '-':
                    num1 = num2 -num1
                elif ch == '/':
                    num1 = int(num2 / num1)
                
                stack.append(num1)

        return stack[-1]
            