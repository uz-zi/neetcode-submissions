class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ('[','(','{'):
                stack.append(ch)
            elif ch in ('}',')',']'):
                if not stack:
                    return False
                top = stack.pop() 
                if (top == '{' and ch == '}' or
                    top == '(' and ch == ')' or
                    top == '[' and ch == ']'):
                    continue
                return False  
            else:
                return False
            
        if stack:
            return False
        return True


        