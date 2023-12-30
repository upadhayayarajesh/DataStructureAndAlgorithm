def is_sorted(arr):
    """
    Check if an array is sorted in ascending order
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array
    :return: Boolean which checks if the array is sorted or not.
    """
    smallest = 0
    for i, v in enumerate(arr):
        if v < arr[smallest]:
            return False
        smallest = i
    return True


if __name__ == '__main__':
    test_arr_1 = [8, 12, 15]  # O/P True
    test_arr_2 = [8, 10, 10, 12]  # O/p True
    test_arr_3 = [100]  # O/P True
    test_arr_4 = [100, 20, 200]  # O/P False

    print(is_sorted(test_arr_1))
    print(is_sorted(test_arr_2))
    print(is_sorted(test_arr_3))
    print(is_sorted(test_arr_4))
