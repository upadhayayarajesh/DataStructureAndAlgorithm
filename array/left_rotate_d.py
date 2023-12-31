def left_rotate_d_1(arr, d):
    """
    Left rotate the array by d index
    Time complexity: O(dN)
    Space complexity: O(1)
    :param arr: Array
    :param d: Positive Integer less than or equal to an element in the array
    :return: Array after left rotating by
    """
    for j in range(d):
        for i in range(len(arr)):
            if i == 0:
                continue
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr


def left_rotate_d_2(arr, d):
    """"
       Left rotate the array by d index
       Time complexity: O(N)
       Space complexity: O(d)
       :param arr: Array
       :param d: Positive Integer less than or equal to an element in the array
       :return: Array
       """

    first_d = []
    for i in range(d):
        first_d.append(arr[i])
    counter = 0
    for i in range(d, len(arr)):
        arr[counter] = arr[i]
        counter += 1

    for i in range(d):
        arr[counter] = first_d[i]
        counter += 1
    return arr


def left_rotate_d_3(arr, d):
    """"
    Left rotate the array by d index Efficient approach.
    Time complexity: O(N)
    Space complexity: O(1)
    :param arr: Array
    :param d: Positive Integer less than or equal to an element in the array
    :return: Array
    """
    reverse(arr, 0, d - 1)
    reverse(arr, d, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)
    return arr


def reverse(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start], arr[end] = arr[end], temp
        start, end = start + 1, end - 1


if __name__ == "__main__":
    test_arr_1 = [1, 2, 3, 4, 5]  # O/P = [3, 4, 5, 1, 2]
    test_arr_2 = [10, 5, 30, 15]  # O/p = [15, 10, 5, 30]

    print(left_rotate_d_1(test_arr_1, 2))
    print(left_rotate_d_1(test_arr_2, 3))

    test_arr_1 = [1, 2, 3, 4, 5]  # O/P = [3, 4, 5, 1, 2]
    test_arr_2 = [10, 5, 30, 15]  # O/p = [15, 10, 5, 30]

    print(left_rotate_d_2(test_arr_1, 2))
    print(left_rotate_d_2(test_arr_2, 3))

    test_arr_1 = [1, 2, 3, 4, 5]  # O/P = [3, 4, 5, 1, 2]
    test_arr_2 = [10, 5, 30, 15]  # O/p = [15, 10, 5, 30]

    print(left_rotate_d_3(test_arr_1, 2))
    print(left_rotate_d_3(test_arr_2, 3))
