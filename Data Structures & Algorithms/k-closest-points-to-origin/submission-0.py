class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        res = []
        for i in range(len(points)):
            dis = math.sqrt((0-points[i][0])**2 + (0-points[i][1])**2)
            dic[i] = dis

        keys = sorted(dic, key=dic.get)

        res = []
        for i in range(k):
            res.append(points[keys[i]])

        return res
            


        

        