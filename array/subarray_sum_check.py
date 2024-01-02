def subarray_sum_check_1(arr, target):
    """
    Find if the target sum exists or not in subarray
    Time Complexity: O(N^2)
    Space Complexity: O (1)
    :param arr: Array
    :param target: Integer
    :return: Boolean
    """

    for i in range(len(arr)):
        curr_sub = arr[i]
        if curr_sub == target:
            return True
        for j in range(i + 1, len(arr)):
            curr_sub += arr[j]
            if curr_sub == target:
                return True
            elif curr_sub > target:
                break
    return False


def subarray_sum_check_2(arr, target):
    """
    Efficient approach to find if the target sum exists or not in subarray.
    Time Complexity: O(N)
    Space Complexity: O (1)
    :param arr: Array
    :param target: Integer
    :return: Boolean
    """
    curr_wind = 0
    end = 0
    start = 0
    while end < len(arr):
        curr_wind += arr[end]
        while target < curr_wind:
            curr_wind -= arr[start]
            start += 1
        if curr_wind == target:
            return True
        end += 1
    return False


if __name__ == '__main__':
    test_arr_1 = [1, 4, 20, 3, 10, 5]
    test_arr_2 = [1, 4, 0, 0, 3, 10, 5]
    test_arr_3 = [2, 4]

    print(subarray_sum_check_1(test_arr_1, 33))  # O/P = T
    print(subarray_sum_check_1(test_arr_2, 7))  # O/P = T
    print(subarray_sum_check_1(test_arr_3, 7))  # O/P = F

    print(subarray_sum_check_2(test_arr_1, 33))
    print(subarray_sum_check_2(test_arr_2, 7))
    print(subarray_sum_check_2(test_arr_3, 7))
