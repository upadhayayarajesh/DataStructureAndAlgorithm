def max_element_range_1(arr_start, arr_end):
    """
    Find the element appears maximum times in the range between arr_start and arr_end.
    Element in the arr_start and arr_end are less than 100.
    Time Complexity: O(N * 100(max_value))
    Time Complexity: O(100(max_value)
    :param arr_start: Start of the range for i element
    :param arr_end:  End of the range for i element
    :return: max appear an element in the range.
    """
    fre = [0] * 100
    for i in range(len(arr_start)):
        for j in range(arr_start[i], arr_end[i] + 1):
            fre[j] += 1
    res = 0
    for i in range(len(fre)):
        if fre[i] > fre[res]:
            res = i

    return res


def max_element_range_2(arr_start, arr_end):
    """
    Effective approach to solve using a prefix sum array.
    Find the element appears maximum times in the range between arr_start and arr_end.
    Elements in the arr_start and arr_end are less than 100.
    Time Complexity: O(N + 100(max_value))
    Time Complexity: O(100(max_value)
    :param arr_start: Start of the range for i element
    :param arr_end:  End of the range for i element
    :return: max appear an element in the range.
        """
    fre = [0] * 101
    for i in range(len(arr_start)):
        fre[arr_start[i]] = 1
        fre[arr_end[i] + 1] = -1

    count = 0
    for i in range(len(fre)):
        count += fre[i]
        fre[i] = count

    res = 0
    for i in range(len(fre)):
        if fre[i] > fre[res]:
            res = i

    return res


if __name__ == '__main__':
    test_arr_start_1 = [1, 2, 5, 15]
    test_arr_end_1 = [5, 8, 7, 18]

    test_arr_start_2 = [1, 2]
    test_arr_end_2 = [5, 4]

    print(max_element_range_1(test_arr_start_1, test_arr_end_1))  # O/P = 5
    print(max_element_range_1(test_arr_start_2, test_arr_end_2))  # O/P = 2

    print(max_element_range_2(test_arr_start_1, test_arr_end_1))
    print(max_element_range_2(test_arr_start_2, test_arr_end_2))
