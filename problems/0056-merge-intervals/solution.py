from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Optimal Sort and Sweep Solution
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not intervals:
            return []
            
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        
        for curr in intervals[1:]:
            prev = merged[-1]
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(curr)
                
        return merged


if __name__ == "__main__":
    solver = Solution()
    assert solver.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solver.merge([[1, 4], [4, 5]]) == [[1, 5]]
    print("All test cases for Problem 56 (Merge Intervals) passed!")
