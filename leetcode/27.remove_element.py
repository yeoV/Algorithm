# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[count] = nums[idx]
                count += 1
        return count


Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
