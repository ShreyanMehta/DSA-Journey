"""
Problem: Remove Element
Link: https://leetcode.com/problems/remove-element/
Difficulty: Easy
Pattern: Array
Date: 2026-03-05

Approach:
- Traverse the array from start to end.
- If an element equals val, replace it with 0.
- If the element is not equal to val, increment a counter.
- After traversal, sort the array in reverse order so that all zero values move to the end.
- Return the counter which represents the number of elements not equal to val.

Time Complexity: O(n log n)   (due to sorting)
Space Complexity: O(1)

Key Insight:
Instead of directly deleting elements from the array, replace the unwanted values and push them to the end using sorting. The count of non-val elements gives the required result length.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]=0
            else:
                count +=1
        nums = nums.sort(reverse=True)
        return count
            
