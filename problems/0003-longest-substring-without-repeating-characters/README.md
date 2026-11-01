# Problem 3: Longest Substring Without Repeating Characters

- **Difficulty:** Medium
- **Topics:** Hash Table, String, Sliding Window
- **LeetCode Link:** [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Approaches & Complexity

### Sliding Window with Hash Map / Set
Maintain a dynamic window `[left, right]`. As the `right` pointer expands:
1. If character `s[right]` was seen inside current window, slide `left` forward past its previous index.
2. Update the character's last seen index.
3. Track max window length `max(max_len, right - left + 1)`.

- **Time Complexity:** $O(n)$ — Each character is visited at most twice.
- **Space Complexity:** $O(\min(m, n))$ — Storing unique characters in the window.
