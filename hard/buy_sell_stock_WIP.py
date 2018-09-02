"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
import sys


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        if not prices:
            return max_profit

        min_stock = prices[0]
        min_stock_idx = 0
        max_stock = 0
        max_stock_idx = None

        for i in range(len(prices)):
            price = prices[i]
            if price <= min_stock:
                min_stock = price
                min_stock_idx = i
                max_stock = 0
                max_stock_idx = None
            if price >= max_stock and i > min_stock_idx:
                max_stock = price
                max_stock_idx = i
            if max_stock - min_stock >= max_profit:
                max_profit = max_stock - min_stock

        return max_profit


def main(args):
    prices = args[0]
    prices = list(prices)
    prices_int = []
    for price in prices:
        prices_int.append(int(price))

    sol = Solution()
    print('Solution: ', sol.maxProfit(prices_int))
            

if __name__ == "__main__":
    main(sys.argv[1:])
