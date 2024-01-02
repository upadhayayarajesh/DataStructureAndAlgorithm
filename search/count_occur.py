from first_occurance import first_occurrence
from last_occurance import last_occurrence


def count_occurrence(arr, s):
    """
    Find the total number of occurrences of s in an array.
    Time Complexity: O(log(n))
    Space Complexity: O(1)
    :param arr: Array
    :param s: Element to be found.
    :return: Number of elements of s.
    """
    first = first_occurrence(arr, s)
    if first == -1:
        return 0
    return last_occurrence(arr, s) - first + 1


if __name__ == '__main__':
    test_arr_1 = [5, 10, 10, 15, 15]
    test_arr_2 = [10, 10, 10]

    print(count_occurrence(test_arr_1, 15))  # O/P = 4
    print(count_occurrence(test_arr_2, 10))  # O/P = 2
