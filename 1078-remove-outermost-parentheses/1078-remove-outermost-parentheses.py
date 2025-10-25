class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        depth=0

        for i in s:
            if i=="(":
                if depth>0:
                    res+="("
                depth+=1
            else:
                depth-=1
                if depth >0:
                    res+=")"
        return res
            
        