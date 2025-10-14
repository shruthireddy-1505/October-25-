class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        h=n-1
        ans=float("inf")
        while l<=h:
            m=(l+h)//2
            if nums[l]<=nums[m]:
                if nums[l]<ans:
                    ans=nums[l]
                l=m+1
            elif nums[m]<=nums[h]:
                if nums[m]<ans:
                    ans=nums[m]
                h=m-1
        return ans
                