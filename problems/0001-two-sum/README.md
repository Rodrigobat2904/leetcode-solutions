# Problem 1: Two Sum

- **Difficulty:** Easy
- **Topics:** Array, Hash Table
- **LeetCode Link:** [LeetCode #1 - Two Sum](https://leetcode.com/problems/two-sum/)

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have ***exactly one solution***, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints:
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

---

## Approaches & Complexity

### Hash Map (One-Pass) - Optimal
Instead of checking all pairs with a brute-force $O(n^2)$ nested loop, we can use a hash map to remember numbers we have seen so far along with their indices.

For every number $x$ at index $i$:
1. Calculate the complement: `complement = target - x`.
2. Check if `complement` exists in the hash map.
3. If it exists, return `[hash_map[complement], i]`.
4. Otherwise, save `hash_map[x] = i` and proceed.

- **Time Complexity:** $O(n)$ — Single pass through the array, with average $O(1)$ dictionary lookups.
- **Space Complexity:** $O(n)$ — Storing at most $n$ elements in the hash map.
