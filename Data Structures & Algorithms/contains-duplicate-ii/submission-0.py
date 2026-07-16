class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left = 0
        windows = set()
        for right in range(len(nums)):

            if nums[right] in windows:
                return True

            windows.add(nums[right])

            if right-left >= k:
                windows.remove(nums[left])
                left += 1

        return False