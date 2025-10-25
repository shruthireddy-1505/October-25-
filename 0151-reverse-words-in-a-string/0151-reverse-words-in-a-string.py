class Solution:
    def reverseWords(self, s: str) -> str:
        string=s.split()
        n=len(string)
        l=0
        h=n-1
        while l<h:
            string[l],string[h]=string[h],string[l]
            l+=1
            h-=1
        res=" ".join(string)
        return res
                