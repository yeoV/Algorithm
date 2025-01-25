# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # not match
        for idx, v in enumerate(nums):
            if v == val:
                nums[idx] = "_"
            else:
                k += 1

        idx, cnt = 0, 0
        while cnt < len(nums):
            if nums[idx] != "_":
                idx += 1
            else:
                temp = nums.pop(idx)
                nums.append(temp)
            cnt += 1
        return k


Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
