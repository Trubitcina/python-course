import re
import sys

data = sys.stdin.read()
data = data.split('\n')
num = 0
for line in data:
    num += 1
    result = re.match(' *([\w,. ]+) = ', line)
    if result is not None:
        answer = list(result.groups())
        for i in answer:
            print(num, ' '.join(i.split(', ')))
