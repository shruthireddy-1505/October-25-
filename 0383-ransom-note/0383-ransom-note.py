class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key in ransomNote:
            if key not in d or d[key]==0:
                return False
            d[key]-=1
        return True
                