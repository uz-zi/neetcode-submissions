class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = ('a','e','i','o','u')
        res = []
        count = 0
        for li, ri in queries:
            i = li
            while i <= ri:
                if words[i][0] in s and words[i][-1] in s:
                    count +=1
                i+=1
            
            res.append(count)
            count = 0

        return res


        