__author__ = 'Нина'


def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)

print(euclid(*(int(x) for x in input().split())))
