class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev