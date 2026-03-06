"""
Problem: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
Pattern: Linked List / Two Pointers
Date: 2026-03-06

Approach:
- Create a dummy node to simplify handling of the result linked list.
- Use a pointer `temp` to build the merged list.
- Traverse both linked lists simultaneously while both `list1` and `list2` are not empty.
- Compare the values of the current nodes of `list1` and `list2`.
- Attach the node with the smaller value to `temp.next`.
- Move the pointer of the selected list (`list1` or `list2`) forward.
- Move the `temp` pointer forward.
- After the loop ends, one list may still have remaining nodes.
- Attach the remaining portion of that list directly to `temp.next`.
- Return `dummy.next`, which points to the head of the merged sorted list.

Time Complexity: O(n + m)
Space Complexity: O(1)

Key Insight:
Both lists are already sorted, so we merge them by comparing nodes one by one.
Instead of creating new nodes, we reuse the existing nodes and rearrange pointers.
The dummy node helps avoid special handling for the head of the merged list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        while list1 and list2:
            if list2.val < list1.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            temp = temp.next
        if list1:
            temp.next = list1
            temp=temp.next
        if list2:
            temp.next = list2
            temp=temp.next
        return dummy.next

            
        

            