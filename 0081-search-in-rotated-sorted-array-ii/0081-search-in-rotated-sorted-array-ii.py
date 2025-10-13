class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        l=0
        h=n-1
        while l<=h:
            m=(l+h)//2
            if nums[m]==target:
                return True
            if nums[l]==nums[m]==nums[h]:
                l+=1
                h-=1
            elif nums[l]<=nums[m]:
                if nums[l]<=target<=nums[m]:
                    h=m-1
                else:
                    l=m+1
            elif nums[m]<=nums[h]:
                if nums[m]<=target<=nums[h]:
                    l=m+1
                else:
                    h=m-1
        return False
                