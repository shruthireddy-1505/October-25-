class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}

        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=""

        for key,value in d.items():
            if d[key]==1:
                res=key
                break
        index=-1
        for i in range(len(s)):
            if res==s[i]:
                index=i
                break
        return index
                