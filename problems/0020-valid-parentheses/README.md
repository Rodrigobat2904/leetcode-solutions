# Problem 20: Valid Parentheses

- **Difficulty:** Easy
- **Topics:** String, Stack
- **LeetCode Link:** [LeetCode #20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example 1:
```
Input: s = "()"
Output: true
```

### Example 2:
```
Input: s = "()[]{}"
Output: true
```

### Example 3:
```
Input: s = "(]"
Output: false
```

### Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

---

## Approaches & Complexity

### Stack - Optimal
Use a LIFO (Last-In-First-Out) stack:
1. When encountering an opening bracket `(`, `{`, `[`, push the corresponding closing bracket `)`, `}`, `]` to the stack.
2. When encountering a closing bracket, pop from the stack and verify that it matches.
3. If the stack is empty before popping or elements don't match, string is invalid.
4. At the end, the stack must be empty.

- **Time Complexity:** $O(n)$ — Single pass over string of length $n$.
- **Space Complexity:** $O(n)$ — Stack can hold up to $n$ characters in the worst case (all open brackets).
