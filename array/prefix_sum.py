def get_sum_1(arr, s, e):
    """
    Find the sum of all numbers in s and e
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array
    :param s: start index
    :param e: end index
    :return: Sum of all numbers in s, e
    """
    result = 0
    for i in range(s, e + 1):
        result += arr[i]
    return result


def get_sum_2(arr, s, e):
    """
        Find the sum of all numbers in s and e.
        It does a prefix sum array we can make it global and time complexity is O(1).
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param arr: Array
        :param s: start index
        :param e: end index
        :return: Sum of all numbers in s, e
        """
    prefix_sum_arr = [arr[0]]
    for i in range(1, len(arr)):
        prefix_sum_arr.append(prefix_sum_arr[i - 1] + arr[i])
    if s == 0:
        return prefix_sum_arr[e]
    return prefix_sum_arr[e] - prefix_sum_arr[s - 1]


if __name__ == '__main__':
    test_arr_1 = [2, 8, 3, 9, 6, 5, 4]

    print(get_sum_1(test_arr_1, 0, 2))  # O/P = 12
    print(get_sum_1(test_arr_1, 1, 3))  # O/P = 20

    print(get_sum_2(test_arr_1, 0, 2))
    print(get_sum_2(test_arr_1, 1, 3))
