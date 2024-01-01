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


if __name__ == '__main__':
    test_arr_1 = [5, -2, 3, 4]  # O/P = 12
    test_arr_2 = [2, 3, -4]  # O/P = 5
    test_arr_3 = [-8, 7, 6]  # O/P = 13
    test_arr_4 = [3, -4, 5, 6, -8, 7]  # O/P = 17
    test_arr_5 = [-3, 4, 6, -2]  # O/P = 10

    print(max_sum_circular_subarray(test_arr_1))
    print(max_sum_circular_subarray(test_arr_2))
    print(max_sum_circular_subarray(test_arr_3))
    print(max_sum_circular_subarray(test_arr_4))
    print(max_sum_circular_subarray(test_arr_5))
