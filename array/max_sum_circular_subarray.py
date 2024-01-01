def max_sum_circular_subarray(arr):
    """
    Find the maximum of circular subarray sum in an array
    Time Complexity: O(N ^2)
    Space Complexity: O(1)
    :param arr:Array
    :return: Integer
    """
    max_sum = arr[0]
    for i in range(len(arr)):
        max_sum = max(max_sum, arr[i])
        counter = (i + 1) % len(arr)
        local_sum = arr[i]
        while i != counter:
            local_sum += arr[counter]
            max_sum = max(max_sum, local_sum)
            counter = (counter + 1) % len(arr)
    return max_sum


def max_sum_circular_subarray_2(arr):
    """
    Find the maximum of circular subarray sum in an array efficient solution
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr:Array
    :return: Integer
    """
    max_sum = arr[0]
    min_sum = arr[0]
    max_end = arr[0]
    min_end = arr[0]
    total_sum = arr[0]
    for i in range(1, len(arr)):
        max_end = max(max_end + arr[i], arr[i])
        max_sum = max(max_sum, max_end)
        min_end = min(min_end + arr[i], arr[i])
        min_sum = min(min_end, min_sum)
        total_sum += arr[i]
    if max_sum < 0:
        return max_sum
    max_sum = max(max_sum, (total_sum - min_sum))
    return max_sum


if __name__ == '__main__':
    test_arr_1 = [5, -2, 3, 4]  # O/P = 12
    test_arr_2 = [2, 3, -4]  # O/P = 5
    test_arr_3 = [-8, 7, 6]  # O/P = 13
    test_arr_4 = [3, -4, 5, 6, -8, 7]  # O/P = 17
    test_arr_5 = [-3, 4, 6, -2]  # O/P = 10
    test_arr_6 = [-3, -2, -1]  # O/P = -1

    print(max_sum_circular_subarray(test_arr_1))
    print(max_sum_circular_subarray(test_arr_2))
    print(max_sum_circular_subarray(test_arr_3))
    print(max_sum_circular_subarray(test_arr_4))
    print(max_sum_circular_subarray(test_arr_5))
    print(max_sum_circular_subarray(test_arr_6))

    print(max_sum_circular_subarray_2(test_arr_1))
    print(max_sum_circular_subarray_2(test_arr_2))
    print(max_sum_circular_subarray_2(test_arr_3))
    print(max_sum_circular_subarray_2(test_arr_4))
    print(max_sum_circular_subarray_2(test_arr_5))
    print(max_sum_circular_subarray_2(test_arr_6))
