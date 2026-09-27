class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        water = 0
        dis = 0
        maxwater = 0
        while l < r:
            dis = r - l
            if heights[l] < heights[r]:
                water = heights[l]*dis
                l+=1
            elif heights[l] > heights[r]:
                water = heights[r]*dis
                r-=1
            else:
                water = heights[l]*dis
                r-=1
                l+=1
            maxwater = max(water, maxwater)

        return maxwater



        