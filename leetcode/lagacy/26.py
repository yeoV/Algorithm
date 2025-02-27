# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    # 초기답안 : 1 부터 비교할 필요가 없는데 쓸데 없는 연산이 들어감
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     unique = 0
    #     for idx in range(len(nums)):
    #         if nums[unique] != nums[idx]:
    #             unique += 1
    #             nums[unique] = nums[idx]
    #     return unique + 1
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        for idx in range(1, len(nums)):  # 굳이 1은 비교할  필요가 없음
            if nums[unique] != nums[idx]:
                unique += 1
                nums[unique] = nums[idx]
        return unique + 1


Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
