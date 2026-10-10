class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        cap = 0
        maxcap = 0

        while l < r:
            if heights[l] < heights[r]:
                cap = heights[l]*(r-l)
                l+=1
            elif heights[l] > heights[r]:
                cap = heights[r]*(r-l)
                r-=1
            else:
                cap = heights[r]*(r-l)
                r-=1
                l+=1
            
            maxcap = max(cap,maxcap)

        return maxcap


            
            

