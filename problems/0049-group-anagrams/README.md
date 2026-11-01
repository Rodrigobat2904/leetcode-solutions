# Problem 49: Group Anagrams

- **Difficulty:** Medium
- **Topics:** Array, Hash Table, String, Sorting
- **LeetCode Link:** [LeetCode #49](https://leetcode.com/problems/group-anagrams/)

---

## Approaches & Complexity

### Categorize by Sorted String or Character Count
1. For each string, sort characters as a canonical key (e.g. `"eat"` -> `"aet"`).
2. Append the original string into a hash map bucket `dict[key].append(string)`.
3. Return list of all dictionary values.

- **Time Complexity:** $O(n \cdot k \log k)$ where $k$ is max length of string.
- **Space Complexity:** $O(n \cdot k)$ to store grouped words in map.
