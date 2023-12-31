def move_all_zero_last(arr):
    """
    Move all the zero to the end of the array
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array
    :return: Arrays with zero to the end of the array and non-zero element to the beginning of the array
    keeping the original order.
    """
    res = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[res]
            arr[res] = arr[i]
            arr[i] = temp
            res += 1
    return arr


if __name__ == '__main__':
    test_arr_1 = [8, 5, 0, 10, 0, 20]
    test_arr_2 = [0, 0, 10, 0]
    test_arr_3 = [10, 0, 0, 0]
    print(move_all_zero_last(test_arr_1))
    print(move_all_zero_last(test_arr_2))
    print(move_all_zero_last(test_arr_3))
