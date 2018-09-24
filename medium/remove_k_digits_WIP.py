"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # Convert to Ascending order
        # If already in ascending order, remove from back
        # Remove trailing zeros
        if k == 0:
            return num
        
        if len(num) == 0:
            return num
        
        if len(num) == k:
            return '0'
        
        count = 0
        remove_index = []
        num = list(num)
        
        for i in range(len(num)):
            if count >= k:
                break
            if i + 1 >= len(num):
                break
            if num[i] > num[i+1]:
                remove_index.append(i)
                count += 1
        
        print('remove_index: ', remove_index)
        
        for i in reversed(remove_index):
            print('DELETING num[{}]: {}'.format(i, num[i]))
            del num[i]
        
        for i in range(len(num) - 1, 0, -1):
            if count >= k:
                break
            if i - 1 < 0:
                break
            if num[i] < num[i-1]:
                del num[i-1]
                count += 1
        
        if count < k:
            for i in range(k - count):
                del num[-1]
                count += 1
        
        while (num and num[0] == '0'):
            del num[0]
        
        if not num:
            return '0'
        
        num = ''.join(num)
        return num
            
