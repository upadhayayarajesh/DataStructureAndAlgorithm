def sum_n_natural_number(n):
    """
     To find the sum of n natural number.
     Time Complexity:O(c)
        - Sum of Natural number is the formula n*(n+1)/2 so constant time.
     Space Complexity:o(c)
        - Takes constant time.
    :param n: Integer number to find the sum.
    :return: sum of N natural number
    """
    return int(n * ((n + 1) / 2));


if __name__ == '__main__':
    print(sum_n_natural_number(5))
