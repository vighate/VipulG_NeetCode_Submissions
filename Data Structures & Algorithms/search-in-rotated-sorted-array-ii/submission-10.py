class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # l = 0
        # r = len(nums)-1

        # while l<=r:
        #     mid = (l+r)//2

        #     if nums[mid] == target:
        #         return True
            
        #     if nums[l] == nums[mid] == nums[r]:
        #         l = mid+1
        #         r = mid-1

        #     elif nums[l] < nums[mid]:
        #         if nums[l] <= target < nums[mid]:
        #             r = mid-1
        #         else:
        #             l = mid+1
        #     else:
        #         if nums[mid] <= target < nums[r]:
        #             l = mid+1
        #         else:
        #             r = mid-1
                        
        # return False
        
        left = 0
        right = len(nums)-1


        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return False