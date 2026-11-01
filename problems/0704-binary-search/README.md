# Problem 704: Binary Search

- **Difficulty:** Easy
- **Topics:** Array, Binary Search
- **LeetCode Link:** [LeetCode #704](https://leetcode.com/problems/binary-search/)

---

## Approaches & Complexity

### Two Pointers (Divide & Conquer)
Given sorted array, maintain `left = 0` and `right = len(nums) - 1`.
1. Calculate `mid = left + (right - left) // 2`.
2. If `nums[mid] == target`, return `mid`.
3. If `nums[mid] < target`, search right half: `left = mid + 1`.
4. If `nums[mid] > target`, search left half: `right = mid - 1`.
5. Return `-1` if not found.

- **Time Complexity:** $O(\log n)$ — Search space halves each step.
- **Space Complexity:** $O(1)$ — In-place pointer manipulation.
