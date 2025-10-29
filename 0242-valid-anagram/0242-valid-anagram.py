class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m={}
        for i in t:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        for i in range(len(s)):
            ch=s[i]
            if ch in m:
                if d[ch]!=m[ch]:
                    return False
            else:
                return False
        else:
            return True
            