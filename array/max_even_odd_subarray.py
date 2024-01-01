def max_even_odd_subarray(arr):
    """
    Find the maximum even odd subarray within an array
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array
    :return: Integer
    """
    max_even_orr = 1
    prev_even_orr = 1
    for i in range(1, len(arr)):
        if (arr[i - 1] % 2 != 0 and arr[i] % 2 == 0) or (arr[i - 1] % 2 == 0 and arr[i] % 2 == 1):
            max_even_orr = max_even_orr + 1
            prev_even_orr = max(prev_even_orr, max_even_orr)
        else:
            max_even_orr = 1
    return prev_even_orr


if __name__ == '__main__':
    test_arr_1 = [10, 12, 14, 7, 8]
    test_arr_2 = [7, 10, 13, 14]
    test_arr_3 = [10, 12, 8, 4]

    print(max_even_odd_subarray(test_arr_1))
    print(max_even_odd_subarray(test_arr_2))
    print(max_even_odd_subarray(test_arr_3))
