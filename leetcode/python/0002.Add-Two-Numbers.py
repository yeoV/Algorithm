# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 3 ms Beats 72.93%
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        s_l1, s_l2 = [l1.val], [l2.val]
        while l1.next:
            s_l1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            s_l2.append(l2.next.val)
            l2 = l2.next

        # print("".join(s_l1[::-1]) + "".join(s_l2[::-1]))
        l1_val = int("".join(map(str, s_l1[::-1])))
        l2_val = int("".join(map(str, s_l2[::-1])))

        result_val = list(map(int, str(l1_val + l2_val)[::-1]))
        result = [ListNode(result_val[0])]

        for idx in range(1, len(result_val)):
            nxt_node = ListNode(result_val[idx])
            result[idx - 1].next = nxt_node
            result.append(nxt_node)
        return result[0]


# 1ms Beats 82.75%
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        n1, n2, carry, point = 0, 0, 0, res
        
        while l1 or l2 or carry:
            if l1:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0
            if l2:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0
            point.next = ListNode(int((n1 + n2 + carry) % 10))
            carry = (n1 + n2 + carry) // 10
            point = point.next

        return res.next