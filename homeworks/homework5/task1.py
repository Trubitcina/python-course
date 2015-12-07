import re
import sys

data = sys.stdin.read()
lst = re.findall('(y|Y)ou', data)
print(len(lst))
