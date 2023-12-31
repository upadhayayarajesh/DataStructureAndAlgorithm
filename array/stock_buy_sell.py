def stock_buy_and_sell(prices):
    """
    Making the profit by sell the stock on a day( array index) lower and selling in a height day( array index).
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param prices:  Array stock selling price.
    :return: Max profit.
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


if __name__ == "__main__":
    arr_test_1 = [1, 5, 3, 8, 12]  # O/P = 13
    arr_test_2 = [30, 20, 10]  # O/P = 0
    arr_test_3 = [10, 20, 30]  # O/P = 20
    arr_test_4 = [1, 5, 3, 1, 2, 8]  # O/P = 11

    print(stock_buy_and_sell(arr_test_1))
    print(stock_buy_and_sell(arr_test_2))
    print(stock_buy_and_sell(arr_test_3))
    print(stock_buy_and_sell(arr_test_4))
