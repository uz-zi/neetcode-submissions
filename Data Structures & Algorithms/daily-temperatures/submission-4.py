class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = 1
        stack.append(0)
        while(i < len(temperatures)):
            if temperatures[i] > temperatures[stack[-1]]:
                while(stack and temperatures[stack[-1]] < temperatures[i]):
                    temperatures[stack[-1]] = i - stack[-1]
                    stack.pop()
            
            stack.append(i)
            
            i+=1

        while(stack):
            temperatures[stack[-1]] = 0
            stack.pop()

        return temperatures
            
            
            

