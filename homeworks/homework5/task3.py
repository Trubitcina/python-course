import re
import sys


data = sys.stdin.read()
data = data.split('\n')
num = 0
for line in data:
    num += 1
    results = re.findall('([\w]+) = ', line)
    if len(results) != 0:
        print(num, results[0])
