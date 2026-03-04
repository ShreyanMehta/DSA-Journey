"""
Problem: Remove Nth Node From End of List  
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
Difficulty: Medium  
Pattern: Linked List  
Date: 2026-03-04  

Approach:
- Traverse the list once to calculate total length (count)
- If n == count, remove the head node by returning head.next
- Otherwise, traverse again to reach (count - n - 1)th node
- This node is just before the one to be deleted
- Update temp.next = temp.next.next to skip the target node
- Return head

Time Complexity: O(n)  
Space Complexity: O(1)  

Key Insight:
Although the problem can be solved using two pointers in one pass,
this approach uses a length-based method.
By first calculating total nodes, we convert the problem into 
removing the (count - n)th node from the beginning.
The deletion is performed by bypassing the target node using pointer reassignment.
The core idea is identifying the node just before the one to remove.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count = count + 1
            temp=temp.next
        if n==count:
            return head.next
        temp=head   
        for _ in range(count-n-1):
            temp=temp.next
        temp.next=temp.next.next
        return head