# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        pre = None
        res = 0
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp 
        while slow:
            res = max(res, pre.val+slow.val)
            slow = slow.next
            pre = pre.next
        return res