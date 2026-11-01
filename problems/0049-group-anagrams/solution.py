from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Optimal Hash Map with Sorted Key
        Time Complexity: O(n * k log k)
        Space Complexity: O(n * k)
        """
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


if __name__ == "__main__":
    solver = Solution()
    res = solver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort groups for deterministic comparison
    res_sorted = sorted([sorted(group) for group in res])
    expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert res_sorted == expected
    print("All test cases for Problem 49 (Group Anagrams) passed!")
