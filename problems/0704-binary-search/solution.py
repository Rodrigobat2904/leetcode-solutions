from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Optimal Binary Search Solution
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


if __name__ == "__main__":
    solver = Solution()
    assert solver.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solver.search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("All test cases for Problem 704 (Binary Search) passed!")
