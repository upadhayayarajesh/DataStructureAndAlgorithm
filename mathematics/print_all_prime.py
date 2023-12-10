import math


# Sieve of Eratosthenes

def all_prime(n):
    """
    Finds all prime numbers using naive approach
    Time Complexity: O(n * sqrt (n))
        - Sqrt complexity for checking prime number.
    Space Complexity: O(c)
    :param n:
    :return:
    """
    for i in range(2, n + 1):
        if is_prime(i):
            print(i)


def is_prime(n):
    """
    Checks if a number is prime or not.
    :param n:  Positive Integer number to check
    :return:  Boolean True if number is prime, False otherwise
    """
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """
    Finds the all prime factors of a number using Sieve of Eratosthenes algorithm
    Time Complexity: O( n log log (n))
        - It's complex to explain log n from finding the prime and log n from the marking them as false.
        - Log log n complexity increases very slowly even less than log n
    Space Complexity: O(n)
        -Creating an array of true boolean value
    :param n:
    :return: Prime Factor of n using Sieve of Eratosthenes algorithm
    """
    is_prime_array = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime_array[i]:
            print(i)
            start = i * i
            for j in range(start, n + 1, i):
                if is_prime_array[j]:
                    is_prime_array[j] = False


if __name__ == '__main__':
    sieve_of_eratosthenes(23)
    sieve_of_eratosthenes(7)
