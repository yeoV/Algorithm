# My solve
# 공간복잡도 : O(n) -> 낭비가 많음 / 시간 복잡도 O(1)
from typing import List


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = dict()
        result = set()
        n = len(nums) / 2
        for val in nums:
            count_map[val] = count_map.get(val, 0) + 1
            if count_map[val] > n:
                result.add(val)
        return result.pop()


# Boyer-Moore Majority Vote Algorithm -> 뭔가 후보자를 선정해서 하나씩. 더하거나 빼면서 가는 느낌
class Solution2:
    def majorityElement(self, nums: List[int]) -> None:
        candidate, count = None, 0
        for val in nums:
            if count == 0:
                candidate = val
            count += 1 if candidate == val else -1

        return candidate  # type: ignore


Solution2().majorityElement(nums=[3, 2, 3, 2, 1, 2])  # 해당 케이스 주의
