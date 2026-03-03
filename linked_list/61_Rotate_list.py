"""
Problem: Rotate List  
Link: https://leetcode.com/problems/rotate-list/  
Difficulty: Medium  
Pattern: Linked List  
Date: 2026-03-03  

Approach:
- Handle edge cases (empty list / single node / k = 0)
- Traverse once to calculate length (n) and get tail
- Reduce rotations using k = k % n
- If k == 0, return head
- Connect tail → head to form circular list
- Walk (n - k - 1) steps from head to reach new tail
- New head = new_tail.next
- Break circular link

Time Complexity: O(n)  
Space Complexity: O(1)  

Key Insight:
Rotating right by k is equivalent to shifting the starting point of the list.
Instead of moving nodes one by one, convert the list into a circular structure and 
redefine the breaking point at (n - k - 1).
The operation is pointer manipulation, not data shifting.
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        count = 1
        ptr = head
        while head and ptr.next:
            ptr = ptr.next
            count = count + 1
        k=k%count
        ptr.next = head
        current = head 
        for _ in range(count-k-1):
            current = current.next
        new_head = current.next
        current.next = None
        return new_head
