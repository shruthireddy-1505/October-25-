class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        from math import ceil
        l=1
        h=max(nums)
        while l<=h:
            mid=(l+h)//2
            s=0
            for i in nums:
                s+=ceil(i/mid)
            if s<=threshold:
                h=mid-1
            else:
                l=mid+1
        return l
                