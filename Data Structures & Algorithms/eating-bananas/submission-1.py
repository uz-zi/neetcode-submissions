
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        result = j
        
        while( i <= j):
            mid = (i+j)//2
            
            ans = 0
            for num in piles:
                ans += math.ceil(num / mid)
            
            if ans <= h:
                j = mid -1
            else:
                i = mid +1
        
        return i
        