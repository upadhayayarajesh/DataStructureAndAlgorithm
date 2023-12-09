def factorial_iterative(n):
    """
    Iterative solution
    Factorial is the multiplication of number from one to n.
    Time Complexity:Theta(n)
        - Looping through the n.
    Space Complexity: o(c)
        - Not creating any array or variable.
    :param n: Integer greater than or equal to zero.
    :return: Factorial of n
    """
    if n <= 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def factorial_recursive(n):
    """
     Recursive solution
    Factorial is the multiplication of number from one to n.
    Time Complexity:(n)
        - Looping through the n.
    Space Complexity: Theta(n+1)
        - Not creating any array or variable.
    :param n: Integer greater than or equal to zero.
    :return: Factorial of n
    """
    if n <= 0:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    # Iterative
    print(factorial_iterative(4))  # 24
    print(factorial_iterative(6))  # 720
    print(factorial_iterative(0))  # 1

    print("\n")

    # Recursive
    print(factorial_recursive(4))  # 24
    print(factorial_recursive(6))  # 720
    print(factorial_recursive(0))  # 1
