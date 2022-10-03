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
    DP = [None] * n
    DP[0], DP[1] = 1, 1

    for i in range(2, n):
        DP[i] = DP[i - 1] + DP[i - 2]

    return DP[-1]


if __name__ == "__main__":
    result1 = domino(40)
    result2 = domino_fast(40)
    
    print(result1, result2)
