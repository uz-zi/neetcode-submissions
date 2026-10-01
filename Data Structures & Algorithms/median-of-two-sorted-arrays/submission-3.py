class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2,nums1
        
        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while (left <= right):
            m1 = (left+right)//2
            m2 = (m+n)//2 - m1

            l1 = float("-inf") if m1 == 0 else nums1[m1-1]
            l2 = float("-inf") if m2 == 0 else nums2[m2-1]
            r1 = float("inf") if m1 == len(nums1) else nums1[m1]
            r2 = float("inf") if m2 == len(nums2) else nums2[m2]

            if l1 <= r2 and l2 <= r1:
                if (m+n) % 2 == 1:
                    return min(r1,r2)
                return (max(l1,l2)+min(r1,r2)) /2

            if l1 > r2:
                right = m1-1
            else:
                left = m1+1

            