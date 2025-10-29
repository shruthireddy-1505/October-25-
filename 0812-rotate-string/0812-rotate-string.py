class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        n=len(s)
        for i in range(n-1,-1,-1):
            s=s[n-1]+s[:n-1]
            if s==goal:
                return True
        else:
            return False
            
        