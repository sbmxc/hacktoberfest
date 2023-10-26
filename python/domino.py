"""
Exercise picture
https://i.imgur.com/Ijp6QEe.png
"""

def domino_fast(n):
    a, b = 1, 1

    for _ in range(2, n):
        a, b = b, a + b

    return b


def domino(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    DP = [None] * n
    DP[0], DP[1] = 1, 1

    for i in range(2, n):
        DP[i] = DP[i - 1] + DP[i - 2]

    return DP[-1]

def domino_sum(n):
    sum1 = sum(domino(i) for i in range(1, n + 1))
    sum2 = sum(domino_fast(i) for i in range(1, n + 1))
    return sum1, sum2

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    result1 = domino(n)
    result2 = domino_fast(n)
    sum_result1, sum_result2 = domino_sum(n)

    print("Result for domino({}): {}".format(n, result1))
    print("Result for domino_fast({}): {}".format(n, result2))
    print("Sum of the first {} terms using domino: {}".format(n, sum_result1))
    print("Sum of the first {} terms using domino_fast: {}".format(n, sum_result2))

