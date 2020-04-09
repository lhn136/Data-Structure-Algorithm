def maxProfit(prices):
    """

    :param prices: array of integers
    :return: return max profit in which you were to buy and sell the stock
    """
    profit = 0
    min = float('inf')
    for index,valNum in enumerate(prices):
        ifSoldProfitNow = ( valNum - min )
        if valNum < min :
            # print(min)
            min = valNum
        elif ifSoldProfitNow>profit:
            profit =  ifSoldProfitNow

    return profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([2,4,1]))
print(maxProfit([3,2,6,5,0,3]))