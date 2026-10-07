class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        ans = []
        
        for num in nums1:
            ans.append(num)
        
        for num in nums2:
            ans.append(num)

        res = []
        median = 0

        for num in ans:

            left = 0
            right = len(res)

            while left < right:
                mid = (left+right)//2

                if res[mid] <= num:
                    right = mid
                else:
                    left = mid+1
            
            res.insert(left, num)

            n = len(res)
            if n%2 == 0:
                median = (res[n//2-1]+res[n//2])/2
            else:
                median = res[n//2]

        return median


        
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