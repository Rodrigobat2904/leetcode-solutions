class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Optimal Sliding Window Solution
        Time Complexity: O(n)
        Space Complexity: O(min(m, n))
        """
        char_map = {}
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length


if __name__ == "__main__":
    solver = Solution()
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3
    assert solver.lengthOfLongestSubstring("bbbbb") == 1
    assert solver.lengthOfLongestSubstring("pwwkew") == 3
    assert solver.lengthOfLongestSubstring("") == 0
    print("All test cases for Problem 3 (Longest Substring) passed!")
