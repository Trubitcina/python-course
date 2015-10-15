__author__ = 'Нина'


def prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = int(input())
for i in range(n):
    print(prime(int(input())))
