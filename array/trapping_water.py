def trap(arr):
    """
    Trapping the water post asked interview question.
    Time Complexity: O(N)
    Space Complexity: O(N)
    :param arr: Array of integers
    :return: Integer value of trapped water.
    """
    trapped_water = 0
    left_max = [None] * len(arr)
    right_max = [None] * len(arr)
    left_max[0] = arr[0]

    for i in range(1, len(arr)):
        left_max[i] = max(arr[i], left_max[i - 1])
    right_max[len(arr) - 1] = arr[- 1]

    for i in range(len(arr) - 2, -1, -1):
        right_max[i] = max(arr[i], right_max[i + 1])

    for i in range(len(arr)):
        trapped_water += min(left_max[i], right_max[i]) - arr[i]
    return trapped_water


if __name__ == '__main__':
    test_arr_1 = [2, 0, 2]  # O/P = 2
    test_arr_2 = [3, 0, 1, 2, 5]  # O/P = 6
    test_arr_3 = [1, 2, 3]  # O/P = 0
    test_arr_4 = [3, 2, 1]  # O/P = 0
    test_arr_5 = [5, 0, 6, 2, 3]  # O/P = 6
    test_arr_6 = [5, 5, 6, 6, 6]  # O/P = 0

    print(trap(test_arr_1))
    print(trap(test_arr_2))
    print(trap(test_arr_3))
    print(trap(test_arr_4))
    print(trap(test_arr_5))
    print(trap(test_arr_6))
