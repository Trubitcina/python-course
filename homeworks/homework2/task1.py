__author__ = 'Нина'


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def combinations(n, k):
    if k > n:
        return 0
    elif k == n | k == 0:
        return 1
    else:
        return (factorial(n) // (factorial(k) * factorial(n - k)))

print(combinations(*(int(x) for x in input().split())))
