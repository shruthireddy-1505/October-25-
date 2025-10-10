class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        ans=[-1,-1]
        l=0
        h=n-1
        while l<=h:
            m=(l+h)//2
            if nums[m]>=target:
                h=m-1
            else:
                l=m+1
        if l<n and nums[l]==target:
            ans[0]=l

        l=0
        h=n-1
        while l<=h:
            m=(l+h)//2
            if nums[m]<=target:
                l=m+1
            else:
                h=m-1
        if h>=0 and nums[h]==target:
            ans[1]=h
        return ans