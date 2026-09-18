class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        res = []

        for i in range(len(points)):
            dis = math.sqrt(points[i][0]**2 + points[i][1]**2)

            dic[i] = dis

        index = sorted(dic, key=dic.get)

        for i in range(k):
            res.append(points[index[i]])

        return res
            


        

        