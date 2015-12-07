import re
import sys

data = sys.stdin.read()
lst = re.findall('you', data)
print(len(lst))
