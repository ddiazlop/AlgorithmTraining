"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def validateInput(self, s):
        if len(s) <= 0:
            raise ValueError("The length of the string must not be zero or lower")
        if len(s) >= 5 * 10**4:
            raise ValueError("The length of the string is too large")

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """

        self.validateInput(s)

        substrings = []
        i = 0

        # O(k) complexity.
        # k -> length of each substring.
        for char in s:
            if len(substrings) <= i:
                substrings.append([])

            curr_substring = substrings[i]

            if char not in curr_substring:
                curr_substring += char
            else:
                i += 1

        # Worst-case scenario len(s) substrings are created -> O(n**2) complexity.
        return len(max(substrings, key=len))

    def lengthOfLongestSubstring(self, s):
        self.validateInput(s)
        char_index = {}
        # Chained assignment
        max_length = start = 0

        # O(n) time complexity
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length
