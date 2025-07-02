def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    for i in prices:
        minPrice = min(minPrice, i)
        maxProfit = max(maxProfit, i - minPrice)
    return maxProfit


print(maxProfit([12, 4, 6, 8, 9, 1]))
