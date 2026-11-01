# Problem 56: Merge Intervals

- **Difficulty:** Medium
- **Topics:** Array, Sorting
- **LeetCode Link:** [LeetCode #56](https://leetcode.com/problems/merge-intervals/)

---

## Approaches & Complexity

### Sort by Start Time & Sweep Line
1. Sort intervals by start value: `intervals.sort(key=lambda x: x[0])`.
2. Iterate through sorted intervals:
   - If merged list is empty or current interval does not overlap with previous (`curr.start > prev.end`), append it.
   - Else, merge by updating end: `prev.end = max(prev.end, curr.end)`.

- **Time Complexity:** $O(n \log n)$ due to sorting.
- **Space Complexity:** $O(n)$ for storing merged intervals.
