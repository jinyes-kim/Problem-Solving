# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = collections.deque()
        
        if not head:
            return True
        
        node = head
        while node is not None:
            queue.append(node.val)
            node = node.next
        
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        return True
        