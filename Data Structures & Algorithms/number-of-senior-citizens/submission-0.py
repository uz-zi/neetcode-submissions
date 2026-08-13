class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for string in details:
            age = int(string[11:13])
            count +=1 if age > 60 else 0

        return count
                
        