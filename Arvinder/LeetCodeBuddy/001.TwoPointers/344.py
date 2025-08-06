
"""
🌟 LeetCode Problem: 344 — Reverse String

🔍 Problem Statement:
Write a function that reverses a string. The input string is provided 
as a list of characters `s`. You must reverse the string **in-place**, 
using only **O(1)** extra memory.

📥 Input:
- A list of characters: s = ["h", "e", "l", "l", "o"]

📤 Output:
- The same list reversed in-place: ["o", "l", "l", "e", "h"]

🎯 Requirements:
- Modify the original list (no new list should be created)
- Use constant extra memory (O(1))

💡 Examples:
Example 1:
Input  : ["h", "e", "l", "l", "o"]
Output : ["o", "l", "l", "e", "h"]

Example 2:
Input  : ["H", "a", "n", "n", "a", "h"]
Output : ["h", "a", "n", "n", "a", "H"]

📌 Constraints:
- 1 <= len(s) <= 10^5
- Each element `s[i]` is a printable ASCII character
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
        

