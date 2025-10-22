class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=s.lower()
        temp=""
        for i in string:
            if i.isalnum():
                temp+=i
        if temp==temp[::-1]:
            return True
        else:
            return False
        