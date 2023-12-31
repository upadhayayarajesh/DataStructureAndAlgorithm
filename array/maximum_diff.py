def maximum_diff_1(arr):
    """
    Find the maximum difference between arr[j] - arr [i] such that j > i
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    :param arr: Array
    :return: Maximum difference between arr[j] - arr [i].
    """
    max_diff = None
    for j in range(len(arr) - 1, 0, -1):
        for i in range(j - 1, -1, -1):
            if max_diff is None:
                max_diff = arr[j] - arr[i]
            else:
                max_diff = max(max_diff, (arr[j] - arr[i]))
    return max_diff


def maximum_diff_2(arr):
    """
    Find the maximum difference between arr[j] - arr [i] such that j > i
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array
    :return: Maximum difference between arr[j] - arr [i].
    """
    lowest = arr[0]
    max_val = arr[1] - arr[0]
    for j in range(1, len(arr)):
        max_val = max(max_val, (arr[j] - lowest))
        lowest = min(lowest, arr[j])
    return max_val


if __name__ == '__main__':
    test_arr_1 = [2, 3, 10, 6, 4, 8, 1]  # O/P = 8
    test_arr_2 = [7, 9, 5, 6, 3, 2]  # O/P = 2
    test_arr_3 = [10, 20, 30]  # O/P = 20
    test_arr_4 = [30, 10, 8, 2]  # O/P = -2

    print(maximum_diff_1(test_arr_1))
    print(maximum_diff_1(test_arr_2))
    print(maximum_diff_1(test_arr_3))
    print(maximum_diff_1(test_arr_4))

    print(maximum_diff_2(test_arr_1))
    print(maximum_diff_2(test_arr_2))
    print(maximum_diff_2(test_arr_3))
    print(maximum_diff_2(test_arr_4))
