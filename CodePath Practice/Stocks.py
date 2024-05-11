from operator import index


def StockProfit(prices):
    buy_price = prices[0]
    if len(prices) > 1 :
        sell_price = prices[1]
    else:
        return 0
    profit = 0
    for p in prices[1:]:
        if p < buy_price:
            buy_price = p
        if (p - buy_price) > profit:
            profit = p - buy_price
            sell_price = p       
    return 0 if index(buy_price) >= index(sell_price) else profit
    
    


def main():
    prices = [1]
    '''[7,1,5,3,6,4], [7,6,4,3,1],[2,4,1], [1,2], [2,1]'''
    '''for i in n:
        prices[i] = input("Please Enter a number: ")'''
    profit = StockProfit(prices)
    print(f'The Maximum Profit made is {profit}')


if __name__ == '__main__':
    main()