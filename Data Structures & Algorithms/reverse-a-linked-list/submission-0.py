# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Use the 2-pointers approach
        # None    [0  -> 1  -> 2  -> None]
        #  ^       ^
        # prev    curr

        # None    [0  -> 1  -> 2  -> None]
        #          ^     ^
        #         prev  curr
        # [None <- 0]

        # None    [0  -> 1  -> 2  -> None]
        #                ^     ^
        #               prev  curr
        # [None <- 0  <- 1]

        # None    [0  -> 1  -> 2  -> None]
        #                      ^     ^
        #                     prev  curr(**STOP**)
        # [None <- 0  <- 1  <- 2] <--- **ANS**
        
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        
