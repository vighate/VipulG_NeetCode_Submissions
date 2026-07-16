class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n = len(nums1)
        m = len(nums2)

        res = []

        for i in range(len(nums1)):
            res.append(nums1[i])

        for j in range(len(nums2)):
            res.append(nums2[j])

        res = sorted(res)
        print(res)

        if len(res)%2 != 0:
            return res[len(res)//2]
        else:
            return (res[len(res)//2-1] + res[len(res)//2])/2

        return -1