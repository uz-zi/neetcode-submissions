class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            dis = math.sqrt(points[i][0]**2 + points[i][1]**2)
            heap.append([dis,points[i]])

        heapq.heapify(heap)

        res = []

        for i in range(k):
            point = heapq.heappop(heap)
            res.append(point[1])

        return res


            


        

        