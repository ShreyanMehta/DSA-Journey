"""
Problem: Middle of the Linked List
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Difficulty: Easy
Pattern: Linked List (Fast–Slow Pointer)
Date: 2026-03-03

Approach:
- initialize two pointers: fast and slow (2 pointer approach)
- fast = head
  slow = head
- slow moves 1 step while fast moves 2 steps
- when fast reaches end, slow is in middle
- return slow

Time Complexity: O(n)
Space Complexity: O(1)

Key Insight:
It is better to use 2 pointer approach instead of iterating through list 2 times
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow