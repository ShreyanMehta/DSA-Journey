"""
Problem: Delete Node in a Linked List
Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
Difficulty: Medium
Pattern: Linked List
Date: 2026-03-02

Approach:
- Cannot access head
- Copy next node's value
- Skip next node

Time Complexity: O(1)
Space Complexity: O(1)

Key Insight:
Deletion without previous pointer requires overwriting.
Node to be deleted is not last node. The node is not being deleted from memory but its now just not part of the linked list.
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val

        node.next = node.next.next
