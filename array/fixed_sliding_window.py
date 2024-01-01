def fixed_sliding_window(arr, k):
    """
    Fixed window sliding technique of k sizes.
    Time Complexity: O(N * k)
    Space Complexity: O(1)
    :param arr:
    :param k:
    :return:
    """
    res = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, i + k):
            if j >= len(arr):
                break
            curr_sum += arr[j]
        res = max(res, curr_sum)
    return res


if __name__ == '__main__':
    test_arr_1 = [1, 8, 30, -5, 20, 7]
    test_arr_2 = [5, -10, 6, 90, 3]

    print(fixed_sliding_window(test_arr_1, 3))
    print(fixed_sliding_window(test_arr_2, 2))
