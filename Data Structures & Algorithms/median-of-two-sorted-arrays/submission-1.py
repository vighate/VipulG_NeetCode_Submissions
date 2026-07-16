class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        res = []

        for i in range(len(nums1)):
            res.append(nums1[i])

        for k in range(len(nums2)):
            res.append(nums2[k])

        res = sorted(res)

        ans = 0

        n = len(res)
        print(n//2)
        if n%2 == 0:
            ans = (res[n//2-1] + res[n//2])/2
        else:
            ans = res[n//2]

        return ans