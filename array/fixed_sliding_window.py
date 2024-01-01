def fixed_sliding_window_1(arr, k):
    """
    Fixed window sliding technique of k sizes.
    Time Complexity: O(N * k)
    Space Complexity: O(1)
    :param arr: Array
    :param k: size of a window.
    :return: Integer
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


def fixed_sliding_window_2(arr, k):
    """
      Fixed window sliding technique of k sizes.
      Time Complexity: O(N)
      Space Complexity: O(1)
      :param arr: Array
      :param k: size of a window.
      :return: Integer
      """
    curr_wind_sum = 0
    for i in range(k):
        curr_wind_sum += arr[i]
    res = curr_wind_sum
    for i in range(k, len(arr)):
        curr_wind_sum = curr_wind_sum - arr[i - k] + arr[i]
        res = max(res, curr_wind_sum)
    return res


if __name__ == '__main__':
    test_arr_1 = [1, 8, 30, -5, 20, 7]
    test_arr_2 = [5, -10, 6, 90, 3]

    print(fixed_sliding_window_1(test_arr_1, 3))  # O/P = 45
    print(fixed_sliding_window_1(test_arr_2, 2))  # O/P = 96

    print(fixed_sliding_window_2(test_arr_1, 3))  # O/P = 45
    print(fixed_sliding_window_2(test_arr_2, 2))  # O/P = 96
