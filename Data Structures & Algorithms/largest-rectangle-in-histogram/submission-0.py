class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pse = [0]*len(heights)
        nse = [0]*len(heights)
        stack = []

        for i in range(len(heights)):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                pse[i] = -1
            else:
                pse[i] = stack[-1]

            stack.append(i)
        
        stack = []
        for i in range(len(heights)-1,-1,-1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                nse[i] = len(heights)
            else:
                nse[i] = stack[-1]

            stack.append(i)

        maxi = 0
        for i in range(len(heights)):
            maxi = max(maxi, heights[i]*(nse[i] - pse[i] -1))

        return maxi
                

            
        