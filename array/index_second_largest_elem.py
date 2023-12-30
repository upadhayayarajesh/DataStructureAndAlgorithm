def second_largest_elem(array):
    """
    Find the second-largest element in the array
    Time complexity: O(N)
    Space complexity: O(1)
    :param array: Array to find the largest element in the array.
    :return: Index of the second-largest element in the array
    """
    largest_index = 0
    second_largest_index = -1
    for i, v in enumerate(array):
        if v > array[largest_index]:
            second_largest_index = largest_index
            largest_index = i
        elif v < array[largest_index]:
            if second_largest_index == -1:
                second_largest_index = i
            elif v > array[second_largest_index]:
                second_largest_index = i
    return second_largest_index


if __name__ == '__main__':
    test_arr_1 = [10, 5, 8, 20]  # O/P = 0
    test_arr_2 = [20, 10, 20, 8, 12]  # O/P = 4
    test_arr_3 = [10, 10, 10]  # O/P = -1

    print(second_largest_elem(test_arr_1))
    print(second_largest_elem(test_arr_2))
    print(second_largest_elem(test_arr_3))
