import math

__author__ = 'Nina'


f = open('/home/nina/Bio_Py/dict.txt', 'r')
contents = f.read()
words = contents.split('\n')
a, n, v = 0, 0, 0
a_n_v = 0
for word in words:
    if word[-2:] == 'yo':
        a += 1
    elif word[-2:] == 'ka':
        n += 1
    else:
        v += 1
for i in range(0, a):
    a_n_v += math.factorial(a)//math.factorial(i)
print(a_n_v * n * v)
