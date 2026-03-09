"""
Problem: Palindrome Linked List
Link: https://leetcode.com/problems/palindrome-linked-list/
Difficulty: Easy
Pattern: Linked List / Stack
Date: 2026-03-09

Approach:
- If the linked list has only one node, return True.
- Create an empty list (stack1) to store node values.
- Traverse the linked list using a temporary pointer.
- Append each node's value to stack1.
- After traversal, compare stack1 with its reversed version.
- If both are equal, return True.
- Otherwise, return False.

Time Complexity: O(n)
- One traversal to store values.
- One comparison with reversed list.

Space Complexity: O(n)
- Extra space is used to store node values in a list.

Key Insight:
A palindrome reads the same forward and backward.
Instead of modifying the linked list, we store its values
and check whether the list equals its reverse.
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        stack1 = []
        temp =  head
        while temp:
            stack1.append(temp.val)
            temp = temp.next
        if stack1[::-1] == stack1:
            return True
        else:
            return False
            
