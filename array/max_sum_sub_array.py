def max_sum_sub_array_1(arr):
    """
    Naive approach to find the sum of max subarray in an array.
    Time Complexity: O(N ^2)
    Space Complexity: O(1)
    :param arr:
    :return:
    """
    max_sum = arr[0]
    for i, v in enumerate(arr):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum


def max_sum_sub_array_2(arr):
    """
    Effective approach to find the sum of max subarray in an array.
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array to be summed
    :return: Integer
    """
    res = arr[0]
    max_ending = arr[0]
    for i in range(1, len(arr)):
        max_ending = max(max_ending + arr[i], arr[i])
        res = max(res, max_ending)
    return res


if __name__ == '__main__':
    test_arr_1 = [2, 3, -8, 7, -1, 2, 3]  # O/P = 11
    test_arr_2 = [5, 8, 3]  # O/P = 16
    test_arr_3 = [-6, -1, -8]  # O/P = -1

    print(max_sum_sub_array_1(test_arr_1))
    print(max_sum_sub_array_1(test_arr_2))
    print(max_sum_sub_array_1(test_arr_3))

    print(max_sum_sub_array_2(test_arr_1))
    print(max_sum_sub_array_2(test_arr_2))
    print(max_sum_sub_array_2(test_arr_3))
