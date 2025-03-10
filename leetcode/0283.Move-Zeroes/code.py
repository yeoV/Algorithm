from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1

        for i in range(left, len_nums):
            nums[i] = 0

if __name__ == "__main__":
    Solution().moveZeroes([0,1,0,3,12])
    Solution().moveZeroes([0])