def sum(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError
    if a < 0 or b < 0:
        raise ValueError
    else:
        return int(a) + int(b)
