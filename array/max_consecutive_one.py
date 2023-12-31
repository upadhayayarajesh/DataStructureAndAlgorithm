def max_consecutive_one(binary_arr):
    """
    Finds the maximum sum of consecutive one in the given binary array
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param binary_arr: Array of zero and one
    :return: Positive integer
    """
    max_con_one = 0
    fre = 0
    for i, v in enumerate(binary_arr):
        if v == 1:
            fre += 1
            max_con_one = max(max_con_one, fre)
        else:
            fre = 0
    return max_con_one


if __name__ == '__main__':
    test_arr_1 = [0, 1, 1, 0, 1, 0]  # O/P = 2
    test_arr_2 = [1, 1, 1, 1]  # O/P = 4
    test_arr_3 = [0, 0, 0]  # O/P = 0
    test_arr_4 = [1, 0, 1, 1, 1, 1, 0, 1, 1]  # O/P = 4

    print(max_consecutive_one(test_arr_1))
    print(max_consecutive_one(test_arr_2))
    print(max_consecutive_one(test_arr_3))
    print(max_consecutive_one(test_arr_4))
