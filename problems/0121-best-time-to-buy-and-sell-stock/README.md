# Problem 121: Best Time to Buy and Sell Stock

- **Difficulty:** Easy
- **Topics:** Array, Dynamic Programming
- **LeetCode Link:** [LeetCode #121 - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the *maximum profit* you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
```

### Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

---

## Approaches & Complexity

### One Pass (Tracking Minimum Price) - Optimal
Track the minimum price seen so far as we iterate through the days. The potential profit on day $i$ is `prices[i] - min_price`. Update maximum profit accordingly.

- **Time Complexity:** $O(n)$ — Single traversal of prices.
- **Space Complexity:** $O(1)$ — Only constant variables stored.
