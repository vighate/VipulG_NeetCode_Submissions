class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        res = []

        

        for num in nums:
            l = 0
            r = len(res)-1
            while l <= r:
                mid = (l+r)//2

                if res[mid] > num:
                    r = mid-1
                else:
                    l = mid+1
            
            res.insert(l, num)

        return res

