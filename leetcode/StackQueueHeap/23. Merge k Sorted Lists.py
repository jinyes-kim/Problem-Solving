# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = pivot = ListNode()
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            pivot.next = node[2] # current node insert
            pivot = pivot.next # update pivot to current node
            
            if pivot.next: # exsist next node 
                heapq.heappush(heap, (pivot.next.val, idx, pivot.next))
                               
        return root.next
                               