def subset_sum(s, sum_add, current_value, index):
    """
    Find the total count of the subset in s
    TIme Complexity: O(2^n)
    Space Complexity: O(2^n)
    :param sum_add:
    :param index:
    :param current_value:
    :param s: Set
    :return: Integer
    """
    if index == len(s):
        if sum(current_value) == sum_add:
            return 1
        return 0

    cur_arr = current_value[:]
    a = subset_sum(s, sum_add, cur_arr, index + 1)
    cur_arr.append(s[index])
    b = subset_sum(s, sum_add, cur_arr, index + 1)

    return a + b


if __name__ == '__main__':
    print(subset_sum([10, 15, 20], 25, [], 0))
