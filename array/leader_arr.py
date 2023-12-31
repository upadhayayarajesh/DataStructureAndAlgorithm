def leader_arr(arr):
    """
    Find leader in an array
    Leader in an array means every element after that element needs to be strictly less than that element
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array to be checked
    :return: None
    """
    leader = arr[-1]
    print(leader)
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > leader:
            leader = arr[i]
            print(leader)


if __name__ == '__main__':
    test_arr_1 = [7, 10, 4, 10, 6, 5, 2]  # O/P = 10 6 5 2
    test_arr_2 = [10, 20, 30]  # O/P = 30
    test_arr_3 = [30, 20, 10]  # O/P = 10 20 30

    leader_arr(test_arr_1)
    leader_arr(test_arr_2)
    leader_arr(test_arr_3)
