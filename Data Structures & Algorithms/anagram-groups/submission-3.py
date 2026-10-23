class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            word = ''.join(sorted(string))
            if word not in dic:
                dic[word] = []
            
            dic[word].append(string)

        return list(dic.values())
            
            
        