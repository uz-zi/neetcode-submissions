import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        s = 0
        while k >= 1:
            n = math.isqrt(-heapq.heappop(gifts))
            heapq.heappush(gifts, -n)
            k-=1

        while gifts:
            s += (-gifts.pop())

        return s

            



        