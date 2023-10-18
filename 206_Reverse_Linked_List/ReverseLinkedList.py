# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        pre = None
        now = head
        while now:
            next_node = now.next
            now.next = pre 
            pre = now
            now = next_node
        return pre