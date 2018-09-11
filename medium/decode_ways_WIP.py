"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
-
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
-
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
import sys


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        decode_count = 1
        consecutive_nums = 0
        # DICT: {consecutive_num: count}
        fib_dict = {}
        """
        Good nums: 
        1: 0-9
        2: 0-6

        Good consecutives: 
        1, 2, (0-6)
        """
        for i in range(len(s)):
            # REALLY GOOD INTS
            if s[i] in ['1', '2'] and len(s) is not 1:
                # ADD TO CONSECUTIVE NUMS NO PRECLUSION
                consecutive_nums += 1
                print('1 or 2')
            elif int(s[i]) in range(3, 7) and s[i-1] in ['1', '2']:
                # ADD TO CONSECUTIVE NUMS IF PREVIOUS NUM IS 1 OR 2
                consecutive_nums += 1
                print('3-6 with 1 or 2 before')
            elif int(s[i]) in range(7-10) and s[i-1] is '1':
                # ADD TO CONSECUTIVE NUMS IF PREVIOUS NUM IS 1
                consecutive_nums += 1
                print('7-9 with 1 before')
            elif int(s[i]) is 0 and len(s) is 1:
                return 0
            else:
                # ADD CONSECUTIVE NUMS TO DICT
                # RESET CONSECUTIVE NUMS
                print('NEITHER')
                if consecutive_nums not in fib_dict:
                    fib_dict[consecutive_nums] = 1
                else:
                    fib_dict[consecutive_nums] += 1
                consecutive_nums = 0

            if i is len(s) - 1:
                if consecutive_nums not in fib_dict:
                    fib_dict[consecutive_nums] = 1
                else:
                    fib_dict[consecutive_nums] += 1
                consecutive_nums = 0


        for consecutive_num in fib_dict.keys():
            decode_count += (self.fib(consecutive_num) * fib_dict[consecutive_num])

        return decode_count

    def fib(self, n, computed = {0: 0, 1: 1}):
        if n not in computed:
            computed[n] = self.fib(n-1, computed) + self.fib(n-2, computed)
        return computed[n]


def main(args):
    sol = Solution()
    print('solution: ', sol.numDecodings(args[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
