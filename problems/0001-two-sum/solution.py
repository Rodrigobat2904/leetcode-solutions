from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Optimal Hash Map (One-Pass) Solution
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    solver = Solution()
    
    # Test cases
    assert solver.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solver.twoSum([3, 2, 4], 6) == [1, 2]
    assert solver.twoSum([3, 3], 6) == [0, 1]
    
    print("All test cases for Problem 1 (Two Sum) passed!")
