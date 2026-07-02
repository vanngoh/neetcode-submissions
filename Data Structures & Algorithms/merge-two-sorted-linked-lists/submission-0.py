# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # [1 -> 2 -> 4]             [1 -> 3 -> 5]
        #  ^                         ^
        #  p1                        p2             # compare p1 & p2
        # (set p1 to res)
        #
        # [1 -> 2 -> 4]             [1 -> 3 -> 5]
        #       ^                    ^
        #       p1                   p2             # compare p1 & p2
        #                      (set p2 to res)
        #
        # [1 -> 2 -> 4]             [1 -> 3 -> 5]
        #       ^                         ^
        #       p1                        p2        # compare p1 & p2
        # etc...
                
        # Default: [0]
        res = p_res = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                p_res.next = list1
                list1 = list1.next
            else:
                p_res.next = list2
                list2 = list2.next
            p_res = p_res.next

        # If either the ListNode is None(empty)
        # Set the other one to be the rest of it
        p_res.next = list1 or list2
        
        # Remove the first 0
        return res.next




