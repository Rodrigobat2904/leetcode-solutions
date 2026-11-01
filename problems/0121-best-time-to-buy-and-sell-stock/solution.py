from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Optimal One-Pass Solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit


if __name__ == "__main__":
    solver = Solution()
    assert solver.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solver.maxProfit([7, 6, 4, 3, 1]) == 0
    print("All test cases for Problem 121 (Best Time to Buy and Sell Stock) passed!")
