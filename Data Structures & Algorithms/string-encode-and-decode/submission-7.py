class Solution:

    def encode(self, strs: List[str]) -> str:
        tempstr = ""

        for st in strs:
            tempstr += str(len(st))+ "#"+st
        
        return tempstr
       
            
    def decode(self, s: str) -> List[str]:
        temp = []
        i =0
        while(i < len(s)):
            j = i
            while(s[j] != '#'):
                j+=1
            length = int(s[i:j])
            temp.append(s[j+1:j+1+length])
            i = j+1+length

        return temp
        
            


