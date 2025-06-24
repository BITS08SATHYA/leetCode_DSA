def maxProfit(prices):
    left = 0
    profit = 0

    for right in range(1, len(prices)):
        if prices[right] < prices[left]:
            left = right
        else:
            profit = max(profit, prices[right] - prices[left])
    return profit


prices = [3,2,4,9]
print(maxProfit(prices))