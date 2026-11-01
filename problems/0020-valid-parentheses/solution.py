class Solution:
    def isValid(self, s: str) -> bool:
        """
        Optimal Stack Solution
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack


if __name__ == "__main__":
    solver = Solution()
    assert solver.isValid("()") is True
    assert solver.isValid("()[]{}") is True
    assert solver.isValid("(]") is False
    assert solver.isValid("([)]") is False
    assert solver.isValid("{[]}") is True
    print("All test cases for Problem 20 (Valid Parentheses) passed!")
