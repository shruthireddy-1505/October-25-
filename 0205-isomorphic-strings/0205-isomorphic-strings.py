class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        m={}
        for i in range(len(s)):
            ch=s[i]
            ch1=t[i]
            if ch in d:
                if ch1!=d[ch]:
                    return False
            if ch1 in m:
                if m[ch1]!=ch:
                    return False
            d[ch]=ch1
            m[ch1]=ch
        else:
            return True