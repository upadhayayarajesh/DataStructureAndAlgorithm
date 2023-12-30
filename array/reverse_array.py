def reverse_array(arr):
    """
    Reverse the array
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param arr: Array to be reversed
    :return: Reversed array
    """
    start_index = 0
    end_index = len(arr) - 1
    while start_index < end_index:
        temp = arr[start_index]
        arr[start_index], arr[end_index] = arr[end_index], temp
        end_index -= 1
        start_index += 1
    return arr


if __name__ == '__main__':
    test_arr_1 = [10, 5, 7, 30]  # O/P = [30, 7, 5, 10]
    test_arr_2 = [30, 20, 5]  # O/P = [5, 20, 30]

    print(reverse_array(test_arr_1))
    print(reverse_array(test_arr_2))
