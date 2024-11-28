class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left_pointer, right_pointer = 0, 1 # Two pointers indicating when we buy and when we sell respecively
        max_profit = 0

        while right_pointer < len(prices):
            buy_price = prices[left_pointer] 
            sell_price = prices[right_pointer]

            if buy_price < sell_price:
                profit = sell_price - buy_price
                max_profit = max(max_profit, profit) # In profitable case, check whether profit is bigger than our current max 
            else:
                left_pointer = right_pointer # In not profitable case update left pointer because in this case the right would be less than the left
            right_pointer += 1  # Update right pointer either way to keep searching through the list

        return max_profit

solution = Solution()
stock_prices = [1, 5, 0, 9]
print(solution.maxProfit(stock_prices))

"""
Time: O(n)
    Loop through list is linear operation

Space: O(1)
    Variables are constant

Why does this work? 
Whenever we get a profit we check if it's bigger than the max therefor getting the max profit
"""
