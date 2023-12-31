def left_rotate(arr):
    """
    Left rotate given an array by one index
    Time Complexity: O(N)
    Space Complexity: O(1)
    :return: Array
    """
    for i, v in enumerate(arr):
        if i == 0:
            continue
        temp = arr[i - 1]
        arr[i - 1] = v
        arr[i] = temp
    return arr


if __name__ == '__main__':
    test_arr_1 = [1, 2, 3, 4, 5]  # O/P = [5, 4, 3, 2, 1]
    test_arr_2 = [30, 5, 20]  # O/P = [5, 20, 30]
    print(left_rotate(test_arr_1))
    print(left_rotate(test_arr_2))
