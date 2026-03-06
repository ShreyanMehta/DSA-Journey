"""
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium
Pattern: Linked List / Simulation
Date: 2026-03-06

Approach:
- Create a dummy node to simplify handling of the result list.
- Use a pointer `temp` to build the new linked list.
- Maintain a variable `carry` to store carry from digit addition.
- Traverse both linked lists simultaneously until both lists and carry become zero.
- Extract values from current nodes of `l1` and `l2`. If a list is exhausted, treat its value as 0.
- Compute the sum of the digits and carry.
- Update carry using integer division by 10.
- Store the current digit using modulo 10.
- Create a new node with this digit and attach it to the result list.
- Move the pointers of `l1`, `l2`, and the result list forward.
- Return `dummy.next` which points to the head of the result list.

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

Key Insight:
The numbers are stored in reverse order in the linked lists, so addition can be performed exactly like manual digit-by-digit addition from least significant digit to most significant digit. A dummy node helps avoid special handling for the head of the result list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry =  0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            temp.next = ListNode(val)

            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


            
            
