class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
        # left = 0 
        # right = len(nums)-1

        # while left <= right:

        #     mid = (left+right)//2

        #     if nums[mid] == target:
        #         return mid
            
        #     if nums[left] <= nums[mid]:

        #         if nums[left] <= target < nums[mid]:
        #             right = mid-1
        #         else:
        #             left = mid+1

        #     else:
        #         if nums[mid] < target <= nums[right]:
        #             left = mid+1
        #         else:
        #             right = mid-1

        # return -1



        
        # # l = 0
        # # r = len(nums)-1

        # # while l<=r:
        # #     mid = (l+r)//2

        # #     if nums[mid] == target:
        # #         return mid

        # #     if nums[l] <= nums[mid]:
        # #         if nums[l] <= target < nums[mid]:
        # #             r = mid-1
        # #         else:
        # #             l = mid+1
            
        # #     else:
        # #         if nums[mid] < target <= nums[r]:
        # #             l = mid+1
        # #         else:
        # #             r = mid-1

        # # return -1

        # # l = 0
        # # r = len(nums)-1

        # # if target not in nums:
        # #     return -1

        # # while l<=r:

        # #     mid = (l+r)//2

        # #     if nums[mid] == target:
        # #         return mid

        # #     if nums[mid] >= nums[l]:
        # #         if nums[l] <= target < nums[mid]:
        # #             r = mid-1
        # #         else:
        # #             l = mid+1
            
        # #     if nums[mid] <= nums[r]:
        # #         if nums[mid] < target <= nums[r]:
        # #             l = mid+1
        # #         else:
        # #             r = mid-1


