class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []

        self.dic[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        else:
            arr = self.dic[key]

            l = 0
            r = len(arr)-1
            ans = ""

            while( l<=r):
                mid = (l+r)//2

                if(arr[mid][0] <= timestamp):
                    ans = arr[mid][1]
                    l = mid+1
                else:
                    r = mid -1

        return ans        
