"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
{
  a: 2,
  b: 4,
  c: 2
}

abc
bca
cab
abc
bc
cb
b
b

MAX: 3


Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

abcdefghijklmnopqrstuvwxyz
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_to_count = {}

        for index, letter in enumerate(s):
            if letter not in letter_to_count:
                letter_to_count[letter] = 0
            else:
                letter_to_count[letter] += 1


