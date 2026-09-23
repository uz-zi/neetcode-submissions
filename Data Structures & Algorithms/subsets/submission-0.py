class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def subset(i, cur):
            if i == n:
                ans.append(cur[:])
                return

            cur.append(nums[i])
            subset(i+1,cur)
            cur.pop()
            subset(i+1,cur)

        subset(0,[])

        return ans
            
                


        