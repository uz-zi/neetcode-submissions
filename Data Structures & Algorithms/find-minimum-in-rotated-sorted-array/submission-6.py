class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        mini = nums[0]
        r = len(nums)-1
        while(l <= r):
            mid = (l+r)//2
        
            if (nums[l] <= nums[mid]):
                mini = min(nums[l], mini)
                l = mid+1
            else:
                mini = min(nums[mid], mini)
                r = mid-1
            
        
        return mini


        