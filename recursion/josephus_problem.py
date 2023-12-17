def josephus_problem(n, k):
    """
     Finds the person killed in the josephus problem
     Time Complexity: O(n)
     Space Complexity: O(n)
    :param n: number of people in circle
    :param k: difference of people killed
    :return: people who remains till last.
    """
    if n == 1:
        return 0
    else:
        return (josephus_problem(n - 1, k) + k) % n


if __name__ == '__main__':
    print(josephus_problem(5, 3))
