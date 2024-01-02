def equilibrium_point_1(arr):
    """
    Find the equilibrium point of an array
    Equilibrium point means the sum of element in the left of it is equal to the sum of element in the right of it.
    Time Complexity: O(N)
    Space Complexity: O(N)
    :param arr: Array
    :return: Boolean
    """
    prefix_sum = [arr[0]]
    suffix_sum = [None] * len(arr)
    for i in range(1, len(arr)):
        prefix_sum.append(arr[i] + prefix_sum[i - 1])
    suffix_sum[(len(arr) - 1)] = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]

    for i in range(len(arr)):
        if suffix_sum[i] == prefix_sum[i]:
            return True
    return False


def equilibrium_point_2(arr):
    """
       Find the equilibrium point of an array
       Equilibrium point means the sum of element in the left of it is equal to the sum of element in the right of it.
       Time Complexity: O(N)
       Space Complexity: O(1)
       :param arr: Array
       :return: Boolean
       """
    right_sum = 0
    for i, v in enumerate(arr):
        right_sum += v
    left_sum = 0
    for i, v in enumerate(arr):
        right_sum -= v
        if left_sum == right_sum:
            return True
        left_sum += v
    return False


if __name__ == '__main__':
    test_arr_1 = [3, 4, 8, -9, 20, 6]
    test_arr_2 = [4, 2, -2]
    test_arr_3 = [4, 2, 2]

    print(equilibrium_point_1(test_arr_1))  # O/P = True
    print(equilibrium_point_1(test_arr_2))  # O/P = True
    print(equilibrium_point_1(test_arr_3))  # O/P = False

    print(equilibrium_point_2(test_arr_1))  # O/P = True
    print(equilibrium_point_2(test_arr_2))  # O/P = True
    print(equilibrium_point_2(test_arr_3))  # O/P = False
