class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(spells)
        m=len(potions)
        res=[0]*n

        for i in range(0,n):
            l=0
            h=m-1
            while l<=h:
                mid=(l+h)//2
                temp=spells[i]*potions[mid]
                if temp>=success:
                    ans=m-mid
                    res[i]=ans
                    h=mid-1
                else:
                    l=mid+1
        return res
        