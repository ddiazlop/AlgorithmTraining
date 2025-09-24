"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);



Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"



Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

"""

import math


class Solution:
    def _validateInput(self, s, numRows):
        if not isinstance(s, str):
            raise TypeError("s must be a string")

        if not isinstance(numRows, int):
            raise TypeError("numRows must be an integer")

        if numRows < 0:
            raise ValueError("numRows must be positive")

    # def convert(self, s: str, numRows: int) -> str:
    #     # Guess how many letters should be in each line.
    #     # first column = numRows numbers
    #     # second column = 1 number
    #     # 2 types of columns ->  FULL, SINGLE.
    #     # Number of single columns after a full -> numrows - 2 (We skip first and last)
    #     # Approach 1: Create 2 arrays, 1 array with all of the full columns, and a second array with the single number columns, then mix both.
    #     # First we're going to create the solution string and then we can iterate to print it out.

    #     self._validateInput(s, numRows)

    #     zigZaggedString = ""
    #     fullColumns = []
    #     singleColumns = []
    #     pointer = 0
    #     while pointer < len(s):
    #         fullColumns.append(s[pointer : pointer + numRows])
    #         singleColumns.append(
    #             s[pointer + numRows : pointer + numRows + math.ceil(numRows / 2)]
    #         )

    #         pointer = pointer + numRows + numRows / 2
    #         # Here I should have both types of columns ready, and I just need to mix them

    #     print(singleColumns)
    #     print(fullColumns)

    #     return zigZaggedString

    # Going up and down was much simpler
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        print(rows)
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return "".join(rows)


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 4))
