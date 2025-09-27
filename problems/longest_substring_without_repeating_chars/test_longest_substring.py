from problems.longest_substring_without_repeating_chars import (
    find_length_from_longest_substring,
)


def test_longestSubstring_abc():
    full_string = "abcabcbb"

    lengthOfLongestSubstring = (
        find_length_from_longest_substring().lengthOfLongestSubstring(full_string)
    )

    assert (lengthOfLongestSubstring) == 3


def test_longestSubstring_b():
    full_string = "bbbbb"

    lengthOfLongestSubstring = (
        find_length_from_longest_substring().lengthOfLongestSubstring(full_string)
    )

    assert (lengthOfLongestSubstring) == 1


def test_longestSubstring_kew():
    full_string = "pwwkew"

    lengthOfLongestSubstring = (
        find_length_from_longest_substring().lengthOfLongestSubstring(full_string)
    )

    assert (lengthOfLongestSubstring) == 3


def test_longestSubstring_nolength():
    full_string = ""

    exception_msg = ""
    try:
        find_length_from_longest_substring().lengthOfLongestSubstring(full_string)
    except Exception as e:
        exception_msg = str(e)

    assert exception_msg == "The length of the string must not be zero or lower"


def test_longestSubstring_maxRange():
    full_string = "a" * (5 * 10**4)

    exception_msg = ""
    try:
        find_length_from_longest_substring().lengthOfLongestSubstring(full_string)
    except Exception as e:
        exception_msg = str(e)

    assert exception_msg == "The length of the string is too large"
