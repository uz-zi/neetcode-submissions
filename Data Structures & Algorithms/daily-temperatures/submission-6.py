class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        res = []
        for i in range(1,len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                    temperatures[stack[-1]] = i - stack[-1]
                    stack.pop()

            stack.append(i)
        
        while stack:
            temperatures[stack[-1]] = 0
            stack.pop()


        return temperatures 
            

        
                



        
        